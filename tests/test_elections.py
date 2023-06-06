"""A collection of tests for the elections module"""
from google_civic_information_api import elections
import pytest

# Elections Tests

def test_elections_proper_usage():
    """Test that the function receives properly shaped data from the API"""

# VoterInfo Tests
def test_voter_info_invalid_params():
    """Test the invalid parameter verifications"""
    with pytest.raises(ValueError, match="official_only must be True or False"):
        elections.voter_info("api-key", "address", official_only="Invalid")

def test_voter_info_proper_usage():
    """Test that the function receives properly shaped data from the API"""