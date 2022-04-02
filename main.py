import json

from api_caller import APICaller
from data_crawler import Scraper

PAGE_NAME = "Fight_Club"

if __name__ == "__main__":
    caller = APICaller()

    caller.get_page(PAGE_NAME)
    body = caller.get_json()["parse"]["text"]["*"]

    scraper = Scraper(body)

    with open("temp.html", "w") as f:
        for matchup in scraper.get_matchups():
            f.write(str(matchup) + "\n")
