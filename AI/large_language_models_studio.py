import lmstudio as lms

class LMStudio:
    def __init__(self, model_name: str, system_prompt: str, save_chat_history: bool = False):
        self.model = lms.llm(model_name)
        self.save_chat_history = save_chat_history
        self.messages = {
            'messages': [
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
        model = self.model
        save_chat_history = self.save_chat_history

        messages.append(
            {
                'role': 'user',
                'content': user_prompt
            }
        )

        response = model.respond({'messages': messages}).content

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
