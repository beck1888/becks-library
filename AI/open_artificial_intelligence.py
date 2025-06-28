from openai import OpenAI

class OpenArtificialIntelligence:
    def __init__(self, api_key: str, model_name: str, system_prompt: str, save_chat_history: bool = False):
        self.model_name = model_name
        self.client = OpenAI(
            api_key=api_key
        )

        self.save_chat_history = save_chat_history
        self.messages = {
            'messages': [ # The messages part is a relic from LMStudio
                {
                    'role': 'system',
                    'content': system_prompt
                }
            ]
        }

    def __str__(self) -> str:
        message_list = self.messages['messages']
        string_history = ''

        for message in message_list:
            string_history += f"{message['role']}: {message['content']}\n"


        return string_history


    def respond(self, user_prompt: str) -> str:
        messages = self.messages['messages']
        client = self.client
        model_name = self.model_name
        save_chat_history = self.save_chat_history

        messages.append(
            {
                'role': 'user',
                'content': user_prompt
            }
        )

        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            store=False
        ).choices[0].message.content

        if save_chat_history:
            messages.append(
                {
                    'role': 'assistant',
                    'content': response
                }
            )
            self.messages['messages'] = messages
        else:
            self.messages = {'messages': [messages[0]]}

        return response
