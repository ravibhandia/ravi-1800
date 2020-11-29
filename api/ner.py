import spacy
import stanza

class NER(object):
    model_spacy=None
    model_stanza=None

    @classmethod
    def get_spacy_model(cls):
        if cls.model_spacy is None:
            cls.model_spacy= spacy.load("en_core_web_sm")
        return cls.model_spacy

    @classmethod
    def get_stanza_model(cls):
        if cls.model_stanza is None:
            #can take a while to load roughly 3-5 minutes (ideally would have in Dockerfile)
            stanza.download('en',processors='tokenize,ner')
            cls.model_stanza = stanza.Pipeline(lang='en', processors='tokenize,ner')
        return cls.model_stanza

    @classmethod
    def get_entities(cls, input, mod):
        """For the input, get entities and return them."""
        switcher = {
            "spacy": cls.get_spacy_model(),
            "stanza":cls.get_stanza_model()
        }
        clf = switcher.get(mod, cls.get_spacy_model())
        if mod=='stanza':
            return dict([(str(ent.text),str(ent.type)) for sent in clf(input).sentences for ent in sent.ents])
        else:
            #when using spacy
            return dict([(str(x), x.label_) for x in clf(input).ents])