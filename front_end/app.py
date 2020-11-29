import streamlit as st
import requests
url = "http://api:8080/predict_entity"


st.title('Named Entity Recognition App')

txt=st.text_area('Please input words or a sentence that you want to be analyzed for NER ')

clicked=st.button('Process', key=None)
if clicked:
    payload="{\"text\":\""+txt+"\",\"model\":\"spacy\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    st.write(response.text)


