"""A collection of tests for the representatives module"""
from google_civic_information_api import representatives
import pytest
import os

TEST_API_KEY = os.environ["TEST_CIVIC_INFO_API_KEY"]

# Representative by Address Tests


def test_address_invalid_params():
    """Test the invalid parameter verifications"""
    with pytest.raises(ValueError, match="include_offices must be True or False"):
        representatives.representative_info_by_address(
            TEST_API_KEY, "address", include_offices="Invalid")

    with pytest.raises(ValueError, match=r"levels must be one of .*"):
        representatives.representative_info_by_address(
            TEST_API_KEY, "address", levels="Invalid")

    with pytest.raises(ValueError, match=r"roles must be one of .*"):
        representatives.representative_info_by_address(
            TEST_API_KEY, "address", roles="Invalid")


def test_address_bad_request():
    """Test that when given an empty or invalid address, the function receives a 400 Bad Request"""
    address_results = representatives.representative_info_by_address(
        TEST_API_KEY, "")
    results_json = address_results.json()

    assert address_results.status_code == 400
    assert "error" in results_json


def test_address_proper_usage():
    """Test that the function receives properly shaped data from the API"""
    address_results = representatives.representative_info_by_address(
        TEST_API_KEY, "District of Columbia")
    results_json = address_results.json()

    assert address_results.status_code == 200
    assert results_json["kind"] == "civicinfo#representativeInfoResponse"
    assert "divisions" in results_json
    assert "offices" in results_json

# Representatives by Division Tests


def test_division_invalid_params():
    """Test the invalid parameter verifications"""
    with pytest.raises(ValueError, match="recursive must be True or False"):
        representatives.representative_info_by_division(
            TEST_API_KEY, "ocd-id", recursive="Invalid")

    with pytest.raises(ValueError, match=r"levels must be one of .*"):
        representatives.representative_info_by_division(
            TEST_API_KEY, "ocd-id", levels="Invalid")

    with pytest.raises(ValueError, match=r"roles must be one of .*"):
        representatives.representative_info_by_division(
            TEST_API_KEY, "ocd-id", roles="Invalid")


def test_divisions_bad_request():
    """Test that when given an empty or invalid ocdId, the function receives a 404 Not Found"""
    division_results = representatives.representative_info_by_division(
        TEST_API_KEY, "ocd-di")
    results_json = division_results.json()

    assert division_results.status_code == 400
    assert "error" in results_json


def test_divisions_proper_usage():
    """Test that the function receives properly shaped data from the API"""
    division_results = representatives.representative_info_by_division(
        TEST_API_KEY, "ocd-division/country:us/district:dc")
    results_json = division_results.json()

    assert division_results.status_code == 200
    assert "divisions" in results_json
    assert "offices" in results_json
    assert "officials" in results_json
