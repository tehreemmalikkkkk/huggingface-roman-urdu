import streamlit as st
from transformers import pipeline

# Load the translation model
@st.cache_resource
def load_model():
    model_name = "HuggingFaceH4/roman-urdu"  # Updated model name
    translator = pipeline("translation", model=model_name)
    return translator

translator = load_model()

# Streamlit app layout
st.title("English to Roman Urdu Translator")
st.write("Enter your English text below:")

# User input
input_text = st.text_area("Input Text")

if st.button("Translate"):
    if input_text:
        # Perform translation
        translation = translator(input_text, target_lang="ur")  # Adjust if needed
        st.write("Translated Text:")
        st.write(translation[0]['translation_text'])  # Display translated text
    else:
        st.error("Please enter some text to translate.")

# Run the app using the command below
# streamlit run app.py
