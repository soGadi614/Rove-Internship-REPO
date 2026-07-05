# Rove Support Co-Pilot

This project is a prototype AI co-pilot for Rove customer support agents. It helps an agent review a customer ticket by finding relevant SOP information, drafting a grounded suggested answer, matching the ticket to the right SOP category, and calculating refunds when relevant.

## What The Co-Pilot Does

For a support ticket, the co-pilot returns:

- A suggested answer grounded in Rove documentation
- The sources used for the answer
- The matched SOP category
- A canned response the agent can personalize
- A confidence flag for the SOP match
- A refund calculation if the ticket involves refunds or cancellations

The tool is meant to support a human agent, not replace one.

## Files

- `knowledge/knowledge_base.py`  
  Holds the sourced Rove SOP chunks as `rove_chunks`.

- `code/retrieval.py`  
  Finds the most relevant SOP chunks for a ticket using keyword matching.

- `code/rag_loop.py`  
  Uses retrieval plus an AI model to draft a grounded suggested answer.

- `code/sop_match.py`  
  Classifies the ticket type and prepares a matching canned SOP response.

- `code/refund_calculator.py`  
  Extracts refund details with AI, then does refund math in Python.

- `code/combined_copilot.py`  
  Runs the suggested answer helper, SOP matcher, and refund calculator together.

- `code/api_test.py`  
  Tests whether the OpenAI API key is working.

## Setup

**1. Install required packages:**

```bash
pip install openai python-dotenv
```

**2. Add your OpenAI API key:**

Create a `.env` file in the root of the repo:

```
OPENAI_API_KEY=your-key-here
```

**3. Run the co-pilot:**

```bash
python3 code/rag_loop.py
```

Or run the full combined copilot:

```bash
python3 code/combined_copilot.py
```

## How to Run (End-to-End)

1. Clone the repo
2. Run `pip install openai python-dotenv`
3. Create a `.env` file with your `OPENAI_API_KEY`
4. Run `python3 code/rag_loop.py`
5. The co-pilot will process each ticket in `test_tickets` and print a draft reply with cited sources

## Accuracy Results (v1)

Tested on 4 real Rove support tickets:

| Ticket | Relevant Sources Retrieved | Answer Quality |
|--------|---------------------------|----------------|
| Member used promo code at The Pasta House, missing Rove Miles | ✅ Ticket Management, Refund Eligibility | ✅ Correct — asks for booking ID to verify |
| United Airlines canceled flight, member wants refund | ✅ Flight Cancellation by Airline Workflow | ✅ Correct — follows airline cancellation SOP |
| Member not receiving verification code to log in | ✅ Verification Requirements & Level 3 | ✅ Correct — requests email verification with details |
| Member asking when Adidas shopping Miles will be available | ✅ Shopping Miles Timeline | ✅ Correct — explains 24hr–10 day pending window |

**Overall: 4/4 tickets answered correctly and grounded in Rove documentation.**

All answers cited their source document. No hallucinations observed in v1 testing.

## Before & After

**Before (Week 1):** Agents had to manually search through SOP documents to find the right procedure for each ticket. No AI assistance, no draft replies, no source citations.

**After (v1):** The co-pilot automatically retrieves the most relevant SOP chunks, drafts a professional reply, and cites the exact source — in seconds. Agents review and send rather than starting from scratch.
