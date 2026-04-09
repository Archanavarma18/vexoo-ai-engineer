import re
from collections import Counter

class SlidingWindow:
    def __init__(self, window_size=500, overlap=100):
        self.window_size = window_size
        self.overlap = overlap

    def split(self, text):
        chunks = []
        step = self.window_size - self.overlap
        for i in range(0, len(text), step):
            chunks.append(text[i:i+self.window_size])
        return chunks


class KnowledgePyramid:
    def __init__(self):
        self.entries = []

    def summarize(self, chunk):
        sentences = re.split(r'[.!?]', chunk)
        return '. '.join(sentences[:2]).strip()

    def categorize(self, chunk):
        text = chunk.lower()
        if "math" in text:
            return "Mathematics"
        elif "ai" in text:
            return "AI/ML"
        elif "law" in text:
            return "Legal"
        return "General"

    def distill(self, chunk):
        words = re.findall(r'\w+', chunk.lower())
        common = Counter(words).most_common(5)
        return [w for w, _ in common]

    def build(self, chunks):
        for chunk in chunks:
            self.entries.append({
                "raw": chunk,
                "summary": self.summarize(chunk),
                "category": self.categorize(chunk),
                "distilled": self.distill(chunk)
            })


class QueryEngine:
    def similarity(self, a, b):
        set_a = set(a.split())
        set_b = set(b.split())
        return len(set_a & set_b) / (len(set_a | set_b) + 1e-5)

    def search(self, query, entries):
        best_score = 0
        best_result = None

        for entry in entries:
            for key in ["raw", "summary", "category"]:
                score = self.similarity(query.lower(), str(entry[key]).lower())
                if score > best_score:
                    best_score = score
                    best_result = (key, entry[key])

            score = self.similarity(query.lower(), " ".join(entry["distilled"]))
            if score > best_score:
                best_score = score
                best_result = ("distilled", entry["distilled"])

        return best_result


if __name__ == "__main__":
    text = """Artificial Intelligence is transforming industries. 
    Machine learning is a subset of AI. Mathematics plays a key role in AI systems."""

    sw = SlidingWindow()
    chunks = sw.split(text)

    kp = KnowledgePyramid()
    kp.build(chunks)

    qe = QueryEngine()
    result = qe.search("What is AI?")

    print("Query Result:", result)
