import click
from .debug.log import logger
from .debug.log import setup_log_level
from .debug.log import DEBUG

import subprocess


@click.command()
@click.option('--verbose', is_flag=True, help='will do a verbose mode')
@click.option('--proj', required=True, help='')
def cli(verbose, proj):
    setup_log_level(level=DEBUG)
    logger.debug('some example log')
    build_project(name=proj)


def build_project(name: str):
    logger.debug(f'BUILDING PROJECT {name}')
    result = subprocess.check_output(['xcodebuild', 
                                      '-showBuildSettings',
                                      name,
                                      'build',
                                      'CODE_SIGNING_ALLOWED=NO',
                                      'CODE_SIGNING_REQUIRED=NO'])
    logger.debug(result)
