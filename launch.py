"""
Send a bunch of requests to median-microservice.
"""
from datetime import datetime
from random import randrange
from urllib import urlencode
from urllib2 import Request, urlopen

MICROSERVICE_HOST = '159.203.166.146'


def send_requests_to_median(amount, upper_limit):
    """
    Send an `amount` of random put requests with median requests interpersed.

    Args:
    amount (int): The amount of requests to send.
    upper_limit (int): The highest number you want to send to /put.
    median_interval
    """
    for i in range(0, amount):
        this_int = randrange(1, upper_limit)
        data = urlencode({'int': this_int})
        req = Request('http://{}/put'.format(MICROSERVICE_HOST), data)
        response = urlopen(req)
        if response.code == 200:
            print('{} - Sent: {}'.format(datetime.now(), this_int))
        del response

if __name__ == '__main__':
    send_requests_to_median(2000, 20000)
