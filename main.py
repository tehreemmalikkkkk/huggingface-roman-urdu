import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Function to load the model (remove caching temporarily for debugging)
def load_model():
    model_name = "Helsinki-NLP/opus-mt-en-ur"  # Replace with the correct model name or path
    try:
        # Load the pre-trained model and tokenizer
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        translator = pipeline("translation", model=model, tokenizer=tokenizer)
        return translator
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load the translation model
translator = load_model()

# Streamlit app layout
st.title("English to Roman Urdu Translator")

# Input field for the English prompt
input_text = st.text_area("Enter English text to translate:", height=100)

# Button to trigger translation
if st.button("Translate"):
    if input_text and translator is not None:
        try:
            # Translate English text to Roman Urdu
            translation = translator(input_text)
            roman_urdu_text = translation[0]['translation_text']
            st.subheader("Roman Urdu Translation:")
            st.write(roman_urdu_text)
        except Exception as e:
            st.error(f"Translation error: {e}")
    elif translator is None:
        st.error("The model could not be loaded. Please check the model name.")
    else:
        st.error("Please enter some text to translate.")
