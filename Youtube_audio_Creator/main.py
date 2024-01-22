
from chatGPT import OpenAIHelper
from voice_over import TextToSpeech
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(".env")

def main():
    openAI_API_Key = os.getenv('OPENAI_API_KEY')
    elevenlabs_API_Key = os.getenv('ELEVENLABS_API_KEY')
    voice_id = os.getenv('VOICE_ID')

    if not openAI_API_Key or not elevenlabs_API_Key:
        print("API keys are not set. Please set OPENAI_API_KEY and ELEVENLABS_API_KEY in your environment.")
        return

    openai_helper = OpenAIHelper(openAI_API_Key)
    tts = TextToSpeech(elevenlabs_API_Key)

    order = input("What kind of story would you like to have?")
    chat_result = openai_helper.chat_completion(order)
    if chat_result['status'] == 1:
        print("Generated content:", chat_result['response'])
        audio = tts.generate_speech(chat_result['response'], voice_id)
        tts.save_audio(audio, 'output.mp3')
    else:
        print("Failed to generate content:", chat_result['response'])

if __name__ == "__main__":
    main()
