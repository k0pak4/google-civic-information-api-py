"""A collection of tests for the elections module"""
from google_civic_information_api import elections
import pytest
import os

TEST_API_KEY = os.environ["TEST_CIVIC_INFO_API_KEY"]

# Elections Tests


def test_elections_proper_usage():
    """Test that the function receives properly shaped data from the API"""
    elections_results = elections.elections(TEST_API_KEY)
    results_json = elections_results.json()

    assert elections_results.status_code == 200
    assert "elections" in results_json and len(results_json["elections"]) >= 1
    assert results_json["elections"][0]["id"] == "2000"

# VoterInfo Tests


def test_voter_info_invalid_params():
    """Test the invalid parameter verifications"""
    with pytest.raises(ValueError, match="official_only must be True or False"):
        elections.voter_info("api-key", "address", official_only="Invalid")


def test_voter_info_proper_usage():
    """Test that the function receives properly shaped data from the API"""
    voter_info_results = elections.voter_info(TEST_API_KEY, "20001",
                                              election_id=2000, official_only=False)
    results_json = voter_info_results.json()

    assert voter_info_results.status_code == 200
    assert "election" in results_json
    assert results_json["election"]["id"] == "2000"


def test_voter_info_no_address():
    """Test that when provided an empty address, an error is returned"""
    voter_info_results = elections.voter_info(TEST_API_KEY, "")
    results_json = voter_info_results.json()

    assert voter_info_results.status_code != 200
    assert "error" in results_json
