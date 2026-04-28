"""
    twtxt.config
    ~~~~~~~~~~~~

    This module implements the config file parser/writer.

    :copyright: (c) 2016-2022 by buckket.
    :license: MIT, see LICENSE for more details.
"""

import configparser
import logging
import os

import click

from twtxt.models import Source

logger = logging.getLogger(__name__)


class Config:
    """:class:`Config` interacts with the configuration file.

    :param str config_file: full path to the loaded config file
    :param ~configparser.ConfigParser cfg: a :class:`~configparser.ConfigParser` object with config loaded
    """
    config_dir = click.get_app_dir("twtxt")
    config_name = "config"

    def __init__(self, config_file, cfg):
        self.config_file = config_file
        self.cfg = cfg

    @classmethod
    def from_file(cls, file):
        """Try loading given config file.

        :param str file: full path to the config file to load
        """
        pass

    @classmethod
    def discover(cls):
        """Make a guess about the config file location an try loading it."""
        pass

    @classmethod
    def create_config(cls, cfgfile, nick, twtfile, twturl, disclose_identity, add_news):
        """Create a new config file at the default location.

        :param str cfgfile: path to the config file
        :param str nick: nickname to use for own tweets
        :param str twtfile: path to the local twtxt file
        :param str twturl: URL to the remote twtxt file
        :param bool disclose_identity: if true the users id will be disclosed
        :param bool add_news: if true follow twtxt news feed
        """
        pass

    def write_config(self):
        """Writes `self.cfg` to `self.config_file`."""
        pass

    @property
    def following(self):
        """A :class:`list` of all :class:`Source` objects."""
        pass

    @property
    def options(self):
        """A :class:`dict` of all config options."""
        pass

    @property
    def nick(self):
        pass

    @property
    def twtfile(self):
        pass

    @property
    def twturl(self):
        pass

    @property
    def check_following(self):
        pass

    @property
    def use_pager(self):
        pass

    @property
    def use_cache(self):
        pass

    @property
    def porcelain(self):
        pass

    @property
    def disclose_identity(self):
        pass

    @property
    def character_limit(self):
        pass

    @property
    def character_warning(self):
        pass

    @property
    def limit_timeline(self):
        pass

    @property
    def timeline_update_interval(self):
        pass

    @property
    def use_abs_time(self):
        pass

    @property
    def timeout(self):
        pass

    @property
    def sorting(self):
        pass

    @property
    def source(self):
        pass

    @property
    def pre_tweet_hook(self):
        pass

    @property
    def post_tweet_hook(self):
        pass

    def add_source(self, source):
        """Adds a new :class:`Source` to the config’s following section."""
        pass

    def get_source_by_nick(self, nick):
        """Returns the :class:`Source` of the given nick.

        :param str nick: nickname for which will be searched in the config
        """
        pass

    def remove_source_by_nick(self, nick):
        """Removes a :class:`Source` form the config’s following section.

        :param str nick: nickname for which will be searched in the config
        """
        pass

    def build_default_map(self):
        """Maps config options to the default values used by click, returns :class:`dict`."""
        pass

    def check_config_sanity(self):
        """Checks if the given values in the config file are sane."""
        pass
