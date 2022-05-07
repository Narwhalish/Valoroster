from api_caller import APICaller
from tourny_scraper import Scraper

PAGE_NAME = "Fight_Club"
# PAGE_NAME = "The_Esports_Club/Gauntlet/Season_4"

if __name__ == "__main__":
    # caller = APICaller()

    # caller.get_page(PAGE_NAME)
    # body = caller.response.json()["parse"]["text"]["*"]

    # with open("test_io/test_input.html", "w") as f:
    #     f.write(body)

    with open("test_io/test_input.html", "r") as f:
        body = f.read()

    scraper = Scraper(body)
    with open("test_io/test_output.txt", "w") as f:
        for game in scraper.games:
            f.write(str(game) + "\n")
