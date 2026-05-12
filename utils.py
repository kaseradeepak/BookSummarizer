from pathlib import Path
import base64

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

def save_base64_image(base64_data: str, output_path: str):
    """
    Converts a base64 image string into an actual image file.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    image_bytes = base64.b64decode(base64_data)

    with open(output_path, "wb") as file:
        file.write(image_bytes)

    print(f"Image saved successfully at: {output_path}")


# 18 words
# chunk_size = 5
# chunks = ["Give models access to new", "functionality and data they can", "", ""]

# i = 5
# Give models access to new functionality and data they can use to follow instructions and respond to prompts.

# chunk = "Give models access to new"