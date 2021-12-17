# -*- coding: utf-8 -*-

from pathlib import Path

from modules.separator import separate_voice
from modules.speech import extract_text_from_voice
from src.logger import logger


def guess_text(input_path: Path) -> None:
    logger.info("Guessing the text of the audio")

    #separate_voice(input_path)
    extract_text_from_voice(input_path)
