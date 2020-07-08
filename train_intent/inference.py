from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.training_data  import load_data


train_data = load_data('./test.json')

trainer = Trainer(config.load("config.yml"))
trainer.train(train_data)
# model_directory = trainer.persist('/models/')
# print(model_directory)
# interpreter = Interpreter.load("./models/nlu/component_5_DIETClassifier.tf_model")
# interpreter.parse(u"I am looking for an Italian Restaurant where I can eat")
