import streamlit as st
import requests
url = "http://api:8080/predict_entity" #change to api host when using docker compose


st.title('Named Entity Recognition App')

txt=st.text_area('Please input words or a sentence that you want to be analyzed for NER ')
option = st.selectbox('Which NLP Framework would you like to use?',('spaCy', 'Stanza'))
clicked=st.button('Process', key=None)
option=option.lower()

if clicked:
    payload="{\"text\":\""+txt+"\",\"model\":\""+option+"\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    st.write(response.text)


