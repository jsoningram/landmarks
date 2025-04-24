import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv('GOOGLE_AI_API_KEY')

Image_Path = './images'


def generate_image_description(image_name):
    try:
        # Replace 'YOUR_API_KEY' with your actual API key
        genai.configure(api_key=api_key)

        # Select the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Load the image
        image = Image.open(f'{Image_Path}/{image_name}')

        # Send the image to the model with a prompt
        response = model.generate_content([
            'What is in this image? Provide a location.',
            image
        ])

        return response.text
    except Exception as e:
        print(f'An error occurred while processing {image_name}', e)
        return e
