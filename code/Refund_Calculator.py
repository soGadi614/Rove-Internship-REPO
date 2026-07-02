
"""
Rove Refund Calculator
Based on: Rove Member Support SOP - Refunds & Compensation FAQ
Uses OpenAI to extract ticket details; Python handles all math.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import json
import math
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Constants from the SOP
MILES_VALUE_STANDARD = 0.02       # $0.02 per mile (standard refund deduction)
MILES_VALUE_ROVE_RATE = 0.013     # $0.013 per mile (Rove Rate bookings)
MILES_VALUE_LOYALTY = 0.015       # $0.015 per mile (Loyalty Eligible bookings)


# Extract details from the ticket 
def extract_refund_details(ticket_text: str) -> dict:
    """
    Uses the LLM to read the messy ticket and pull out structured fields.
    The LLM reads; Python does the math (never the other way around).
    """
    prompt = f"""Read this Rove customer support ticket and extract refund-relevant details.
Return ONLY a valid JSON object with these exact fields (use null if not mentioned):

{{
  "refund_type": "standard" | "rove_rate" | "loyalty_eligible" | "flight" | "hotel_complaint" | "exception" | null,
  "original_refund_amount_usd": <number or null>,
  "miles_used": <number or null>,
  "booking_within_24hrs": <true | false | null>,
  "cancellation_initiated_by": "airline" | "customer" | "supplier_error" | null,
  "reservation_canceled": <true | false | null>,
  "reservation_refundable": <true | false | null>,
  "new_supplier_rate_usd": <number or null>,
  "original_miles_paid": <number or null>,
  "member_paid_hotel_directly_usd": <number or null>,
  "original_booking_cost_usd": <number or null>,
  "supplier_rate_usd": <number or null>,
  "issue_summary": "<one sentence describing the request>"
}}

Ticket:
{ticket_text}

Return ONLY the JSON. No explanation, no markdown, no extra text."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=500,
    )

    raw = response.choices[0].message.content.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Strip markdown fences if the model added them anyway
        cleaned = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned)


