import requests
from openai import OpenAI
from config import Config


class Model:
    def __init__(self) -> None:
        self.__config = Config()
        self.__client = OpenAI(api_key=self.__config.api_key)

    def create_thread(self, content):
        thread = self.__client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ]
        )
        return thread

    def send_message(self, question, thread_id):
        return self.__client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=question
        )

    def get_messages(self, thread_id, assistant):
        run = self.__client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=assistant.id
        )

        if run.status == 'completed':
            messages = self.__client.beta.threads.messages.list(
                thread_id=thread_id)

            formatted_messages = []
            for message in messages.data:
                if message.content:
                    for content_block in message.content:
                        if content_block.type == 'text' and hasattr(content_block, 'text'):
                            formatted_messages.append(content_block.text.value)
            return formatted_messages

    def delete_thread(self, thread_id):
        self.__client.beta.threads.delete(thread_id=thread_id)
