
from bottle import  Response, request,post,run,get
from ner import *
import json

@get("/")
def read_root():
    return {"message": "Welcome from the API"}

@post("/predict_entity")
def predict_entity():
    text = request.json["text"]
    model = request.json["model"]
    if model is None:
        print(1)
        model='spacy'
    entity_dict = NER.get_entities(text,model)
    return Response(json.dumps(entity_dict), status=200, mimetype='application/json')


run(host='0.0.0.0',reloader=True, debug=True,port=8080)