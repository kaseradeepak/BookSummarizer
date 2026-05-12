# Text to Image Generation
from openai import OpenAI
import base64
from pathlib import Path
from utils import save_base64_image

client = OpenAI()

# prompt for image generation
# prompt = "Please generate an image of a dog playing with a ball in a Park."
prompt = """
Create a professional poster for a Backend Engineering Bootcamp.

Theme:
- Java
- Spring Boot
- Databases
- System Design
- Clean architecture

Style:
- Modern tech poster
- Dark premium background
- Clean typography
- Minimal clutter
- Suitable for LinkedIn and YouTube thumbnail

Text on image:
"Backend Engineering Bootcamp"
"Java • Spring Boot • Databases • System Design"
"""

def save_base64_image(base64_data: str, output_path: str):
    """
    Converts a base64 image string into an actual image file.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    image_bytes = base64.b64decode(base64_data)

    with open(output_path, "wb") as file:
        file.write(image_bytes)

    print(f"Image saved successfully at: {output_path}")

# Call OpenAI images API for image generation.
result = client.images.generate(
    model="gpt-image-1.5",
    prompt=prompt,
    quality="medium",
    size="1024x1024"
)

image_base64_encoded_string = result.data[0].b64_json

# OpenAI return image in base64 encoded string -> Decode base64 string into bytes -> Save these bytes in the form of image (.png / .jpg / .jpeg) 

save_base64_image(
    image_base64_encoded_string,
    "output_images/poster.png"
)

# Prompt Techniques