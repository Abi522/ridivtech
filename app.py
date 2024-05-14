

# Function to extract text from PDF

import streamlit as st
import openai
import PyPDF2
import io

# Set OpenAI API key
openai.api_key = #  sk-proj-jEaqt0jDMoplNo57GCGBT3BlbkFJDsJzrntb2OArN5cU1sIB  #I have hidded the api key

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    raw_text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    num_pages = len(pdf_reader.pages)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        raw_text += page.extract_text()

    return raw_text

# Function to interact with OpenAI API and generate response
def generate_response(user_input, pdf_text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", # Using GPT-2 engine
  # Update to a supported model
        prompt=pdf_text + "\nUser: " + user_input + "\nAI:",
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main function to run the app
def main():
    st.title("PDF Chatbot")

    # File upload section
    st.header("Upload a PDF File")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Display uploaded PDF
        st.subheader("Uploaded PDF Preview")
        pdf_bytes = uploaded_file.read()
        pdf_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))
        st.write(pdf_text)

        # Chat interface
        st.header("Chat with the PDF")
        user_input = st.text_input("Enter your message")
        if st.button("Send"):
            # Perform chatbot processing and display response
            if user_input.strip() != "":
                bot_response = generate_response(user_input, pdf_text)
                st.write("Chatbot Response:")
                st.write(bot_response)

# Run the app
if __name__ == "__main__":
    main()
