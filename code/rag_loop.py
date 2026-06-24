# rag_loop.py
# --------------------------------------------------
# DAY 5: The full RAG loop — ticket in, answer out
# This is the heart of the Rove co-pilot.
# --------------------------------------------------

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from dotenv import load_dotenv
from openai import OpenAI
from retrieval import retrieve_chunks
from knowledge.knowledge_base import knowledge_base

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------------------------------------
# STEP 1: Build the grounded prompt
# --------------------------------------------------
def build_prompt(ticket, retrieved_chunks):
    """
    Combine the ticket + retrieved Rove docs into a grounded prompt.
    The key instruction: answer ONLY from the provided docs, name the source,
    admit the gap if the answer isn't there.
    """
    if not retrieved_chunks:
        context = "No relevant documents were found in the knowledge base."
    else:
        context = ""
        for chunk in retrieved_chunks:
            context += f"Source: {chunk['source']}\n{chunk['text']}\n\n"

    prompt = f"""You are an AI assistant helping a Rove customer support agent draft replies.

CUSTOMER TICKET:
{ticket}

RELEVANT ROVE DOCUMENTATION:
{context}

INSTRUCTIONS:
- Answer using ONLY the information in the documentation above.
- Always state which source document your answer comes from.
- If the answer is not in the provided documentation, respond with:
  "I couldn't find this in Rove's documentation. Please escalate to a senior agent."
- Keep your tone helpful, friendly, and professional.
- Write the reply as a draft for the agent to review — not a final send.

DRAFT REPLY:"""

    return prompt

# --------------------------------------------------
# STEP 2: Call the AI
# --------------------------------------------------
def call_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3  # Lower = more consistent, less creative
    )
    return response.choices[0].message.content

# --------------------------------------------------
# STEP 3: The full RAG loop
# --------------------------------------------------
def rag_loop(ticket):
    """
    The full pipeline:
    ticket → retrieve chunks → build prompt → AI answer → return with sources
    """
    print(f"\n{'='*60}")
    print(f"TICKET: {ticket}")
    print('='*60)

    # Retrieve relevant chunks
    retrieved = retrieve_chunks(ticket, knowledge_base, top_n=3)

    # Show which sources were retrieved (for debugging/Week 4 interface)
    if retrieved:
        sources = [chunk['source'] for chunk in retrieved]
        print(f"📚 Sources retrieved: {sources}")
    else:
        print("⚠️  No sources retrieved — AI will admit the gap")

    # Build the grounded prompt
    prompt = build_prompt(ticket, retrieved)

    # Get the AI's draft answer
    answer = call_ai(prompt)

    print(f"\n💬 DRAFT ANSWER:\n{answer}")
    print(f"\n📎 CITED SOURCES: {[c['source'] for c in retrieved] if retrieved else 'None'}")
    print('='*60)

    return {
        "ticket": ticket,
        "answer": answer,
        "sources": [c['source'] for c in retrieved]
    }
# Suggested Answer Helper
def suggest_answer(ticket):
    # Get the most relevant docs for the ticket
    retrieved = retrieve_chunks(ticket, knowledge_base, top_n=3)

    # If nothing matches, don't guess
    if not retrieved:
        return {
            "answer": "I couldn't find this in Rove's documentation. Please escalate to a senior agent.",
            "sources": []
        }

    # Build the prompt and generate a response
    prompt = build_prompt(ticket, retrieved)
    answer = call_ai(prompt)

    # Return the answer and the sources that were used
    return {
        "answer": answer,
        "sources": [chunk["source"] for chunk in retrieved]
    }
# --------------------------------------------------
# RUN TESTS — end-to-end on sample tickets
# --------------------------------------------------
if __name__ == "__main__":
    print("ROVE CO-PILOT — RAG LOOP TEST")
    print("Running sample tickets through the full pipeline...\n")

    test_tickets = [
        # These should be answered from the knowledge base
        "My miles didn't show up after my hotel booking 3 days ago. Booking ID is RV-48291.",
        "I cancelled my booking yesterday, it was booked 2 days ago. Will I get a full refund?",
        "How do I cancel my upcoming hotel reservation in the app?",
        "I was charged twice for my booking on March 15th. Booking ID RV-55102.",

        # This should NOT be found — co-pilot should admit the gap
        "Can I transfer my miles to my friend's account as a gift?",
    ]

    results = []
    for ticket in test_tickets:
        result = rag_loop(ticket)
        results.append(result)

    # Summary
    print(f"\n{'='*60}")
    print(f"✅ Ran {len(results)} tickets through the RAG loop.")
    print("Review the answers above:")
    print("  - Are they accurate and grounded in Rove docs?")
    print("  - Do they cite the right source?")
    print("  - Did the last ticket correctly admit the gap?")
    print(f"{'='*60}")
    print("\nNext step: Add your own knowledge base content and tickets.")
    print("Then build the 3 helpers in Week 3!")
