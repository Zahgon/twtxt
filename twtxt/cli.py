"""
    twtxt.cli
    ~~~~~~~~~

    This module implements the command-line interface of twtxt.

    :copyright: (c) 2016-2022 by buckket.
    :license: MIT, see LICENSE for more details.
"""

import logging
import os
import shutil
import sys
import textwrap
from itertools import chain

import click

from twtxt.cache import Cache
from twtxt.config import Config
from twtxt.helper import run_pre_tweet_hook, run_post_tweet_hook
from twtxt.helper import sort_and_truncate_tweets
from twtxt.helper import style_timeline, style_source, style_source_with_status
from twtxt.helper import validate_created_at, validate_text, validate_config_key
from twtxt.log import init_logging
from twtxt.mentions import expand_mentions
from twtxt.models import Tweet, Source
from twtxt.twfile import get_local_tweets, add_local_tweet
from twtxt.twhttp import get_remote_tweets, get_remote_status

logger = logging.getLogger(__name__)


@click.group()
@click.option("--config", "-c",
              type=click.Path(exists=True, file_okay=True, readable=True, writable=True, resolve_path=True),
              help="Specify a custom config file location.")
@click.option("--verbose", "-v",
              is_flag=True, default=False,
              help="Enable verbose output for debugging purposes.")
@click.version_option()
@click.pass_context
def cli(ctx, config, verbose):
    """Decentralised, minimalist microblogging service for hackers."""
    pass


@cli.command()
@click.option("--created-at",
              callback=validate_created_at,
              help="ISO 8601 formatted datetime string to use in Tweet, instead of current time.")
@click.option("--twtfile", "-f",
              type=click.Path(file_okay=True, writable=True, resolve_path=True),
              help="Location of your twtxt file. (Default: twtxt.txt)")
@click.argument("text", callback=validate_text, nargs=-1)
@click.pass_context
def tweet(ctx, created_at, twtfile, text):
    """Append a new tweet to your twtxt file."""
    pass


@cli.command()
@click.option("--pager/--no-pager",
              is_flag=True,
              help="Use a pager to display content. (Default: False)")
@click.option("--limit", "-l",
              type=click.INT,
              help="Limit total number of shown tweets. (Default: 20)")
@click.option("--twtfile", "-f",
              type=click.Path(exists=True, file_okay=True, readable=True, resolve_path=True),
              help="Location of your twtxt file. (Default: twtxt.txt")
@click.option("--ascending", "sorting",
              flag_value="ascending",
              help="Sort timeline in ascending order.")
@click.option("--descending", "sorting",
              flag_value="descending",
              help="Sort timeline in descending order. (Default)")
@click.option("--timeout",
              type=click.FLOAT,
              help="Maximum time requests are allowed to take. (Default: 5.0)")
@click.option("--porcelain",
              is_flag=True,
              help="Style output in an easy-to-parse format. (Default: False)")
@click.option("--source", "-s",
              help="Only show feed of the given source. (Can be nick or URL)")
@click.option("--cache/--no-cache",
              is_flag=True,
              help="Cache remote twtxt files locally. (Default: True)")
@click.option("--force-update",
              is_flag=True,
              help="Force update even if cache is up-to-date. (Default: False)")
@click.pass_context
def timeline(ctx, pager, limit, twtfile, sorting, timeout, porcelain, source, cache, force_update):
    """Retrieve your personal timeline."""
    pass


@cli.command()
@click.option("--pager/--no-pager",
              is_flag=True,
              help="Use a pager to display content. (Default: False)")
@click.option("--limit", "-l",
              type=click.INT,
              help="Limit total number of shown tweets. (Default: 20)")
@click.option("--ascending", "sorting",
              flag_value="ascending",
              help="Sort timeline in ascending order.")
@click.option("--descending", "sorting",
              flag_value="descending",
              help="Sort timeline in descending order. (Default)")
@click.option("--timeout",
              type=click.FLOAT,
              help="Maximum time requests are allowed to take. (Default: 5.0)")
@click.option("--porcelain",
              is_flag=True,
              help="Style output in an easy-to-parse format. (Default: False)")
@click.option("--cache/--no-cache",
              is_flag=True,
              help="Cache remote twtxt files locally. (Default: True)")
@click.option("--force-update",
              is_flag=True,
              help="Force update even if cache is up-to-date. (Default: False)")
@click.argument("source")
@click.pass_context
def view(ctx, **kwargs):
    """Show feed of given source."""
    pass


@cli.command()
@click.option("--check/--no-check",
              is_flag=True,
              help="Check if source URL is valid and readable. (Default: True)")
@click.option("--timeout",
              type=click.FLOAT,
              help="Maximum time requests are allowed to take. (Default: 5.0)")
@click.option("--porcelain",
              is_flag=True,
              help="Style output in an easy-to-parse format. (Default: False)")
@click.pass_context
def following(ctx, check, timeout, porcelain):
    """Return the list of sources you’re following."""
    pass


@cli.command()
@click.argument("nick")
@click.argument("url")
@click.option("--force", "-f",
              flag_value=True,
              help="Force adding and overwriting nick")
@click.pass_context
def follow(ctx, nick, url, force):
    """Add a new source to your followings."""
    pass


@cli.command()
@click.argument("nick")
@click.pass_context
def unfollow(ctx, nick):
    """Remove an existing source from your followings."""
    pass


@cli.command()
def quickstart():
    """Quickstart wizard for setting up twtxt."""
    pass


@cli.command()
@click.argument("key", required=False, callback=validate_config_key)
@click.argument("value", required=False)
@click.option("--remove",
              flag_value=True,
              help="Remove given item")
@click.option("--edit", "-e",
              flag_value=True,
              help="Open config file in editor")
@click.pass_context
def config(ctx, key, value, remove, edit):
    """Get or set config item."""
    pass


main = cli
