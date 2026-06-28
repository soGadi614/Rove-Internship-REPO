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

- `retrieval.py`  
  Finds the most relevant SOP chunks for a ticket using keyword matching.

- `rag_loop.py`  
  Uses retrieval plus an AI model to draft a grounded suggested answer.

- `sop_match.py`  
  Classifies the ticket type and prepares a matching canned SOP response.

- `refund_calculator.py`  
  Extracts refund details with AI, then does refund math in Python.

- `combined_copilot.py`  
  Runs the suggested answer helper, SOP matcher, and refund calculator together.

- `api_test.py`  
  Tests whether the OpenAI API key is working.

## Setup

Install required packages:

```bash
pip install openai python-dotenv
