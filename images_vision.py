# Input image -> Ask OpenAI to describe the Image, or summarize the image etc
# Input image of frontend -> Ask OpenAI to review the fronted from user's perspective.

# Input=Image & Output=Text
# responses API

import base64
from openai import OpenAI

client = OpenAI()

def encoded_image(image_path):
    """ Converts the image from the given path into base64 encoded string."""

    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode("UTF-8")

image_path = "output_images/playing_cat.png"
base64_image = encoded_image(image_path)

result = client.responses.create(
    model="gpt-5.2",
    input=[
        {
            "role" : "user",
            "content" : [
                {
                    "type" : "input_text",
                    "text" : """
                        Please analyze the input image and 
                        tell what the image is all about, 
                        also give some suggestions to improve the image.
                        """
                },
                {
                    "type" : "input_image",
                    "image_url" : f"data:image/png;base64, {base64_image}"
                }
            ]
        }
    ]
)

print(result.output_text)