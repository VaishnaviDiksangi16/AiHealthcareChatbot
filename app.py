import streamlit as st 
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punk')
nltk.download('stopword')

chatboat=pipeline("text-generation",model='distilgpt2')

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult doctor for accurate advice"
    elif "appointment"in user_input:
        return "Would you like to schedule with the Doctor"
    elif "Medication"in user_input:
        return"It is important to take medicians regurlely."    

    else:
        response=chatboat(user_input,max_length=500,num_return_sequences=1)
        return response[0]['generated_text']


def main():
    st.title("Healthcare Assistant Chatboat")
    user_input=st.text_input("How can I assist you today ?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query..."):

                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ", response)
            print(response)
        else:
            st.write("Plese enter the message to get the response.")    

main()    