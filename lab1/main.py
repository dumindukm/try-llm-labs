import os
import base64
from openai import AzureOpenAI
from IPython.display import Markdown, display
from dotenv import load_dotenv



class AzureOpenAIChat:
    def __init__(self):
        self.endpoint = os.getenv("ENDPOINT_URL", "https://az-openai.azure.com/")
        self.deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1")
        self.subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")
        self.client = AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.subscription_key,
            api_version="2025-01-01-preview",
        )
        self.chat_prompt = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant that helps people find information. Response content with Markdown language"
                    }
                ]
            }
        ]

    def create_user_prompt(self, prompt):
        return {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }

    def update_system_prompt(self, prompt):
        self.chat_prompt.append( {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        })

    def message_for_prompt(self, prompt):
        self.chat_prompt.append(prompt)
        return self.chat_prompt

    def call_completion(self, user_prompt):
        prompt = self.create_user_prompt(user_prompt)
        messages = self.message_for_prompt(prompt)
        completion = self.client.chat.completions.create(
            model=self.deployment,
            messages=messages,
            max_tokens=800,
            temperature=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
        )
        # print(completion.to_json())
        print(completion.choices[0].message.content)
        self.update_system_prompt(completion.choices[0].message.content)
        print(completion.choices[0].message.content)


if __name__ == "__main__":
    load_dotenv(override=True)
    print("Hello from lab1!")
    chat = AzureOpenAIChat()
    chat.call_completion("soccer vs football")
    chat.call_completion("how many player per each ?")
