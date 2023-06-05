"""The representatives module contains functions for the representatives resource."""

import requests
import constants

REPS_URL = f"{constants.BASE_URL}/representatives"

VALID_LEVELS = ["administrativeArea1", "administrativeArea2", "country",
                "international", "locality", "regional", "special", "subLocality1", "subLocality2"]

VALID_ROLES = ["deputyHeadOfGovernment", "executiveCouncil", "governmentOfficer", "judge",
               "headOfGovernment", "headOfState", "highestCourtJudge", "legislatorLowerBody",
               "legislatorUpperBody", "schoolBoard", "specialPurposeOfficer"]


def representative_info_by_address(api_key, address, include_offices=True, levels=None, roles=None):
    """Queries the representativeInfoByAddress endpoint with provided parameters"""

    query_params = {"key": api_key, "address": address,
                    "includeOffices": include_offices}
    if levels and levels in VALID_LEVELS:
        query_params["levels"] = levels
    elif roles and roles not in VALID_LEVELS:
        raise ValueError(f"levels must be one of {VALID_LEVELS}")
    if roles and roles in VALID_ROLES:
        query_params["roles"] = roles
    elif roles and roles not in VALID_ROLES:
        raise ValueError(f"roles must be one of {VALID_ROLES}")

    api_response = requests.get(constants.BASE_URL, params=query_params,
                                timeout=constants.DEFAULT_TIMEOUT)
    return api_response


def representative_info_by_division(api_key, ocd_id, recursive=True, levels=None, roles=None):
    """Queries the represenativeInfoByDivision endpoint with provided paramaeters"""

    query_params = {"key": api_key, "recursive": recursive}
    if levels and levels in VALID_LEVELS:
        query_params["levels"] = levels
    elif roles and roles not in VALID_LEVELS:
        raise ValueError(f"levels must be one of {VALID_LEVELS}")
    if roles and roles in VALID_ROLES:
        query_params["roles"] = roles
    elif roles and roles not in VALID_ROLES:
        raise ValueError(f"roles must be one of {VALID_ROLES}")

    api_response = requests.get(f"{constants.BASE_URL}/{ocd_id}", params=query_params,
                                timeout=constants.DEFAULT_TIMEOUT)
    return api_response
