from bs4 import BeautifulSoup
import json
import sys
import hashlib

with open(sys.argv[1]) as fp:
	soup = BeautifulSoup(fp)

data = []
title = soup.title.text
questions = soup.find_all(class_="que")
for question in questions:
	obj = {}
	obj["chapter"]= title
	if (question.find_all(class_="grade")[0].text == "Mark 1.00 out of 1.00"):
		print("Full grade question found")
		obj["question"] = question.find_all(class_="qtext")[0].text.strip().replace("\t", "").replace("\n"," ")
		questionSlug = hashlib.sha224(obj["question"].encode('utf-8')).hexdigest()
		print("QUESTION TEXT:", obj["question"])
		obj["answers"] = []
		answerObj = {}

		for answer in question.find_all(class_=["r0", "r1"]):
			answerObj = {}
			answerObj["question"] = answer.text
			if "checked" in answer.input.attrs:
				print(answer.input["checked"])
				answerObj["correct"] = True
			else:
				answerObj["correct"] = False

			print("ANSWER:", answer.text)
			
			obj["answers"].append(answerObj)

		with open(str(questionSlug)[-8:]+'.json', 'w') as outfile:
			json.dump(obj, outfile)