#  Apply real SOP rules 
def calculate_refund(details: dict) -> dict:
    """
    All arithmetic happens here in Python — never in the LLM's head.
    Each branch maps directly to a rule in the Rove SOP.
    """
    refund_type = details.get("refund_type")
    miles_used = details.get("miles_used") or 0
    original_amount = details.get("original_refund_amount_usd") or 0
    within_24hrs = details.get("booking_within_24hrs")
    canceled_by = details.get("cancellation_initiated_by")
    is_refundable = details.get("reservation_refundable")
    is_canceled = details.get("reservation_canceled")

    result = {
        "refund_amount_usd": None,
        "miles_refunded": 0,
        "miles_deduction_usd": 0,
        "reasoning": [],
        "agent_actions_required": [],
        "flagged": False,
        "flag_reason": None,
    }

    # reservation must be canceled first
    if is_canceled is False:
        result["flagged"] = True
        result["flag_reason"] = "Reservation has NOT been canceled yet. Resolve cancellation before processing refund."
        result["reasoning"].append(" SOP Step 2: Cancellation must be confirmed before any refund is processed.")
        return result

    # reservation must be refundable 
    if is_refundable is False and canceled_by != "supplier_error":
        result["flagged"] = True
        result["flag_reason"] = "Reservation is non-refundable. Escalate to team lead or supplier."
        result["reasoning"].append(" Reservation marked non-refundable. No automatic refund applies.")
        return result

    # FLIGHT: void within 24 hours (US DOT) 
    if refund_type == "flight" and within_24hrs:
        result["refund_amount_usd"] = original_amount
        result["reasoning"].append(
            "Flight canceled within 24 hours of booking → full void under US DOT guidelines."
        )
        result["agent_actions_required"].append(
            "Contact Duffel via Live Chat. Delete pre-filled sentence and enter: "
            "'Please cancel right away. No quote is needed as this is a void within 24 hours.'"
        )

    # FLIGHT: outside 24 hours 
    elif refund_type == "flight" and not within_24hrs:
        result["flagged"] = True
        result["flag_reason"] = "Flight outside 24-hour window. Refund depends on Duffel/airline approval."
        result["reasoning"].append(
            "Flight canceled outside 24-hour window. Submit cancellation quote through Duffel. "
            "Do NOT promise a refund until Duffel/airline confirms."
        )
        result["agent_actions_required"].append(
            "Submit cancellation quote via Duffel Chat or Email depending on case type. "
            "Present Duffel's confirmed amount to member and obtain approval before proceeding."
        )

    # STANDARD refund with miles used 
    elif refund_type == "standard" and miles_used > 0:
        miles_value = miles_used * MILES_VALUE_STANDARD
        final_refund = original_amount - miles_value
        result["refund_amount_usd"] = round(final_refund, 2)
        result["miles_deduction_usd"] = round(miles_value, 2)
        result["reasoning"] += [
            f"Miles used: {miles_used:,}",
            f"Miles value: {miles_used:,} × $0.02 = ${miles_value:.2f}",
            f"Original refundable amount: ${original_amount:.2f}",
            f"Final refund: ${original_amount:.2f} − ${miles_value:.2f} = ${final_refund:.2f}",
        ]
        result["agent_actions_required"] += [
            f"Inform member that {miles_used:,} miles (valued at ${miles_value:.2f}) will be deducted.",
            "Obtain member acknowledgment before processing.",
            "Document miles calculation and refund in CS Panel and Refund Tracker.",
        ]

    #  STANDARD refund, no miles used
    elif refund_type == "standard" and miles_used == 0:
        result["refund_amount_usd"] = round(original_amount, 2)
        result["reasoning"].append(
            f"No miles used. Full refund of ${original_amount:.2f} applies."
        )
        result["agent_actions_required"].append("Process refund via Stripe using Payment Intent ID.")

    # ROVE RATE partial refund (miles-paid booking)
    elif refund_type == "rove_rate":
        new_rate = details.get("new_supplier_rate_usd")
        original_miles = details.get("original_miles_paid") or 0
        if new_rate and original_miles:
            new_miles_raw = new_rate / MILES_VALUE_ROVE_RATE          
            new_miles = math.ceil(new_miles_raw / 1000) * 1000        # round up to nearest 1,000
            miles_refunded = original_miles - new_miles
            result["miles_refunded"] = miles_refunded
            result["reasoning"] += [
                f"Rove Rate booking. New supplier rate: ${new_rate}",
                f"New price in miles: ${new_rate} ÷ $0.013 = {new_miles_raw:.0f} → rounded up to {new_miles:,} miles",
                f"Miles refund: {original_miles:,} − {new_miles:,} = {miles_refunded:,} miles",
            ]
            result["agent_actions_required"].append(
                f"Refund {miles_refunded:,} miles to member's account."
            )
        else:
            result["flagged"] = True
            result["flag_reason"] = "Missing new supplier rate or original miles paid for Rove Rate calculation."

    # LOYALTY ELIGIBLE partial refund
    elif refund_type == "loyalty_eligible":
        new_rate = details.get("new_supplier_rate_usd")
        original_miles = details.get("original_miles_paid") or 0
        if new_rate and original_miles:
            new_miles_raw = new_rate / MILES_VALUE_LOYALTY
            new_miles = math.ceil(new_miles_raw / 1000) * 1000
            miles_refunded = original_miles - new_miles
            result["miles_refunded"] = miles_refunded
            result["reasoning"] += [
                f"Loyalty Eligible booking. New supplier rate: ${new_rate}",
                f"New price in miles: ${new_rate} ÷ $0.015 = {new_miles_raw:.0f} → rounded up to {new_miles:,} miles",
                f"Miles refund: {original_miles:,} − {new_miles:,} = {miles_refunded:,} miles",
            ]
            result["agent_actions_required"].append(
                f"Refund {miles_refunded:,} miles to member's account."
            )
        else:
            result["flagged"] = True
            result["flag_reason"] = "Missing new supplier rate or original miles paid for Loyalty Eligible calculation."

    # EXCEPTION: guest had to pay hotel again 
    elif refund_type == "exception":
        member_paid = details.get("member_paid_hotel_directly_usd") or 0
        original_booking = details.get("original_booking_cost_usd") or 0
        supplier_rate = details.get("supplier_rate_usd") or 0
        if member_paid and original_booking and supplier_rate:
            rate_difference = member_paid - supplier_rate
            total_refund = original_booking + max(0, rate_difference)
            result["refund_amount_usd"] = round(total_refund, 2)
            result["reasoning"] += [
                f"Exception case: member paid hotel directly (${member_paid}).",
                f"Original booking: ${original_booking} | Supplier rate: ${supplier_rate}",
                f"Rate difference covered: ${member_paid} − ${supplier_rate} = ${rate_difference}",
                f"Total refund: ${original_booking} + ${max(0, rate_difference)} = ${total_refund:.2f}",
            ]
            result["agent_actions_required"] += [
                "Request supplier cancellation without penalty.",
                f"Request supplier reimbursement for rate difference (${rate_difference}).",
                "Collect proof of payment and replacement reservation confirmation.",
            ]
        else:
            result["flagged"] = True
            result["flag_reason"] = "Exception case: missing payment details. Collect proof of payment before proceeding."

    #  HOTEL COMPLAINT 
    elif refund_type == "hotel_complaint":
        result["flagged"] = True
        result["flag_reason"] = "Hotel complaint — refund not automatically owed."
        result["reasoning"] += [
            "Hotel issues are the hotel's responsibility, not Rove's.",
            "No refund is owed unless the hotel approves it.",
        ]
        result["agent_actions_required"] += [
            "Ask member: did you speak with hotel management during your stay?",
            "Request photos, videos, or emails as evidence.",
            "Encourage member to seek resolution from the hotel first.",
            "Only escalate to supplier after hotel is unresponsive or refuses reasonable assistance.",
        ]

    # Unknown / missing info
    else:
        result["flagged"] = True
        result["flag_reason"] = "Could not determine refund type from ticket. Manual review required."
        result["reasoning"].append("Insufficient information to apply a refund rule automatically.")

    return result


