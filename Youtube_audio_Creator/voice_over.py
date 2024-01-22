import elevenlabs

class TextToSpeech:
    def __init__(self, api_key):
        self.api_key = api_key
        elevenlabs.set_api_key(self.api_key)

    def create_voice(self, voice_id, stability=0, similarity_boost=0.75):
        voice_settings = elevenlabs.VoiceSettings(
            stability=stability,
            similarity_boost=similarity_boost
        )
        voice = elevenlabs.Voice(
            voice_id=voice_id,
            settings=voice_settings
        )
        return voice

    def generate_speech(self, text, voice_id):
        voice = self.create_voice(voice_id)
        audio = elevenlabs.generate(text=text, voice=voice)
        return audio

    def save_audio(self, audio, filename):
        elevenlabs.save(audio, filename)

