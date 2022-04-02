import re
import string
from bs4 import BeautifulSoup

from game_data import Game


class Scraper:
    def __init__(self, body):
        self.soup = BeautifulSoup(body, "html.parser")
        self.games = []
        self._scrape_games()

    def _scrape_games(self):
        brackets_html = self.soup("div", {"class": "bracket-scroller"})
        if not brackets_html:
            raise Exception("No brackets found")

        for bracket_html in brackets_html:
            matchups_html = bracket_html(
                "div", {"class": "bracket-popup-wrapper bracket-popup-team"}
            )

            for matchup_html in matchups_html:
                teams = tuple(
                    team_html["data-highlightingclass"]
                    for team_html in matchup_html(
                        "span", {"class": "team-template-team-short"}
                    )
                )

                for game_html in matchup_html(
                    "div", {"class": "bracket-popup-body-match-container"}
                ):
                    if game_html.find(
                        "div", {"class": "bracket-popup-body-match-mapskip"}
                    ):
                        continue

                    game = Game()

                    game.teams = teams

                    game.map = (
                        game_html.find("div", {"class": "bracket-popup-body-match-map"})
                        .a["title"]
                        .upper()
                    )

                    game.agents = tuple(
                        tuple(
                            agent_html["title"]
                            .translate(str.maketrans("", "", string.punctuation))
                            .upper()
                            for agent_html in agents_html.children
                        )
                        for agents_html in game_html(
                            "div",
                            {
                                "style": re.compile(
                                    r"float:(?:left|right);margin-(?:left|right):10px"
                                )
                            },
                        )
                    )

                    self.games.append(game)
