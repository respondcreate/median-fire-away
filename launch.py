"""Send a bunch of requests to median-microservice."""
from argparse import ArgumentParser
from datetime import datetime
from random import randrange
from urllib import urlencode
from urllib2 import Request, urlopen


def send_requests_to_median(host, amount, upper_limit):
    """
    Send an `amount` of random put requests with median requests interpersed.

    Args:
    amount (int): The amount of requests to send.
    upper_limit (int): The highest number you want to send to /put.
    """
    for i in range(0, amount):
        this_int = randrange(1, upper_limit)
        data = urlencode({'int': this_int})
        req = Request('http://{}/put'.format(host), data)
        response = urlopen(req)
        if response.code == 200:
            print('{} - Sent: {}'.format(datetime.now(), this_int))
        del response


def create_parser():
    """Create a command line parser for this module."""
    parser = ArgumentParser(
        description='Send some requests to median-microservice.'
    )
    parser.add_argument(
        'host',
        type=str,
        help="The median-microservice host."
    )
    parser.add_argument(
        '-a',
        '--amount',
        type=int,
        default=2000,
        help="The amount of /put requests you want to send."
    )
    parser.add_argument(
        '-u',
        '--upper-limit',
        type=int,
        default=100000,
        help='The largest integer to send to /put (each number sent will be '
             'randomly chosen between 1 and this value).'
    )
    return parser

if __name__ == '__main__':
    parser = create_parser()

    # Arguments to set
    args = parser.parse_args()
    host = args.host
    amount = args.amount
    upper_limit = args.upper_limit
    send_requests_to_median(host, amount, upper_limit)
