from openai import OpenAI

client = OpenAI()

response = client.embeddings.create(
    input="Python is the most widely used programming language for ML.",
    model="text-embedding-3-small"
)

embeddings = response.data[0].embedding

print(len(embeddings))