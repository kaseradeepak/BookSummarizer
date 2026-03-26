from openai import OpenAI
from utils import read_text_from_file

client = OpenAI()

# Learn how to learn

book_text = read_text_from_file('/Users/deepakkasera/book-summarizer/book.txt')

response = client.responses.create(
    model = "gpt-5.4",
    input = f"Summarize this book in simple words to a 10 year old kid: {book_text}"
)

print(response.output_text)