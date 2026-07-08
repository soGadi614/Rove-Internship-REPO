# Rove Support Co-pilot

A Streamlit tool that helps Rove agents handle tickets faster. Paste in a customer ticket and it gives you back a suggested reply (editable), the matched SOP, and a refund calculation if one applies — plus the source doc behind every suggestion so you can double check it before sending anything.

## HOW TO RUN THE COPILOT - SETUP
1. Click on the green "Code" dropdown
2. Add a new codespace & click on it
3. Run these commands in the Codespace terminal:
pip install -r requirements.txt
#Add a .env file in the repo root with:
OPENAI_API_KEY=your-key-here
#Then:
python3 -m streamlit run app.py
-----------------------------------
Open the forwarded URL from the Ports tab. Three pages in the sidebar:
- Combined Copilot — the main thing, runs all three helpers together
- Refund Calculator — just the refund math
- SOP Match — SOP matching

## How well it works

Tested against 9 sample tickets (shopping/dining, flight refunds, retail, hotel complaints, referrals, login, cancellations, Miles timing).

SOP matching: 9/9 correct, including appropriately flagging a low-confidence retail ticket for agent review, matching what the real agent also had to do.

| Ticket | Relevant Sources Retrieved | Answer Quality |
|--------|---------------------------|----------------|
| Member used promo code at The Pasta House, missing Rove Miles | No sources retrieved — ticket wording ("promo code," "$84 last Tuesday") doesn't overlap enough with SOP vocabulary | SOP match correct, but no grounding sources shown to agent |
| United Airlines canceled flight, member wants refund | Payment & Refund FAQ, Flight Cancellation by Airline Workflow, Refundable Hotel Cancellation Workflow | Correct — follows airline cancellation SOP, appropriately avoids promising a dollar amount before Duffel confirms |
| Nike promised 5.2x Miles, member only got 2.6x | Sources off-topic (Atlas & Inbox Procedures, Support Contacts) | Correctly flagged as low-confidence / needs agent review, matching what the real agent also had to escalate |
| Hotel stay missing towels and outlets, member wants compensation | Hotel Complaint Response Template, Hotel Complaint Compensation Policy | Correct — matches SOP that hotel issues are the hotel's responsibility, not Rove's |
| Referral Miles never posted after friend signed up | Referral Miles Policy, Rove Miles Overview & Quick Reference | Correct — asks for referral link, referred member's name, and contact info, matching SOP |
| Member not receiving verification code to log in | Verification Requirements & Principles, Verification Level 3, Login Assistance & OTP Troubleshooting | Correct — walks through logout/login/new-code steps, all three sources on point |
| Member wants to cancel a refundable hotel reservation | Refundable Hotel Cancellation Workflow, Non-Refundable Modification Procedure | Fixed — was misclassified as a hotel complaint, now correctly identified as a standard refund after prompt fix |
| Member asking when Adidas shopping Miles will be available | Shopping Miles Timeline relevant; two other sources off-topic | Correct — explains pending window and 30-100 day posting timeline |
| Hotel Miles not posted after a refundable stay | Hotel Miles Earning Policy relevant; one source off-topic | Correct — refund calculator appropriately flagged "insufficient information" rather than guessing, since this wasn't a refund question |

## Bugs found and fixed

Refund misclassification: a ticket about canceling a refundable hotel booking was getting misread as a complaint instead of a normal cancellation, triggering the wrong refund path entirely. Fixed by adding a clarifying rule to the extraction prompt. Confirmed before/after with the same ticket — refund type changed from "hotel_complaint" to "standard."

Dollar amount extraction: only worked if the ticket said "refund amount" specifically. "Booking cost" returned $0. Fixed by broadening what phrasing the extraction prompt recognizes. Confirmed the same ticket phrased as "booking cost was $350" now correctly extracts $350.00.

## What's still weak

Retrieval is keyword-based, not true semantic search. It works well when the customer's wording overlaps with SOP language, but can miss sources entirely when the wording is very different (e.g. "promo code" vs. "coupon," "compensation" vs. "goodwill miles"). We tried a few weighting approaches and got partial improvement, but fully solving this would need embedding-based semantic search, which is a good next step beyond this week.

Dollar-amount extraction is only as good as how closely the ticket phrasing matches what we've tested. Agents should still check the extracted number against the actual booking before processing a refund.
