from bs4 import BeautifulSoup
import requests as req

LINK = "https://www.stackoverflow.com/questions/tagged/python"

html = req.get(LINK)
print(html.content)
