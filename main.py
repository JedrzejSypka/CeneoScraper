from email import contentmanager
import requests
from bs4 import BeautifulSoup
response= requests.get("https://www.ceneo.pl/63490289#tab=reviews")
print(response.status_code)

page = BeautifulSoup(response.text, "html.parser")



opinions =page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id= opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recommendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
stars = opinion.select_one("span.user-post__score-count").get_text().strip()
content = opinion.select_one("div.user-post__text").get_text().strip()
pros = opinion.select("div.review-feature__item--positives ~ div.review-feature__item")
usuful = opinion.select_one("span[id^=\"votes-yes]").get_text().strip()
print(recommendation)
print(stars)
print(content)
print(pros)
