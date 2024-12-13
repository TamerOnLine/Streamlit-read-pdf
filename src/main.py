import os
import streamlit as st
from PyPDF2 import PdfReader

st.title("PDF Summarization with AI")


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file.
    """
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# File upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Text variable for later use
text = ""

if uploaded_file is not None:
    # Ensure the temp directory exists
    os.makedirs("temp", exist_ok=True)

    # Save the uploaded file
    file_path = f"temp/{uploaded_file.name}"
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())
    st.write("File uploaded successfully.")

    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(file_path)

    # Display the extracted text
    st.write("Extracted Text:")
    st.write(text)
else:
    st.write("Please upload a PDF file.")
