# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Tuple

from google.auth.credentials import Credentials
from google.cloud import speech, storage
from google.oauth2 import service_account

from resources.properties import GOOGLE_APPLICATION_CREDENTIALS, BUCKET_NAME
from src.logger import logger


def extract_text_from_voice(audio_path: Path) -> None:
    logger.info("Extracting text from speech")

    audio_name, voice_folder = get_values(audio_path)
    wav_file = Path(voice_folder).joinpath("vocals.wav").__str__()

    credentials = get_credentials()
    upload_blob(credentials, BUCKET_NAME, wav_file, audio_name)
    transcription = transcript_audio(credentials, BUCKET_NAME, audio_name, 300)
    delete_blob(credentials, BUCKET_NAME, audio_name)

    print(transcription)


def get_values(audio_path: Path) -> Tuple[str, str]:
    audio_name = audio_path.stem
    suffix_length = len(audio_path.suffix)
    voice_folder = audio_path.__str__()[:-suffix_length]

    return audio_name, voice_folder


def transcript_audio(credentials: Credentials, bucket_name: str, audio_name: str, timeout: int) -> str:
    logger.info(f"Transcribing the audio file, please wait for operation to complete. Actual timeout time: {timeout} seconds(s)")

    client = speech.SpeechClient(credentials=credentials)
    gcs_uri = f"gs://{bucket_name}/{audio_name}"

    audio = speech.RecognitionAudio({"uri": gcs_uri})
    config = speech.RecognitionConfig({
        "encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16,
        "audio_channel_count": 2,
        "enable_separate_recognition_per_channel": True,
        "language_code": "en-US"}
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=timeout)

    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription


def get_credentials() -> Credentials:
    logger.info("Loading Google Application Credentials")

    credentials_file = Path(__file__).absolute().parent.parent.joinpath("resources").joinpath(GOOGLE_APPLICATION_CREDENTIALS).__str__()
    credentials = service_account.Credentials.from_service_account_file(credentials_file)

    return credentials


def upload_blob(credentials: Credentials, bucket_name: str, wav_file: str, destination_blob_name: str):
    logger.info("Uploading wav file to Google Cloud Storage")

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(wav_file)


def delete_blob(credentials: Credentials, bucket_name: str, blob_name: str):
    logger.info("Deleting wav file from Google Cloud Storage")

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()


def write_transcriptions(transcriptions: str, output_file: str):
    logger.info("Writing the transcripts from the wav file")
