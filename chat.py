import openai
import os
import time
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = 'gpt-4'


# process user input
def process_input(user_input):
    return user_input.strip()


# format prompt
def format_prompt(prompt):
    return f"User: {prompt}\nGPT-4: "


# send request to OpenAI
@lru_cache(maxsize=128)
def send_request(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {'role': 'system',
                'content': 'You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.'},
            {'role': 'user', 'content': 'Prompt: ' + prompt},
            {'role': 'assistant', 'content': ''},
        ],
        temperature=0.6,
        max_tokens=500,
    )
    return response['choices'][0]['message']['content']


# generate response
def generate_response(prompt):
    prompt = format_prompt(prompt)
    start_time = time.time()
    response = send_request(prompt)
    response_time = time.time() - start_time
    return response, response_time


# handle user input
def handle_input(user_input):
    if user_input.lower() == "quit":
        return None
    processed_input = process_input(user_input)
    return processed_input


def main():
    print("Welcome to TerminalGPT (Powered by GPT-4)! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        prompt = handle_input(user_input)
        if prompt is None:
            break
        response, response_time = generate_response(prompt)
        print(f"GPT-4 (finished in {response_time:.2f} seconds): {response}\n")


if __name__ == "__main__":
    main()
