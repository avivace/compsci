
```bash
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt

python3 scrape.py quizresults1_data.html
# This produces quizresults1_data.json

# TODO
# Now, aggregate every JSON you managed to scrape
# TODO: Merge, set questions ID, set chapter names in a meta key
python3 template.py quizresults1_data.json
# This produces a quizresults1_data.md
pandoc quizresults1_data.md -o quizsresults1_data.pdf
# Finally, your quiz results are in quizresults1_data.pdf
```
