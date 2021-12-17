#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace
from pathlib import Path

from modules.guesser import guess_text
from src.logger import logger, setup_logging


def main() -> None:
    # Initialise the logging system
    setup_logging()

    parser = ArgumentParser(description='Extract the voice from the audio and transcribe it into text to find out what is being said')
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    # Extract
    subparser = subparsers.add_parser('guess', help='Extract the voice and transcribe it.')
    subparser.add_argument('--input', type=str, required=True, help="Path to the audio file")

    arguments = parser.parse_args()
    if arguments.command:
        process_arguments(arguments)
    else:
        parser.print_help()


def process_arguments(arguments: Namespace) -> None:
    logger.info("Processing arguments")

    command = arguments.command
    if command == "guess":
        input_folder = arguments.input
        guesser_handler(input_folder)
    else:
        logger.error(f"Command {command} is not recognised")


def guesser_handler(input_folder: str) -> None:
    input_path = Path(input_folder).absolute()
    guess_text(input_path)


if __name__ == '__main__':
    main()
