from openai import OpenAI
import os
import time
import re


class AppChatGPT:
    def __init__(self):
        self.model = None
        self.initialize()

    def initialize(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def validate_prompt(self, prompt):
        if not prompt:
            raise ValueError("Prompt cannot be empty.")

        if len(prompt) > 1000:
            raise ValueError(
                "Prompt is too long. Please keep it under 1000 characters."
            )

        if re.search(r"[^\w\s]", prompt):
            raise ValueError(
                "Prompt contains special characters. Please avoid using special characters."
            )

        if not prompt.strip():
            raise ValueError("Prompt cannot be empty after removing whitespace.")

        return True

    def prepare_system_message(self, prompt):
        message = "You are a helpful assistant for students, professors, people want to know about srh university, you should answer their queries and give them the best possible answer."
        return {"role": "system", "content": message}

    def generate_response(self, prompt):
        if not self.model:
            self.initialize()

        if not self.validate_prompt(prompt):
            return None

        start_time = time.time()
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        end_time = time.time()
        response_time = round(end_time - start_time, 2)

        print(f"Response Time: {response_time} seconds")
        print(completion.choices[0].message.content)

        return {
            "content": completion.choices[0].message.content,
            "response_time": response_time,
        }
