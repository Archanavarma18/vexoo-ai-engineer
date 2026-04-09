
import math
from collections import Counter

# Create overlapping text chunks
def sliding_window(text, window_size=200, overlap=50):
    chunks = []
    step = window_size - overlap
    for i in range(0, len(text), step):
        chunk = text[i:i + window_size]
        if chunk:
            chunks.append(chunk)
    return chunks
# Generate short summary for each chunk
def summarize(chunk):
    return chunk[:75] + "..." if len(chunk) > 75 else chunk
# Basic keyword-based classification
def classify(chunk):
    chunk_lower = chunk.lower()
    if "ai" in chunk_lower or "machine learning" in chunk_lower:
        return "Technology"
    elif "finance" in chunk_lower:
        return "Finance"
    elif "health" in chunk_lower:
        return "Healthcare"
    else:
        return "General"

# Extract simple keyword set

def extract_keywords(chunk):
    words = chunk.lower().split()
    return list(set(words[:10]))


# Build multi-level knowledge representation
def build_knowledge_pyramid(text):
    chunks = sliding_window(text)
    pyramid = []

    for chunk in chunks:
        entry = {
            "raw_text": chunk,
            "summary": summarize(chunk),
            "category": classify(chunk),
            "keywords": extract_keywords(chunk)
        }
        pyramid.append(entry)

    return pyramid


# Compute cosine similarity between two texts
def cosine_similarity(text1, text2):
    vec1 = Counter(text1.lower().split())
    vec2 = Counter(text2.lower().split())

    intersection = set(vec1.keys()) & set(vec2.keys())
    dot_product = sum([vec1[x] * vec2[x] for x in intersection])

    magnitude1 = math.sqrt(sum([v**2 for v in vec1.values()]))
    magnitude2 = math.sqrt(sum([v**2 for v in vec2.values()]))

    if not magnitude1 or not magnitude2:
        return 0

    return dot_product / (magnitude1 * magnitude2)

# Find best matching content for query

def query_pyramid(pyramid, query):
    best_match = None
    best_score = 0
    best_level = None

    for entry in pyramid:
        # Check all pyramid levels
        levels = {
            "raw_text": entry["raw_text"],
            "summary": entry["summary"],
            "category": entry["category"],
            "keywords": " ".join(entry["keywords"])
        }

        for level_name, content in levels.items():
            score = cosine_similarity(query, content)
            if score > best_score:
                best_score = score
                best_match = content
                best_level = level_name

    return best_level, best_match, best_score


# Demo execution
if __name__ == "__main__":
    sample_text = """
    Artificial Intelligence is transforming industries across the world.
    AI is widely used in healthcare for diagnosis and treatment planning.
    In finance, AI helps in fraud detection and risk analysis.
    Machine learning models are improving automation and efficiency.
    """

    print("🔹 Building Knowledge Pyramid...")
    pyramid = build_knowledge_pyramid(sample_text)

    print("🔹 Pyramid Size:", len(pyramid))

    query = "AI in healthcare"
    print("\n🔹 Running Query:", query)

    level, result, score = query_pyramid(pyramid, query)

    print("\n Best Match Level:", level)
    print(" Result:", result)

       

    
               
