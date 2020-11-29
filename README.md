# Named Entity Recognition App
### Built with Stanza, spaCy, Streamlit, Bottle, and Docker


![Demo Gif](https://github.com/ravibhandia/ravi-1800/blob/main/NER_ISS_demo.gif)


The motivation behind this project is to built an tool for people to easily use named entity recognition (NER) models from both stanza and spacy.

A backend API service was built using the Bottle Framework. The code for the api is located in the folder [API](https://github.com/ravibhandia/ravi-1800/tree/main/api). Stanza and spaCy NLP frameworks and models were used to generate NER results.

The front end was built using Streamlit and can be located in the [front_end](https://github.com/ravibhandia/ravi-1800/tree/main/front_end) folder. Using streamlit you can enter any sentences or words you are interested in testing in the text box. You can then select either Stanza or spaCy as the frameworks to be used.

### Startup
To start this app you can just call `docker-compose up -d --build` . To shut the app off you can call `docker-compose down`.

It takes about a minute for the docker-compose to build the connection between the two containers. When the app is ready you can navigate to [http://0.0.0.0:8501/](http://0.0.0.0:8501/) to view the streamlit app. After your first call with the process button, it will take roughly 5 minutes to download the stanza model. After this load time, the app works smoothly and takes very little time on each query.

### Future Work / Issues
1. Once  ` docker-compose up -d --build ` is called, the app only takes roughly 10 seconds to start up. However due to `stanza.download('en',processors='tokenize,ner')` located in [ner.py](https://github.com/ravibhandia/ravi-1800/blob/main/api/ner.py), once the first POST call is made through the API it will take roughly 5 minutes to download the english model in Stanza and the appropriate processors. I have been looking for a way to include the downloading of Stanza models in the dockerfile, but at this time have not found a way. Perhaps, I can use a tar.gz file like I did for the spaCy model.



### Acknowledgments


https://www.javacodemonk.com/named-entity-recognition-spacy-flask-api-1678a5df

https://www.toptal.com/bottle/building-a-rest-api-with-bottle-framework

https://cloudconvert.com/mov-to-gif

https://github.com/stanfordnlp/stanza/issues/367




