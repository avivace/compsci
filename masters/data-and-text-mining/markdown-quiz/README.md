# pretty moodle quiz

Given a list of saved quiz reviewes from Moodle (put the saved HTML files in `quizreviews/`), this script produces a single PDF listing each question and each answers, highlighting the correct ones. `pandoc` and `python3` must be installed.


```bash
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt

bash prettyquiz.sh
```
