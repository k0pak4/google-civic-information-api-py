"""The divisions module contains functions for the divisions resource"""

import requests
import constants

DIVISIONS_URL = f"{constants.BASE_URL}/divisions"


def search(api_key, query=""):
    """Queries the divisions endpoint with the provided parameters"""

    query_params = {"key": api_key, "query": query}

    api_response = requests.get(DIVISIONS_URL, params=query_params,
                                timeout=constants.DEFAULT_TIMEOUT)
    return api_response
