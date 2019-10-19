from bs4 import BeautifulSoup
import json
import sys

with open(sys.argv[1]) as fp:
	soup = BeautifulSoup(fp)

data = []

questions = soup.find_all(class_="que")
for question in questions:
	obj = {}
	if (question.find_all(class_="grade")[0].text == "Mark 1.00 out of 1.00"):
		print("Full grade question found")
		obj["text"] = question.find_all(class_="qtext")[0].text.strip().replace("\t", "").replace("\n"," ")
		print("QUESTION TEXT:", obj["text"])
		obj["answers"] = []
		answerObj = {}

		for answer in question.find_all(class_=["r0", "r1"]):
			answerObj = {}
			answerObj["text"] = answer.text
			if "checked" in answer.input.attrs:
				print(answer.input["checked"])
				answerObj["correct"] = True
			else:
				answerObj["correct"] = False

			print("ANSWER:", answer.text)
			
			obj["answers"].append(answerObj)

		data.append(obj)


jsondata = json.dumps(data, indent=4, sort_keys=True)

with open(sys.argv[1][:-5]+'.json', 'w') as outfile:
    json.dump(jsondata, outfile)