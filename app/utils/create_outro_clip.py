import os
import elevenlabs

from dotenv import load_dotenv
from elevenlabs import Voice, VoiceSettings
from elevenlabs.client import ElevenLabs

def main():
    """Creates voice-over text-to-speech (TTS) audio files and subtitles."""
    load_dotenv()
    eleven_labs_api_key = os.environ.get("ELEVEN_LABS_API_KEY")
    client = ElevenLabs(api_key=eleven_labs_api_key)
    
    tts_file_name = f'outro_audio.mp3' 
    tts_audio = client.generate(
        text="Head to the nicks dot news website for more!", 
        voice=Voice(
            voice_id='yeNojDSkqjMLki231UWs',
            settings=VoiceSettings(stability=0.5, similarity_boost=0.75)
        ),
        model="eleven_turbo_v2"
    )
    elevenlabs.save(tts_audio, tts_file_name)

if __name__ == "__main__":
    main()