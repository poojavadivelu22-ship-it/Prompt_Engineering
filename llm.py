
import os
from google import genai


def generate_response(prompt, temperature=0.2, max_tokens=500):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise Exception("GEMINI_API_KEY is not set.")

    client = genai.Client(
        api_key=api_key
    )

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text

