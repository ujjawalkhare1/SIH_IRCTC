from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Metadata, Interpreter

model_directory = './models/default/model_20200719-141717'
interpreter = Interpreter.load(model_directory)
print(interpreter.parse(u"tell me running status of 23912"))
