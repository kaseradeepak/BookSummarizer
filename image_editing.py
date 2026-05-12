from openai import OpenAI
from utils import save_base64_image

client = OpenAI()

prompt = "Please edit the image and change dog into cat."

result = client.images.edit(
    model="gpt-image-2",
    image=open("output_images/playing_dog.png", "rb"),
    prompt=prompt,
    size="1024x1024",
    quality="medium"
)

image_base64 = result.data[0].b64_json

save_base64_image(
    image_base64,
    "output_images/playing_cat.png"
)