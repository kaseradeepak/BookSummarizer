from sentence_transformers import SentenceTransformer

# Step 1: Load the pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Input sentences
sentences = [
    "I love learning machine learning",
    "AI is transforming the world",
    "Cricket is a very popular sport in India"
]

# Step 3: Generate embeddings
embeddings = model.encode(sentences)

# Step 4: Print embeddings
for i in range(len(sentences)):
    print("Sentence:", sentences[i])
    print("Embedding:", embeddings[i])
    print("Embedding length:", len(embeddings[i]))
    print()

# Step 5: Print overall shape
print("Total embeddings shape:", embeddings.shape)