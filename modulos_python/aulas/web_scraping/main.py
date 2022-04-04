from bs4 import BeautifulSoup
import requests as req

LINK = "https://www.stackoverflow.com/questions/tagged/python"
TITLE_CLASS = ".s-link"
EXCERPT_CLASS = ".s-post-summary--content-excerpt"
RELTIME_CLASS = ".relativetime"
VOTES_CLASS = ".s-post-summary--stats-item-number"

NO_DATA_TEXTS = ["NOT APLICABLE"] * 4


response = req.get(LINK)
html = BeautifulSoup(response.text, "html.parser")

questions = html.select(".s-post-summary")

questions_data = dict()

for i, question in enumerate(questions):
    title, summary, relativetime, votes = NO_DATA_TEXTS
    if question.select_one(TITLE_CLASS) is not None:
        title = question.select_one(TITLE_CLASS).text  # type: ignore

    if question.select_one(EXCERPT_CLASS) is not None:
        summary = question.select_one(EXCERPT_CLASS).text  # type: ignore

    if question.select_one(RELTIME_CLASS) is not None:
        relativetime = question.select_one(RELTIME_CLASS).text  # type: ignore

    if question.select_one(VOTES_CLASS) is not None:
        votes = question.select_one(VOTES_CLASS).text  # type: ignore

    questions_data[i] = {
        "title": title,
        "summary": summary.strip("\r\t\n").strip("                  "),
        "relativetime": relativetime,
        "votes": votes,
    }

for key, data in questions_data.items():
    print(f"Question {key} ".center(40, "#"))
    print(f"{data.get('title')}")
    print(f"  {data.get('summary')}")
    print(f"  asked: {data.get('relativetime')}")
    print(f"  votes: {data.get('votes')}")
