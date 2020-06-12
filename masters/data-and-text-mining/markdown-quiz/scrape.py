from bs4 import BeautifulSoup
import json
import sys
import hashlib
import os
import shutil

def DoesListContainsQuestion(question, list):
    for q in list:
        if q == question:
            return True
    return False

path = './quizreviews'

files = []
# Root, Directories, Files
for r, d, f in os.walk(path):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))

print(len(files), "quiz reviews to scrape")

answeredQuestionsHash = []
unansweredQuestionsHash = []

init = False

for f in files:
    print("Processing", f)

    with open(f, encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, features="html.parser")


    data = []
    title = soup.title.text[6:].replace(':', '')
    title = title.replace(' Attempt review', '')
    questions = soup.find_all(class_="que")

    try:
        os.mkdir("dumps")
        print("Directory dumps Created ")
    except FileExistsError:
        if not init:
            folder = 'dumps'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            init = True
        else:
            pass

    for question in questions:
        obj = {}
        obj["chapter"] = title

        if question.find_all(class_="grade")[0].text == "Mark 1.00 out of 1.00":
            obj["question"] = question.find_all(class_="qtext")[0].text.strip().replace("\t", "").replace("\n", " ").replace(u"\u03c6", "PHI")
#				questionSlug = hashlib.sha224(obj["question"].encode('utf-8')).hexdigest()
#				print("Found full grade question", questionSlug[-8:])
            obj["answers"] = []
            answerObj = {}
            corrects=0
            answersText = []  # list of all possible answers for later use
            for answer in question.find_all(class_=["r0", "r1"]):
                answerObj = {}
                answerObj["text"] = answer.text.replace(u"\u03c6", "PHI")
                answersText.append(answerObj["text"])

                if "checked" in answer.input.attrs:
                    answerObj["correct"] = True
                    corrects+=1
                else:
                    answerObj["correct"] = False

                obj["answers"].append(answerObj)
#				print(" with", len(obj["answers"]), "options,", corrects, "correct")

            # Get hash of question and save it for later comparison
            answersText.sort()
            textToHash = obj["question"]
            for text in answersText:
                textToHash += text
            textToHash = textToHash.replace(" ", "").replace("\n", "").replace("\t", "")
            questionSlug = hashlib.sha224(textToHash.encode('utf-8')).hexdigest()
            print("TextToHash for this question: \"", textToHash, "\" ", questionSlug)

            obj["meta"] = {}
            obj["meta"]["schemaver"] = "2"
            obj["meta"]["hash"] = str(questionSlug)[-8:]

            if(not(DoesListContainsQuestion(questionSlug, answeredQuestionsHash))):
                try:
                    os.mkdir("dumps/"+title)
                    print("Directory " , title ,  " Created ")
                except FileExistsError:
                    pass
                with open("dumps/"+title+"/"+str(questionSlug)[-8:]+'.json', 'w') as outfile:
                    json.dump(obj, outfile)

                answeredQuestionsHash.append(questionSlug)

for f in files:
    print("Processing unanswered questions", f)

    with open(f, encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, features="html.parser")

    data = []
    title = "Unanswered " + soup.title.text[6:].replace(':', '')
    title = title.replace(' Attempt review', '')
    questions = soup.find_all(class_="que")

    for question in questions:
        obj = {}
        obj["chapter"]= title

        if question.find_all(class_="grade")[0].text != "Mark 1.00 out of 1.00":
            obj["question"] = question.find_all(class_="qtext")[0].text.strip().replace("\t", "").replace("\n", " ").replace(u"\u03c6", "PHI")
            #				questionSlug = hashlib.sha224(obj["question"].encode('utf-8')).hexdigest()
            #				print("Found full grade question", questionSlug[-8:])
            obj["answers"] = []
            answerObj = {}
            answersText = []  # list of all possible answers for later use
            for answer in question.find_all(class_=["r0", "r1"]):
                answerObj = {}
                answerObj["text"] = answer.text.replace(u"\u03c6", "PHI")
                answersText.append(answerObj["text"])

                answerObj["correct"] = False

                obj["answers"].append(answerObj)
            #				print(" with", len(obj["answers"]), "options,", corrects, "correct")

            # Get hash of question and save it for later comparison
            answersText.sort()
            textToHash = obj["question"]
            for text in answersText:
                textToHash += text
            textToHash = textToHash.replace(" ", "").replace("\n", "").replace("\t", "")
            questionSlug = hashlib.sha224(textToHash.encode('utf-8')).hexdigest()
            print("TextToHash for this question: \"", textToHash, "\" ", questionSlug)

            obj["meta"] = {}
            obj["meta"]["schemaver"] = "2"
            obj["meta"]["hash"] = str(questionSlug)[-8:]

            if not (DoesListContainsQuestion(questionSlug, answeredQuestionsHash)) and not (DoesListContainsQuestion(questionSlug, unansweredQuestionsHash)):
                try:
                    os.mkdir("dumps/" + title)
                    print("Directory ", title, " Created ")
                except FileExistsError:
                    pass
                with open("dumps/" + title + "/" + str(questionSlug)[-8:] + '.json', 'w') as outfile:
                    json.dump(obj, outfile)

                unansweredQuestionsHash.append(questionSlug)