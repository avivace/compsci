from bs4 import BeautifulSoup
import json
import sys
import hashlib

with open(sys.argv[1]) as fp:
	soup = BeautifulSoup(fp, features="html.parser")

data = []
title = soup.title.text[6:]
questions = soup.find_all(class_="que")
for question in questions:
	obj = {}
	obj["chapter"]= title
	if (question.find_all(class_="grade")[0].text == "Mark 1.00 out of 1.00"):
		obj["question"] = question.find_all(class_="qtext")[0].text.strip().replace("\t", "").replace("\n"," ")
		questionSlug = hashlib.sha224(obj["question"].encode('utf-8')).hexdigest()
		print("Found full grade question", questionSlug[-8:])
		obj["answers"] = []
		answerObj = {}
		corrects=0
		for answer in question.find_all(class_=["r0", "r1"]):
			
			answerObj = {}
			answerObj["text"] = answer.text
			if "checked" in answer.input.attrs:
				answerObj["correct"] = True
				corrects+=1
			else:
				answerObj["correct"] = False
			
			obj["answers"].append(answerObj)
		print(" with", len(obj["answers"]), "options,", corrects, "correct")

		obj["meta"] = "1"
		with open(str(questionSlug)[-8:]+'.json', 'w') as outfile:
			json.dump(obj, outfile)
