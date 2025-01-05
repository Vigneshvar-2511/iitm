import streamlit as st
from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import StringIO

# Load Hugging Face pipelines
qa_pipeline = pipeline("question-answering")
summarizer = pipeline("summarization")

# Function to summarize text
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function for question answering
def ask_question(text, question):
    response = qa_pipeline(question=question, context=text)
    return response['answer']

# Function to generate word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)

# Streamlit app
st.title("ESG Report Insights Extractor")
st.write("Upload an ESG report to extract key insights and visualize information.")

uploaded_file = st.file_uploader("Upload a document (TXT format)", type="txt")
if uploaded_file is not None:
    # Read the uploaded file
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    document_text = stringio.read()
    
    st.subheader("Uploaded Document")
    st.write(document_text)
    
    # Summarize the document
    st.subheader("Summary of the Document")
    summary = summarize_text(document_text)
    st.write(summary)
    
    # Extract insights via Question Answering
    st.subheader("Key Insights (Question-Answering)")
    sample_questions = [
        "What is the main purpose of this project?",
        "What are the expected outcomes?",
        "Who are the key stakeholders?"
    ]
    for question in sample_questions:
        answer = ask_question(document_text, question)
        st.write(f"**Q:** {question}")
        st.write(f"**A:** {answer}")
    
    # Generate and display word cloud
    st.subheader("Word Cloud of the Document")
    generate_wordcloud(document_text)
