import requests
import json
import os



API_KEY = os.getenv("OPENAPI_URL")


class OpenRouter:

    def prepare_system_message(self):
        system_message = "You are a helpful assistant."
        # TODO: Add more system messages here

        return {"role": "system", "content": system_message}

    def prepare_user_message(self, prompt):
        return {
            "role": "user",
            "content": f"Now refer our database and answer this query: {prompt}",
        }

    def ask(self, prompt):
        print(f"prompt: {prompt}- {API_KEY}")

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                },
                data=json.dumps(
                    {
                        "model": "openai/gpt-3.5-turbo",
                        "messages": [
                            self.prepare_system_message(),
                            self.prepare_user_message(prompt),
                        ],
                    }
                ),
            )
            print(f"response: {response.json()}")
            return response.json()["choices"][0]["message"]["content"]

        except Exception as e:
            print(f"while  calling openai: {e}")
            return None

