# google-civic-information-api-py
![PyPI](https://img.shields.io/pypi/v/google-civic-information-api?color=blue&label=PyPi&style=plastic)
![GitHub](https://img.shields.io/github/license/k0pak4/google-civic-information-api-py?label=License&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/google-civic-information-api?label=Python)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/k0pak4/google-civic-information-api-py/run-unit-tests.yml?style=plastic)

google-civic-information-api-py is a Python wrapper for [Google's Civic Information API](https://developers.google.com/civic-information/docs/v2).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install google-civic-information-api.

```bash
pip install google-civic-information-api
```

## Usage
The google-civic-information-api has three modules: divisions, elections, and representatives. Each module has a few functions, examples of each are provided below.

### divisions
```python
import os
from google_civic_information_api import divisions

civic_api_key = os.environ["TEST_CIVIC_INFO_API_KEY"]

# Search Divisions by Address
search_results = divisions.search(civic_api_key, "District of Columbia")
print(search_results.json())
```

### elections
```python
import os
from google_civic_information_api import elections

civic_api_key = os.environ["TEST_CIVIC_INFO_API_KEY"]

# Search all Elections
elections_results = elections.elections(civic_api_key)
print(elections_results.json())
```

### representatives
```python
import os
from google_civic_information_api import 

civic_api_key = os.environ["TEST_CIVIC_INFO_API_KEY"]

# Retrieve all country level representatives from D.C. by searching by Address
dc_results = representatives.representative_info_by_address(
        civic_api_key, "20001", recursive=True, levels="country")
print(dc_results.json())

# Retrieve all country level representatives from D.C. by searching by OCD Division
dc_results = representatives.representative_info_by_division(
        civic_api_key, "ocd-division/country:us/district:dc", recursive=True, levels="country")
print(dc_results.json())
```

## Contributing
Refer to the [Contributing Guide](https://github.com/k0pak4/google-civic-information-api-py/blob/main/CONTRIBUTING.md) for details on opening issues, pull requests, and development considerations.

## Security
Refer to the [Security Policy](https://github.com/k0pak4/google-civic-information-api-py/blob/main/SECURITY.md) for details on supported versions, reporting vulnerabilities, and other security considerations.

## License

[BSD 3-Clause License](https://github.com/k0pak4/google-civic-information-api-py/blob/main/LICENSE)