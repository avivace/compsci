from bs4 import BeautifulSoup
with open("data1_1.html") as fp:
    soup = BeautifulSoup(fp)

data = []

questions = soup.find_all(class_="que")
for question in questions:
    obj = {}
    obj["text"] = question.find_all(class_="qtext")[0].text.strip().replace("\t", "").replace("\n"," ")
    data.append(obj)

print(data)
