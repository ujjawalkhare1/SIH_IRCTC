import spacy
nlp = spacy.load('en')

docx = nlp(u"I am looking for an Italian Restaurant where I can eat")

