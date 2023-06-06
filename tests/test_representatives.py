"""A collection of tests for the representatives module"""
from google_civic_information_api import representatives
import pytest

# Representative by Address Tests
def test_address_invalid_params():
    """Test the invalid parameter verifications"""
    with pytest.raises(ValueError, match="include_offices must be True or False") as exc_info:
        representatives.representative_info_by_address("api-key", "address", include_offices="Invalid")

    with pytest.raises(ValueError, match=r"levels must be one of .*") as exc_info:
        representatives.representative_info_by_address("api-key", "address", levels="Invalid")

    with pytest.raises(ValueError, match=r"roles must be one of .*") as exc_info:
        representatives.representative_info_by_address("api-key", "address", roles="Invalid")

def test_address_bad_request():
    """Test that when given an empty or invalid address, the function receives a 400 Bad Request"""

def test_address_proper_usage():
    """Test that the function receives properly shaped data from the API"""

# Representatives by Division Tests
def test_division_invalid_params():
    """Test the invalid parameter verifications"""
    with pytest.raises(ValueError, match="recursive must be True or False") as exc_info:
        representatives.representative_info_by_division("api-key", "ocd-id", recursive="Invalid")

    with pytest.raises(ValueError, match=r"levels must be one of .*") as exc_info:
        representatives.representative_info_by_division("api-key", "ocd-id", levels="Invalid")

    with pytest.raises(ValueError, match=r"roles must be one of .*") as exc_info:
        representatives.representative_info_by_division("api-key", "ocd-id", roles="Invalid")