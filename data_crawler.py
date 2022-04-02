from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, body):
        self.soup = BeautifulSoup(body, "html.parser")
        bracket = self.soup.find("div", {"class": "bracket-scroller"})
        self.matchups = bracket.find_all(
            "div", {"class": "bracket-popup-wrapper bracket-popup-team"}
        )

    def get_matchups(self):
        return self.matchups
