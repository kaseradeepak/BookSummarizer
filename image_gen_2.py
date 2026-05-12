# Generating multiple image variations.
# Sometimes one generated image is not enough.
# For more creativity or options, we can ask OpenAI for multiple images generation.

# prompt = "generate 4 logo options for ----------"

prompt = """
Create an original logo for a YouTube channel called "Masai School".

Brand meaning:
- Algorithms
- System Design
- Backend Engineering
- Distributed Systems

Style:
- Premium tech brand
- Simple geometric symbol
- Clean typography
- Dark background
- Suitable for YouTube, LinkedIn, and website branding

Constraints:
- No copied brand elements
- No complex illustration
- Logo should be readable at small size
"""

from openai import OpenAI
import base64
from pathlib import Path
from utils import save_base64_image

client = OpenAI()

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1024",
    quality="high",
    n=4
)

for index, item in enumerate(result.data, start=1):
    save_base64_image(
        item.b64_json,
        f"output_images/masai_logo_option_{index}.png"
    )



