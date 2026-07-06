# Rove Support Co-pilot

A Streamlit tool that helps Rove agents handle tickets faster. Paste in a customer ticket and it gives you back a suggested reply (editable), the matched SOP, and a refund calculation if one applies — plus the source doc behind every suggestion so you can double check it before sending anything.

## Running it

pip install -r requirements.txt

Add a .env file in the repo root with:
OPENAI_API_KEY=your-key-here

Then:
python3 -m streamlit run app.py

Open the forwarded URL from the Ports tab. Three pages in the sidebar:
- Combined Copilot — the main thing, runs all three helpers together
- Refund Calculator — just the refund math
- SOP Match — just SOP matching, no API key needed for this one

## How well it works

Tested against 9 sample tickets (shopping/dining, flight refunds, retail, hotel complaints, referrals, login, cancellations, Miles timing).

- SOP matching: 9/9 correct. Even got the tricky one right — flagged a Nike retail question as low-confidence/needs review, same as what the actual agent had to do.
- Source relevance: started rough, improved. Early on, sources were hit or miss (sometimes 0/3 relevant) because long knowledge base chunks stuffed with common words like "member" and "miles" were outscoring the actually-relevant ones. Fixed by reweighting keyword matches so rare/specific words (like "Wildfire" or "OTP") count more than generic ones.
- Refund calc: found and fixed two real bugs. One ticket about canceling a refundable hotel booking was getting misread as a complaint instead of a normal cancellation — wrong refund path entirely. Fixed by clarifying the prompt. Also found that dollar amounts only got extracted correctly if the ticket said "refund amount" specifically — "booking cost" returned $0. Fixed by broadening what phrasing counts.

## What's still weak

The dollar-amount extraction is only as good as how closely the ticket phrasing matches what we've tested — agents should still eyeball the number against the actual booking before processing anything. Source retrieval is keyword-based, not true semantic search, so a heavily paraphrased ticket might still miss the best doc.
