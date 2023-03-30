import openai
import time
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# record the time before the request is sent
start_time = time.time()


system_prompt = "You are codeGPT, a helpful coding assistant that thinks in steps and then thoughtfully writes clean code."
prompt = "write a python script that generates ASCII art in the terminal, randomely without an input image"

# send a ChatCompletion request to count to 100
response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': 'Prompt: ' + prompt},
        {'role': 'assistant', 'content': ''},
    ],
    temperature=0.5,
)

# calculate the time it took to receive the response
response_time = time.time() - start_time

# print the time delay and text received
print(f"Full response received {response_time:.2f} seconds after request")
print(f"Full response received:\n{response}")

reply = response['choices'][0]['message']
print(f"Extracted reply: \n{reply}")

reply_content = response['choices'][0]['message']['content']
print(f"Extracted content: \n{reply_content}")
