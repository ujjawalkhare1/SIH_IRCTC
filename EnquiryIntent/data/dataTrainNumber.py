import random

filepath = './enquiryData.txt'
with open(filepath,'r',encoding = 'utf-8') as infile:
    sents = infile.read().strip().split('\n')

fp = open("./train_data1.json",'w')
fp.write('{\n "rasa_nlu_data":{\n')
fp.write('\n "regex_features": [],\n "entity_synonyms": [],')
fp.write('"common_examples":[')

iteration = 120
for i in range(iteration):	
	for sent in sents:
		sent = sent  + " "
		ind1 = random.randrange(1, 3, 3)
		ind2 = random.randrange(1000, 10000, 4)

		trainNumber = str(ind1) + str(ind2) 
		sent = sent.replace("{train}", trainNumber)
		
		#Train number data for training
		startTrainNumberEntity = sent.index(trainNumber)
		lenEntity = len(trainNumber)
		endTrainNumberEntity = startTrainNumberEntity + lenEntity

		sent= sent.lower()

		fp.write('	{ \n')
		fp.write('	"text": "' + sent + '",\n')
		fp.write('	"intent": "running status", \n')
		fp.write('	"entities": [\n   { \n ')


		fp.write('	"start" : ' + str(startTrainNumberEntity) + ', \n')
		fp.write('	"end":' + str(endTrainNumberEntity) + ',\n')
		fp.write('	"value":"' + trainNumber + '",\n')
		fp.write('	"entity": "trainNumber" \n   }')

		fp.write('\n')
		fp.write('	]\n')
	#	if(i!=iteration-1):
		fp.write('	}, \n')
		# else:
		# 	fp.write('	} \n')

filepath1 = './pnrStatusData.txt'
with open(filepath1,'r',encoding = 'utf-8') as infile1:
    sents1 = infile1.read().strip().split('\n')

for i in range(iteration):
	for sent in sents1:
		sent = sent + " "

		pnrNumber = str(random.randrange(10001, 99999,4)) + str(random.randrange(10001, 99999,4))
		# print(pnrNumber)
		# print(sent + "semt")
		sent = sent.replace('{pnr}', pnrNumber)
		startPnrNumberEntity = sent.index(pnrNumber)
		lenEntity = len(pnrNumber)
		endPnrNumberEntity = startPnrNumberEntity + lenEntity

		sent = sent.lower()


		fp.write('	{ \n')
		fp.write('	"text": "' + sent + '",\n')
		fp.write('	"intent": "pnr number", \n')
		fp.write('	"entities": [\n   { \n ')


		fp.write('	"start" : ' + str(startPnrNumberEntity) + ', \n')
		fp.write('	"end":' + str(endPnrNumberEntity) + ',\n')
		fp.write('	"value":"' + pnrNumber + '",\n')
		fp.write('	"entity": "pnrNumber" \n   }')


		fp.write('\n')
		fp.write('	]\n')
		fp.write('	}, \n')


fp.write(']' + '\n')
fp.write('} \n')
fp.write('} \n')
fp.close();