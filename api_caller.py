from email.policy import HTTP
import requests
from requests.exceptions import HTTPError


class APICaller:
    """This class uses the requests library to make API calls to the Liquipedia API."""

    BASE_URL = "https://liquipedia.net/valorant/api.php"
    BASE_HEADERS = {"user-agent": "valcomps/0.1 (http://www.valcomps.gg)"}
    BASE_PARAMS = {"action": "parse", "format": "json"}

    def __init__(self):
        """Initialize the APICaller object. Test the connection to the API.

        Raises:
            HTTPError: HTTP response returned unsuccessful status code.
            ConnectionError: Connection to the API failed.
            Timeout: Connection to the API timed out.
        """
        try:
            self.response = requests.get(
                self.BASE_URL, headers=self.BASE_HEADERS, params=self.BASE_PARAMS
            )

            self.response.raise_for_status()
        except HTTPError as exc:
            SystemExit("HTTPError: {}".format(exc.response.status_code))

    def get_page(self, page_name):
        """Get page element from json formatted response.

        Args:
            page_name (str): The name of the requested page on the Liquipedia Wiki.

        Raises:
            HTTPError: HTTP response returned unsuccessful status code.
            ConnectionError: Connection to the API failed.
            Timeout: Connection to the API timed out.
        """
        try:
            self.response = requests.get(
                self.BASE_URL, params=self.BASE_PARAMS | {"page": page_name}
            )

            self.response.raise_for_status()
        except HTTPError as exc:
            SystemExit("HTTPError: {}".format(exc.response.status_code))
