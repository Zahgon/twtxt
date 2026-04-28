"""
    twtxt.twhttp
    ~~~~~~~~~~~~

    This module handles HTTP requests via aiohttp/asyncio.

    :copyright: (c) 2016-2022 by buckket.
    :license: MIT, see LICENSE for more details.
"""

import asyncio
import logging
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from itertools import chain
from ssl import CertificateError

import aiohttp
import click
import humanize

from twtxt.helper import generate_user_agent
from twtxt.parser import parse_tweets

logger = logging.getLogger(__name__)


class SourceResponse:
    """A :class:`SourceResponse` contains information about a :class:`Source`’s HTTP request.

    :param int status_code: response status code
    :param str content_length: Content-Length header field
    :param str last_modified: Last-Modified header field
    """

    def __init__(self, status_code, content_length, last_modified):
        self.status_code = status_code
        self.content_length = content_length
        self.last_modified = last_modified

    @property
    def natural_content_length(self):
        pass

    @property
    def natural_last_modified(self):
        pass


async def retrieve_status(client, source):
    pass


async def retrieve_file(client, source, limit, cache):
    pass


async def process_sources_for_status(client, sources):
    pass


async def process_sources_for_file(client, sources, limit, cache=None):
    pass


def get_remote_tweets(sources, limit=None, timeout=5.0, cache=None):
    pass


def get_remote_status(sources, timeout=5.0):
    pass
