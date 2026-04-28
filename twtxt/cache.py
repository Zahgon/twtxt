"""
    twtxt.cache
    ~~~~~~~~~~~

    This module implements a caching system for storing tweets.

    :copyright: (c) 2016-2022 by buckket.
    :license: MIT, see LICENSE for more details.
"""

import logging
import os
import shelve
from time import time as timestamp

from click import get_app_dir

logger = logging.getLogger(__name__)


class Cache:
    cache_dir = get_app_dir("twtxt")
    cache_name = "cache"

    def __init__(self, cache_file, cache, update_interval=0):
        """Initializes new :class:`Cache` object.

        :param str cache_file: full path to the loaded cache file.
        :param ~shelve.Shelve cache: a Shelve object, with cache loaded.
        :param int update_interval: number of seconds the cache is considered to be
                                    up-to-date without calling any external resources.
        """
        self.cache_file = cache_file
        self.cache = cache
        self.update_interval = update_interval

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.close()

    @classmethod
    def from_file(cls, file, *args, **kwargs):
        """Try loading given cache file."""
        pass

    @classmethod
    def discover(cls, *args, **kwargs):
        """Make a guess about the cache file location and try loading it."""
        pass

    @property
    def last_updated(self):
        """Returns *NIX timestamp of last update of the cache."""
        pass

    @property
    def is_valid(self):
        """Checks if the cache is considered to be up-to-date."""
        pass

    def mark_updated(self):
        """Mark cache as updated at current *NIX timestamp"""
        pass

    def is_cached(self, url):
        """Checks if specified URL is cached."""
        pass

    def last_modified(self, url):
        """Returns saved 'Last-Modified' header, if available."""
        pass

    def add_tweets(self, url, last_modified, tweets):
        """Adds new tweets to the cache."""
        pass

    def get_tweets(self, url, limit=None):
        """Retrieves tweets from the cache."""
        pass

    def remove_tweets(self, url):
        """Tries to remove cached tweets."""
        pass

    def close(self):
        """Closes Shelve object."""
        pass

    def sync(self):
        """Syncs Shelve object."""
        pass
