import openai

class OpenAIHelper:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def chat_completion(self, prompt: str) -> dict:
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {
                        'role': 'system',
                        'content': '''
                        You are a content bot for Youtube Short's your duty is to create a writing that will maximum of reading 30 seconds it need to be real and engaging.
                        be sure the story is engaging and finishes in 30 second'''
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    },
                ])
            return {
                'status': 1,
                'response': response['choices'][0]['message']['content']
            }
        except Exception as e:
            return {'status': 0, 'response': str(e)}
