# ttfb
A Python script for measuring the time to first byte (TTFB) of one or more URLs using multiple requests
TTFB Checker
Description
# TTFB Tester
A Python script for measuring time to first byte (TTFB) of one or more URLs.

TTFB Tester is a Python script that tests the time to first byte (TTFB) for one or more URLs. It makes multiple requests to each URL and calculates the average TTFB, as well as the fastest, slowest, and median TTFBs.
The script is particularly useful for identifying slow-loading websites or web pages, and can help you optimize your website for better performance.

## Requirements

- Python 3.x
- requests module

## Installation

1. Clone the repository or download the files.
2. Install the requests module using pip: `pip install requests`

## Usage

1. Import the ttfb function from ttfb_tester.py.
2. Call the function and pass in a list of URLs to test.
3. Optionally specify the number of requests to make and other options for the requests module.
4. Optionally specify a log file to save response headers for debug purposes.

Example:

```python
from ttfb_tester import ttfb

urls = ["https://www.example.com", "https://www.google.com"]
ttfb(urls, num_requests=3, options={"verify": False}, log_file="ttfb.log", debug=True, verbose=True)
