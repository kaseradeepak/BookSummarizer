from pathlib import Path

def read_text_from_file(file_path: str) -> str:
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        return file.read()