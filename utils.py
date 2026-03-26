from pathlib import Path

# Chunking logic
# chunk_size = 1000
def chunk_text(text: str, chunk_size: int = 1000) -> list[str]:
    words = text.split(' ') # list of words from the text.
    chunks = []
    
    i = 0
    while i < len(words):
        chunk = words[i : i + chunk_size - 1]
        chunks.append(chunk)
        i = i + chunk_size
    
    return chunks


def read_text_from_file(file_path: str) -> str:
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        return file.read()


# 18 words
# chunk_size = 5
# chunks = ["Give models access to new", "functionality and data they can", "", ""]

# i = 5
# Give models access to new functionality and data they can use to follow instructions and respond to prompts.

# chunk = "Give models access to new"