# Format output for the agent 
def format_output(details: dict, result: dict) -> str:
    lines = [
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        "  ROVE REFUND CALCULATOR — AGENT VIEW",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
        f"Issue: {details.get('issue_summary', 'N/A')}",
        f"Refund type detected: {details.get('refund_type', 'unknown')}",
        "",
    ]

    if result["flagged"]:
        lines.append(f" FLAG: {result['flag_reason']}")
        lines.append("")

    if result["refund_amount_usd"] is not None:
        lines.append(f" Final refund amount: ${result['refund_amount_usd']:.2f}")
    if result["miles_refunded"]:
        lines.append(f"  Miles to refund: {result['miles_refunded']:,} miles")
    if result["miles_deduction_usd"]:
        lines.append(f"   (Miles deducted: ${result['miles_deduction_usd']:.2f})")

    if result["reasoning"]:
        lines.append("")
        lines.append(" Reasoning (SOP basis):")
        for r in result["reasoning"]:
            lines.append(f"   • {r}")

    if result["agent_actions_required"]:
        lines.append("")
        lines.append(" Agent actions required:")
        for a in result["agent_actions_required"]:
            lines.append(f"   → {a}")

    lines += [
        "",
        "  REMINDER: Never promise a refund before it is approved.",
        "   Always obtain member acknowledgment before processing.",
        "   Document all calculations in CS Panel and Refund Tracker.",
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
    ]
    return "\n".join(lines)


# Main function
def refund_calculator(ticket_text: str) -> dict:
    """
    Main entry point. Pass in a raw ticket string.
    Returns a dict with the result and a formatted string for the agent.
    """
    details = extract_refund_details(ticket_text)
    result = calculate_refund(details)
    result["formatted_output"] = format_output(details, result)
    result["extracted_details"] = details
    return result

# ---------------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------------
import streamlit as st

st.title("Refund Calculator")
st.write("Paste a support ticket below to calculate the refund per SOP rules.")

ticket_input = st.text_area("Ticket text", height=150)

if st.button("Calculate Refund"):
    if ticket_input.strip():
        with st.spinner("Analyzing ticket..."):
            result = refund_calculator(ticket_input)

        if result["flagged"]:
            st.warning(f"Flagged: {result['flag_reason']}")

        if result["refund_amount_usd"] is not None:
            st.success(f"Final refund amount: ${result['refund_amount_usd']:.2f}")

        if result["miles_refunded"]:
            st.write(f"Miles to refund: {result['miles_refunded']:,}")

        st.subheader("Full agent summary")
        st.text(result["formatted_output"])

        with st.expander("Raw extracted details"):
            st.json(result["extracted_details"])
    else:
        st.warning("Please enter a ticket first.")


