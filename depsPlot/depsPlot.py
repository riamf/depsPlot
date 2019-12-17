import click
from .debug.log import logger
from .debug.log import setup_log_level
from .debug.log import DEBUG


@click.command()
@click.option('--verbose', is_flag=True, help='will do a verbose mode')
@click.option('--xcodeproj', required=True, help='')
def cli(verbose):
    setup_log_level(level=DEBUG)
    logger.debug("some example log")
