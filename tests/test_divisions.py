"""A collection of tests for the divisions module"""
from google_civic_information_api import divisions
import pytest
import os

TEST_API_KEY = os.environ["TEST_CIVIC_INFO_API_KEY"]

# Search Tests
def test_search_proper_usage():
    """Test that the function receives properly shaped data from the API"""
    search_results = divisions.search(TEST_API_KEY, "District of Columbia")
    results_json = search_results.json()

    assert search_results.status_code == 200
    assert len(results_json["results"]) >= 1
    assert "ocdId" in results_json["results"][0]
