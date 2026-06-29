# retrieval.py
# --------------------------------------------------
# DAY 4: Retrieval — find the right chunks for a ticket
# --------------------------------------------------

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from knowledge.knowledge_base import rove_chunks

# Words to ignore when matching — too common to be useful
STOP_WORDS = {
    "i", "my", "the", "a", "an", "and", "or", "to", "in", "is",
    "it", "of", "for", "on", "with", "this", "that", "was", "are",
    "have", "has", "not", "be", "do", "did", "can", "will", "we",
    "you", "me", "he", "she", "they", "up", "at", "but", "so",
    "just", "still", "about", "after", "been", "from", "when",
    "what", "how", "there", "its", "their", "our", "your", "his"
}

def get_keywords(text):
    """Extract meaningful words from text, ignoring stop words."""
    words = text.lower().split()
    # Remove punctuation and stop words
    cleaned = []
    for word in words:
        word = word.strip(".,!?\"'():;")
        if word and word not in STOP_WORDS and len(word) > 2:
            cleaned.append(word)
    return set(cleaned)

def retrieve_chunks(ticket, kb=rove_chunks, top_n=3):
    """
    Find the most relevant chunks for a given ticket.
    Uses keyword matching — counts shared meaningful words.
    Returns top_n chunks with their source labels.
    """
    ticket_keywords = get_keywords(ticket)

    scored_chunks = []
    for chunk in kb:
        chunk_keywords = get_keywords(chunk["text"])
        overlap = len(ticket_keywords & chunk_keywords)
        scored_chunks.append((overlap, chunk))

    # Sort by overlap score, highest first
    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    # Return top N chunks (skip any with 0 overlap)
    top_chunks = [chunk for score, chunk in scored_chunks[:top_n] if score > 0]

    return top_chunks

def print_retrieved(ticket, chunks):
    """Helper to print retrieved chunks clearly for debugging."""
    print(f"\nTICKET: {ticket}")
    print("-" * 60)
    if not chunks:
        print("⚠️  No matching chunks found.")
    for i, chunk in enumerate(chunks, 1):
        print(f"[Chunk {i}] Source: {chunk['source']}")
        print(f"  {chunk['text'][:120]}...")
    print("-" * 60)

# --------------------------------------------------
# TEST IT — run this file directly to check retrieval
# --------------------------------------------------
if __name__ == "__main__":
    test_tickets = [
        "My miles didn't show up after my hotel booking 3 days ago",
        "I want to cancel my reservation, how do I do it?",
        "I was charged twice for my booking and want a refund",
        "Can I transfer my miles to a friend?",  # Should return nothing or weak match
    ]

    print("=" * 60)
    print("RETRIEVAL TEST — checking which chunks are found")
    print("=" * 60)

    for ticket in test_tickets:
        chunks = retrieve_chunks(ticket)
        print_retrieved(ticket, chunks)

    print("\n✅ Review the chunks above — do they match the right tickets?")
    print("If not, go back and clean your knowledge base chunks.")
