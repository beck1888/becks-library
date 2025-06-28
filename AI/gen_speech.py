from openai import OpenAI
from pathlib import Path
import uuid
import playsound
import os

"""
Generate audio using the OpenAI TTS API and speaks it out loud.

Parameters:
text (str): The text to be spoken.
voice (str): The name of the voice to use. Defaults to "onyx".
wait_for_speech_to_stop (bool): Whether to wait for the speech to stop. Defaults to True.
clean_up (bool): Whether to clean up the temporary audio file. Defaults to True.

Returns:
str: The path to the temporary audio file (if applicable).
"""

def say(text, openai_api_key: str, voice="onyx", wait_for_speech_to_stop=True, clean_up=True) -> str:
    # Initialize the OpenAI API client
    client = OpenAI(api_key=openai_api_key)

    # Structure the request
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text,
    )

    # Create the cache directory if it doesn't exist
    if not os.path.exists(Path(__file__).parent / "cache"):
        os.makedirs(Path(__file__).parent / "cache")

    # Save the audio file
    file_name = speech_file_path = Path(__file__).parent / "cache" / f"{uuid.uuid4()}.mp3"
    response.write_to_file(speech_file_path)

    # Play the audio file
    playsound.playsound(speech_file_path, block=wait_for_speech_to_stop)

    # Clean up
    if clean_up:
        os.remove(speech_file_path)

        # If the cache directory is empty, delete it
        if not os.listdir(Path(__file__).parent / "cache"):
            os.rmdir(Path(__file__).parent / "cache")

        return None
    else:
        return speech_file_path
