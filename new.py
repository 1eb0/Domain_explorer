# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from urllib.parse import urlparse, urlunparse


def validate_url(url):
    parsed_url = urlparse(url)

    # Check if scheme is missing
    if not parsed_url.scheme:
        url = 'http://' + url

    # Check if "http://www." is present at the beginning of the string
    if not url.startswith('http://www.'):
        url = url.replace('http://', 'http://www.')

    # Check if ".com" is present at the end of the string
    if not url.endswith('.com'):
        url = url.rstrip('/') + '.com'

    # Check other common top-level domains (.net, .org, etc.) and add ".com" if missing
    if not any(url.endswith(tld) for tld in ['.com', '.net', '.org', '.edu', '.gov', 'co', 'io']):
        url = url.rstrip('/') + '.com'

    # Correct common misspellings
    if 'http://' in url:
        url = url.replace('http://', 'https://', 1)  # Correct http to https

    corrected_url = urlunparse(urlparse(url))
    return corrected_url


# Example usage
user_input = input("Enter a URL: ")
validated_url = validate_url(user_input)
print("Validated URL:", validated_url)
