import requests
import json
import os
import google.generativeai as genai
import time

API_KEY = os.getenv("OPENAPI_URL")
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)


class AI:

    def prepare_system_message(self):
        system_message = "You are a helpful assistant."
        # TODO: Add more system messages here

        return {"role": "system", "content": system_message}

    def prepare_user_message(self, prompt):
        return {
            "role": "user",
            "content": f"Now refer our database and answer this query: {prompt}",
        }

    def ask_gpt(self, prompt):
        try:
            start_time = time.time()
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
            end_time = time.time()
            response_time = round(end_time - start_time, 2)

            content = response.json()["choices"][0]["message"]["content"]
            return {"content": content, "response_time": response_time}

        except Exception as e:
            print(f"while calling openai: {e}")
            return None

    def ask_gemini(self, prompt):
        try:
            start_time = time.time()
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            end_time = time.time()
            response_time = round(end_time - start_time, 2)

            generated_text = response.text.strip()
            return {"content": generated_text, "response_time": response_time}

        except Exception as e:
            print(f"while calling gemini: {e}")
            return None
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)

            generated_text = response.text.strip()
            return generated_text

        except Exception as e:
            print(f"while calling gemini: {e}")
            return None
