# from ratelimit import limits, sleep_and_retry

# import requests

# FIFTEEN_MINUTES = 900

# @sleep_and_retry
# # Limiting the number of calls to the function to 1 per 15 minutes.
# @limits(calls=1, period=FIFTEEN_MINUTES)
# def call_api(url):
#     response = requests.get(url)

#     if response.status_code != 200:
#         raise Exception('API response: {}'.format(response.status_code))
#     return response

from ratelimit import limits, RateLimitException
from backoff import on_exception, expo

import requests

FIFTEEN_MINUTES = 900

@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=2, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response


print(call_api('https://api.github.com/users/joshuaclayton'))