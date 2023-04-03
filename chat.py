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


def send_psych_writting_request(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{'role': 'system', 'content': 'You are psychGPT a cognitive psychology expert, who is also a great writter, you explain concepts back them up with sources.'},
                  {'role': 'user', 'content': 'Prompt: ' + prompt},
                  {'role': 'assistant', 'content': ''},
                  ],
        temperature=0.6,
    )
    return response['choices'][0]['message']['content']


# TODO: have user select the type of request to send on chat startup
@lru_cache(maxsize=128)
def send_create_request(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{'role': 'system', 'content': 'You are createGPT, a large language model trained by OpenAI. You are the epitome of a creative, you see the world in a unique way and can create anything you can imagine. Create the following prompt'},
                  {'role': 'user', 'content': 'Prompt: ' + prompt},
                  {'role': 'assistant', 'content': ''},
                  ],
        temperature=0.8,
    )
    return response['choices'][0]['message']['content']


@lru_cache(maxsize=128)
def send_translate_request(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {'role': 'system',
                'content': 'You are translateGPT, a large language model trained by OpenAI. You are an expert translator, and always translate the prompt into the target language. Translate the following prompt'},
            {'role': 'user', 'content': 'Prompt: ' + prompt},
            {'role': 'assistant', 'content': ''},
        ],
        temperature=0.4,
        # max_tokens=500,
    )
    return response['choices'][0]['message']['content']


@lru_cache(maxsize=128)
def send_summary_request(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {'role': 'system',
                'content': 'You are summaryGPT, a large language model trained by OpenAI. You are an expert summarizer, and always get the most important information. Summarize the following prompt'},
            {'role': 'user', 'content': 'Prompt: ' + prompt},
            {'role': 'assistant', 'content': ''},
        ],
        temperature=0.4,
        # max_tokens=500,
    )
    return response['choices'][0]['message']['content']


@lru_cache(maxsize=128)
def send_code_request(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {'role': 'system',
                'content': 'You are codeGPT, a helpful coding assistant that thinks in steps and then thoughtfully writes clean code, you also debug and improve code that is given to you.'},
            {'role': 'user', 'content': 'Prompt: ' + prompt},
            {'role': 'assistant', 'content': ''},
        ],
        temperature=0.5,
        # max_tokens=500,
    )
    return response['choices'][0]['message']['content']


# send request to OpenAI and cache the response
@lru_cache(maxsize=128)
def send_request(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {'role': 'system',
                'content': 'You are TerminalGPT, a large language model trained by OpenAI. Answer as concisely as possible.'},
            {'role': 'user', 'content': 'Prompt: ' + prompt},
            {'role': 'assistant', 'content': ''},
        ],
        temperature=0.6,
        # max_tokens=500,
    )
    return response['choices'][0]['message']['content']


# generate response
def generate_response(prompt, chat_type):
    prompt = format_prompt(prompt)

    # chat type request handling
    if chat_type == "create":
        start_time = time.time()
        response = send_create_request(prompt)
    elif chat_type == "translate":
        start_time = time.time()
        response = send_translate_request(prompt)
    elif chat_type == "summary":
        start_time = time.time()
        response = send_summary_request(prompt)
    elif chat_type == "code":
        start_time = time.time()
        response = send_code_request(prompt)
    elif chat_type == 'psych':
        start_time = time.time()
        response = send_psych_writting_request(prompt)
    else:
        start_time = time.time()
        response = send_request(prompt)

    # start_time = time.time()
    # response = send_request(prompt)
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
    chat_type = input(
        "What type of chat would you like to have? (create, translate, summary, code, psych, general): ")
    while True:
        user_input = input("You: ")
        prompt = handle_input(user_input)
        if prompt is None:
            break
        response, response_time = generate_response(prompt, chat_type)
        print(f"GPT-4 (finished in {response_time:.2f} seconds): {response}\n")


if __name__ == "__main__":
    main()
