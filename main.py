
from bottle import Bottle, Response, request,post,run
import json
from ner import *
import json
app=Bottle()

@post("/predict_entity")
def predict_entity():
    text = request.json["text"]
    model = request.json["model"]
    if model is None:
        print(1)
        model='spacy'
    entity_dict = NER.get_entities(text,model)
    return Response(json.dumps(entity_dict), status=200, mimetype='application/json')


run(reloader=True, debug=True)