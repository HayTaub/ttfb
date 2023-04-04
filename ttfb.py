import time
import locale
import requests
from typing import List


def ttfb(urls: List[str], num_requests: int = 1, options: dict = None,
         log_file: str = None, debug: bool = False, verbose: bool = False) -> None:
    """
    Shows time in seconds to first byte of one or more URLs.

    :param urls: List of URLs to test.
    :param num_requests: Number of times to test time to first byte.
    :param options: Dictionary of options to pass to requests.get().
    :param log_file: Log file for response headers.
    :param debug: If True, writes response headers to log_file.
    :param verbose: If True, shows request breakdown during -n calls.
    :return: None
    """
    # Set default options for requests.get().
    default_options = {
        "allow_redirects": True,
        "timeout": 30
    }

    # Add user-specified options to default options.
    if options is not None:
        default_options.update(options)

    # Set locale to use period separators for floating point values.
    locale.setlocale(
        locale.LC_ALL, "C.UTF-8" if "C.UTF-8" in locale.locale_alias.keys() else "C")

    for url in urls:
        if verbose:
            print(url)

        # Initialize list to hold TTFB times.
        ttfbs = []

        # Make multiple requests to get TTFB.
        for i in range(num_requests):
            start_time = time.monotonic()
            response = requests.get(url, **default_options)
            end_time = time.monotonic()

            ttfb = end_time - start_time
            ttfbs.append(ttfb)

            if debug and log_file is not None:
                with open(log_file, "a") as f:
                    f.write(f"Request {i+1}\n")
                    f.write(f"URL: {url}\n")
                    f.write(f"Response headers:\n{response.headers}\n\n")

            if verbose:
                print(f"Request {i+1}")
                print(f"TTFB: {ttfb:.6f}")

        # Show results.
        if num_requests > 1:
            ttfbs_sorted = sorted(ttfbs)
            fastest = ttfbs_sorted[0]
            slowest = ttfbs_sorted[-1]
            median = ttfbs_sorted[num_requests // 2]

            print(f"{url}:")
            print(f"No of requests {num_requests}")
            print(f"\tFastest TTFB: {fastest:.6f}")
            print(f"\tSlowest TTFB: {slowest:.6f}")
            print(f"\tMedian TTFB: {median:.6f}")
        else:
            ttfb = ttfbs[0]
            print(f"{url}: {ttfb:.6f}")


if __name__ == "__main__":
    urls = ['https://google.com', 'https://yahoo.com']
    ttfb(urls, num_requests=5)
