"""
    twtxt.parser
    ~~~~~~~~~~~~

    This module implements the parser for twtxt files.

    :copyright: (c) 2016-2022 by buckket.
    :license: MIT, see LICENSE for more details.
"""

import logging
from datetime import datetime, timezone

import click
import dateutil.parser

from twtxt.models import Tweet

logger = logging.getLogger(__name__)


def make_aware(dt):
    """Appends tzinfo and assumes UTC, if datetime object has no tzinfo already."""
    pass


def parse_iso8601(string):
    """Parse string using dateutil.parser."""
    pass


def parse_tweets(raw_tweets, source, now=None):
    """
        Parses a list of raw tweet lines from a twtxt file
        and returns a list of :class:`Tweet` objects.

        :param list raw_tweets: list of raw tweet lines
        :param Source source: the source of the given tweets
        :param Datetime now: the current datetime

        :returns: a list of parsed tweets :class:`Tweet` objects
        :rtype: list
    """
    pass


def parse_tweet(raw_tweet, source, now=None):
    """
        Parses a single raw tweet line from a twtxt file
        and returns a :class:`Tweet` object.

        :param str raw_tweet: a single raw tweet line
        :param Source source: the source of the given tweet
        :param Datetime now: the current datetime

        :returns: the parsed tweet
        :rtype: Tweet
    """
    pass
