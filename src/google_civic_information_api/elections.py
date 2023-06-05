"""The elections module contains functions for the elections resource"""

import requests
import constants

ELECTIONS_URL = f"{constants.BASE_URL}/elections"

VOTER_INFO_URL = f"{constants.BASE_URL}/voterinfo"


def elections(api_key):
    """Queries the electionQuery endpoint with the provided API key"""

    query_params = {"key": api_key}
    api_response = requests.get(ELECTIONS_URL, params=query_params,
                                timeout=constants.DEFAULT_TIMEOUT)
    return api_response


def voter_info(api_key, address, election_id=None, official_only=False):
    """Queries the voterInfoQuery endpoint with the provided parameters"""

    query_params = {"key": api_key, "address": address, "officialOnly": official_only}
    if election_id:
        query_params["electionID"] = election_id

    api_response = requests.get(VOTER_INFO_URL, params=query_params,
                                timeout=constants.DEFAULT_TIMEOUT)
    return api_response
