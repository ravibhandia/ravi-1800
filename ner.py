import spacy


class NER(object):
    model_spacy=None

    @classmethod
    def get_spacy_model(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model_spacy is None:
            cls.model_spacy= spacy.load("en_core_web_sm")
        return cls.model_spacy

    @classmethod
    def get_entities(cls, input, mod):
        """For the input, get entities and return them."""
        switcher = {
            "spacy": cls.get_spacy_model()
        }
        clf = switcher.get(mod, cls.get_spacy_model())
        return dict([(str(x), x.label_) for x in clf(input).ents])