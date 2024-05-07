from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_resonse(input,image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0],prompt])
    return response.text


def input_image_setup(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()
        image_parts = [{
            "mime_type": upload_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
         raise FileNotFoundError("No file uploaded")
     

def main():

    st.title("🔎 Tell Me About this Car")
    """
    Please give me an image, which has a `car` in it, and I will tell you more information about it.
    """
    upload_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
    image = ""
    if upload_file is not None:
        image = Image.open(upload_file)
        st.image(image, caption="uploaded image.", use_column_width=True)
        
    submit = st.button("tell me about the invoice")
    
    input_prompt = """You are an expert in understanding Automobiles
    You will receive input images of cars
    you will have to identify what is the car in the image and provid basic information about it
    
    
    ###RESPONSE###
    Brand : Kia
    Car : Seltos
    Color : White
    Mileage : 15 KmpL
    Top Speed : 200 KmpH
    First release year : 2014
    Found : Kim Cheol-Ho
    Market Share in India : 6.2%
    """
    
    if submit:
        image_data = input_image_setup(upload_file=upload_file)
    response= get_gemini_resonse(input_prompt,image_data,input)
    st.subheader("The response is")
    st.write(response)

if __name__ == "__main__":
    main()

