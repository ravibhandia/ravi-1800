import streamlit as st
import numpy as np
import pandas as pd
import requests
url = "http://127.0.0.1:8080/predict_entity"


st.title('Named Entity Recognition App')

txt=st.text_area('Please input words or a sentence that you want to be analyzed for NER ')

clicked=st.button('Process', key=None)
print(type(txt))
if clicked:
    payload="{\"text\":\""+txt+"\",\"model\":\"spacy\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    st.write(response.text)

