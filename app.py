from openai import OpenAI
from utils import read_text_from_file, chunk_text

client = OpenAI()

# Learn how to learn

book_text = read_text_from_file('/Users/deepakkasera/book-summarizer/book.txt')

# Create chunks from the book_text.
chunks = chunk_text(book_text, 50)

print(f"Number of chunks: {len(chunks)}")

for chunk in chunks:
    chunk_summary = client.responses.create(
        model = "gpt-5.4",
        input = f"Summarize this text: {chunk}"
    )

    print(chunk_summary.output_text, end="==============")


# response = client.responses.create(
#     model = "gpt-5.4",
#     input = f"Summarize this book in simple words to a 10 year old kid: {book_text}"
# )

# print(response.output_text)
