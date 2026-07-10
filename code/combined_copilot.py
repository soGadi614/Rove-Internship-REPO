import os
import sys
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag_loop import suggest_answer
from sop_match import match_sop
from Refund_Calculator import refund_calculator

REFUND_KEYWORDS = [
    "refund", "cancel", "canceled", "cancelled", "cancellation",
    "charged", "charge", "twice", "duplicate", "payment",
    "airline canceled", "hotel complaint"
]


def needs_refund_calculation(ticket):
    ticket_lower = ticket.lower()

    for keyword in REFUND_KEYWORDS:
        if keyword in ticket_lower:
            return True

    return False


def run_copilot(ticket):
    """
    Runs all Week 3 helpers together:
    1. Suggested answer
    2. SOP matcher
    3. Refund calculator, only if relevant
    """

    suggested = suggest_answer(ticket)
    sop = match_sop(ticket)

    if needs_refund_calculation(ticket):
        try:
            refund = refund_calculator(ticket)
        except Exception as error:
            refund = {
                "flagged": True,
                "flag_reason": f"Refund calculator could not process this ticket: {error}",
                "formatted_output": "Refund calculator failed. Manual review required."
            }
    else:
        refund = {
            "refund_applicable": False,
            "formatted_output": "No refund calculation needed for this ticket."
        }

    return {
        "ticket": ticket,
        "suggested_answer": suggested["answer"],
        "answer_sources": suggested["sources"],
        "sop_category": sop["category"],
        "sop_confidence": sop["confidence"],
        "sop_needs_agent_review": sop["needs_agent_review"],
        "sop_reason": sop["reason"],
        "sop_canned_response": sop["canned_response"],
        "sop_sources": sop["matched_sources"],
        "refund_result": refund
    }


def print_copilot_result(result):
    print("\n" + "=" * 70)
    print("ROVE COMBINED CO-PILOT RESULT")
    print("=" * 70)

    print("\nCUSTOMER TICKET:")
    print(result["ticket"])

    print("\nSUGGESTED ANSWER:")
    print(result["suggested_answer"])

    print("\nANSWER SOURCES:")
    if result["answer_sources"]:
        for source in result["answer_sources"]:
            print(f"- {source}")
    else:
        print("No answer sources found.")

    print("\nSOP MATCH:")
    print(f"Category: {result['sop_category']}")
    print(f"Confidence: {result['sop_confidence']}")
    print(f"Needs agent review: {result['sop_needs_agent_review']}")
    print(f"Reason: {result['sop_reason']}")

    print("\nSOP CANNED RESPONSE:")
    print(result["sop_canned_response"])

    print("\nSOP SOURCES:")
    if result["sop_sources"]:
        for source in result["sop_sources"]:
            print(f"- {source}")
    else:
        print("No SOP sources found.")

    print("\nREFUND RESULT:")
    print(result["refund_result"].get("formatted_output", result["refund_result"]))

    print("=" * 70)


st.title("Rove Combined Co-Pilot")

ticket = st.text_area(
    "Paste customer ticket:",
    height=200,
    key="copilot_ticket"
)

if st.button("Analyze", key="copilot_button"):
    if ticket.strip():
        result = run_copilot(ticket)

        st.subheader("Suggested Answer")
        st.write(result["suggested_answer"])

        st.subheader("SOP Match")
        st.write(f"Category: {result['sop_category']}")
        st.write(f"Confidence: {result['sop_confidence']}")
        st.write(result["sop_reason"])

        st.subheader("Refund Result")
        st.write(
            result["refund_result"].get(
                "formatted_output",
                result["refund_result"]
            )
        )
