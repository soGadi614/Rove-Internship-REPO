# sop_match.py

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
from retrieval import retrieve_chunks


SOP_CATEGORIES = {
    "shopping_rewards_issue": {
        "description": "Shopping, dining, merchant rewards, pending Miles, missing shopping Miles, coupon use, or promo code issues.",
        "keywords": [
            "shopping", "dining", "merchant", "miles", "pending", "coupon",
            "promo", "promotion", "nike", "adidas", "purchase", "rewards"
        ],
        "canned_response": (
            "Thanks for reaching out. I can help look into your shopping or dining Miles. "
            "Shopping rewards can depend on merchant validation, purchase eligibility, location, "
            "and offer terms. If a coupon or promotional code was used, rewards may be reduced, "
            "removed, or disqualified depending on the merchant's terms."
        )
    },

    "refund_request": {
        "description": "Refunds, cancellations, duplicate charges, payment issues, or original payment method questions.",
        "keywords": [
            "refund", "cancel", "cancelled", "canceled", "cancellation",
            "charged", "charge", "twice", "duplicate", "payment", "money"
        ],
        "canned_response": (
            "Thanks for reaching out. I can help review the refund status. "
            "Refund eligibility depends on the booking terms and provider confirmation. "
            "If approved, refunds are generally returned to the original payment method within the stated processing timeline."
        )
    },

    "account_login_issue": {
        "description": "Login problems, verification code issues, OTP issues, password problems, or account access.",
        "keywords": [
            "login", "log", "code", "verification", "otp", "account",
            "password", "sign", "access"
        ],
        "canned_response": (
            "Thanks for reaching out. I'm sorry you're having trouble accessing your account. "
            "Please try logging out, logging back in, and requesting a new code. "
            "If the issue continues, please confirm the email address connected to your Rove account so we can investigate further."
        )
    },

    "referral_issue": {
        "description": "Referral Miles, referral bonus, referral links, friends signing up, or missing referral rewards.",
        "keywords": [
            "referral", "referred", "friend", "bonus", "link", "signup",
            "signed", "invite"
        ],
        "canned_response": (
            "Thanks for reaching out. Referral Miles may not post immediately after signup. "
            "We can investigate further once we have the referral link, the referred member's name, "
            "and the phone number or email connected to the referred account."
        )
    },

    "hotel_issue": {
        "description": "Hotel bookings, hotel stays, hotel Miles, reservations, rooms, amenities, check-in, or hotel cancellation issues.",
        "keywords": [
            "hotel", "stay", "reservation", "room", "check-in", "checkout",
            "hilton", "hyatt", "marriott", "amenities", "towels"
        ],
        "canned_response": (
            "Thanks for reaching out. I can help review your hotel-related issue. "
            "We'll check the reservation details, booking terms, and relevant hotel policy before giving the next update."
        )
    },

    "flight_issue": {
        "description": "Flight bookings, airline cancellations, airline refunds, carriers, or flight Miles.",
        "keywords": [
            "flight", "airline", "united", "delta", "carrier", "plane",
            "ticket", "airport"
        ],
        "canned_response": (
            "Thanks for reaching out. I can help review your flight-related issue. "
            "We'll check the booking details and airline status before confirming next steps."
        )
    }
}


def classify_ticket(ticket):
    ticket_lower = ticket.lower()
    scores = {}

    for category, info in SOP_CATEGORIES.items():
        score = 0

        for keyword in info["keywords"]:
            if keyword in ticket_lower:
                score += 1

        scores[category] = score

    best_category = max(scores, key=scores.get)
    best_score = scores[best_category]

    if best_score == 0:
        return {
            "category": "unclear_or_needs_review",
            "confidence": "low",
            "needs_agent_review": True,
            "reason": "No strong category keywords matched."
        }

    if best_score >= 3:
        confidence = "high"
        needs_agent_review = False
    elif best_score == 2:
        confidence = "medium"
        needs_agent_review = False
    else:
        confidence = "low"
        needs_agent_review = True

    return {
        "category": best_category,
        "confidence": confidence,
        "needs_agent_review": needs_agent_review,
        "reason": f"Matched {best_score} keyword(s) for {best_category}."
    }


def match_sop(ticket):
    classification = classify_ticket(ticket)
    retrieved_chunks = retrieve_chunks(ticket, top_n=3)

    category = classification["category"]

    if category == "unclear_or_needs_review":
        canned_response = (
            "I'm not fully sure which SOP applies. Please review this ticket manually "
            "or escalate to a senior agent."
        )
    else:
        canned_response = SOP_CATEGORIES[category]["canned_response"]

    return {
        "ticket": ticket,
        "category": category,
        "confidence": classification["confidence"],
        "needs_agent_review": classification["needs_agent_review"],
        "reason": classification["reason"],
        "canned_response": canned_response,
        "matched_sources": [chunk["source"] for chunk in retrieved_chunks]
    }


def print_match(result):
    print("\n" + "=" * 60)
    print("SOP MATCH RESULT")
    print("=" * 60)
    print(f"Category: {result['category']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Needs agent review: {result['needs_agent_review']}")
    print(f"Reason: {result['reason']}")

    print("\nCanned response:")
    print(result["canned_response"])

    print("\nMatched sources:")
    if result["matched_sources"]:
        for source in result["matched_sources"]:
            print(f"- {source}")
    else:
        print("No matching sources found.")

    print("=" * 60)


# ---------------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------------

st.title("SOP Match")
st.write("Paste a support ticket below to find the matching SOP category and canned response.")

ticket_input = st.text_area("Ticket text", height=150)

if st.button("Match SOP"):
    if ticket_input.strip():
        result = match_sop(ticket_input)

        st.subheader("Result")
        st.write(f"**Category:** {result['category']}")
        st.write(f"**Confidence:** {result['confidence']}")
        st.write(f"**Needs agent review:** {result['needs_agent_review']}")
        st.write(f"**Reason:** {result['reason']}")

        st.subheader("Canned response")
        st.write(result["canned_response"])

        st.subheader("Matched sources")
        if result["matched_sources"]:
            for source in result["matched_sources"]:
                st.write(f"- {source}")
        else:
            st.write("No matching sources found.")
    else:
        st.warning("Please enter a ticket first.")
