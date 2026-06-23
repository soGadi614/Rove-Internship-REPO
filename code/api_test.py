# api_test.py
# --------------------------------------------------
# DAY 2: Test your OpenAI API connection
# Run this first to confirm everything is working.
# --------------------------------------------------

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_connection():
    print("Testing OpenAI API connection...")
    print("=" * 50)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Say 'Rove co-pilot connected!' and nothing else."}
        ]
    )

    print(response.choices[0].message.content)
    print("=" * 50)
    print("✅ Connection successful! You're ready to build.")

def test_with_and_without_context():
    """
    Day 2 exercise: compare answers with vs without Rove context.
    This shows exactly why RAG matters.
    """
    ticket = "My miles didn't show up after my hotel booking 3 days ago."

    rove_doc = """
    Source: Rove Help Center - Missing Miles Policy
    Rove miles are credited within 72 hours of a completed booking. 
    If miles are missing after 72 hours, the customer should contact 
    support and provide their booking ID and the date of the transaction. 
    The support team will investigate and credit any missing miles within 
    3 business days.
    """

    print("\n--- WITHOUT context (just AI general knowledge) ---")
    response_without = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"A customer says: {ticket}\nDraft a helpful support reply."}
        ]
    )
    print(response_without.choices[0].message.content)

    print("\n--- WITH Rove context (grounded answer) ---")
    response_with = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"""A customer says: {ticket}

Here is the relevant Rove documentation:
{rove_doc}

Answer using ONLY this documentation. Name the source. 
If the answer isn't here, say so."""}
        ]
    )
    print(response_with.choices[0].message.content)
    print("\n✅ Notice how much better the grounded answer is!")

if __name__ == "__main__":
    test_connection()
    test_with_and_without_context()
