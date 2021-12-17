# -*- coding: utf-8 -*-

from pathlib import Path

from spleeter.separator import Separator

from src.logger import logger


def separate_voice(source_path: Path) -> None:
    logger.info("Separating voice from other sounds")

    separator = Separator('spleeter:2stems-16kHz')
    source_file = str(source_path)
    output_folder = str(source_path.parent)
    separator.separate_to_file(source_file, output_folder)
