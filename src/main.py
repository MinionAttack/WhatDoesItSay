#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace
from pathlib import Path

from modules.guesser import guess_text
from src.logger import logger, setup_logging


def main() -> None:
    setup_logging()

    parser = ArgumentParser(description='Extract the voice from the audio and transcribe it into text to find out what is being said')
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    subparser = subparsers.add_parser('guess', help='Extract the voice and transcribe it.')
    subparser.add_argument('--input', type=str, required=True, help="Path to the audio file")
    subparser.add_argument('--language_code', type=str, required=True, help="The BCP-47 code of the language spoken in the audio. See the "
                                                                            "table at https://cloud.google.com/speech-to-text/docs/"
                                                                            "languages for all available codes.")
    subparser.add_argument('--model', type=str, choices=['command_and_search', 'phone_call', 'video', 'medical_dictation',
                                                         'medical_conversation', 'default'], required=True, help="The type of "
                                                                                                                 "transcription model to "
                                                                                                                 "use. For more details on "
                                                                                                                 "each model see the table "
                                                                                                                 "at https://cloud.google."
                                                                                                                 "com/speech-to-text/docs/"
                                                                                                                 "transcription-model#"
                                                                                                                 "speech_transcribe_model_"
                                                                                                                 "selection-python.")

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
        language_code = arguments.language_code
        model = arguments.model
        guesser_handler(input_folder, language_code, model)
    else:
        logger.error(f"Command {command} is not recognised")


def guesser_handler(input_folder: str, language_code: str, model: str) -> None:
    input_path = Path(input_folder).absolute()
    guess_text(input_path, language_code, model)


if __name__ == '__main__':
    main()
