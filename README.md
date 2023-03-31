# TerminalGPT

TerminalGPT is a Python script that enables users to interact with the GPT-4 language model through a terminal interface. This script uses the OpenAI API to generate responses to prompts provided by the user.

## Prerequisites

Before running this script, you need to have the following:

-   An OpenAI API key: You can obtain an API key by signing up for the OpenAI API at https://beta.openai.com/signup/.
-   Python 3 installed on your machine.
-   The `dotenv` Python package installed.

## Installation

1. Clone this repository to your local machine.
2. Create a `.env` file in the root directory of the repository.
3. Add your OpenAI API key to the `.env` file as follows: `OPENAI_API_KEY=your-api-key-here`.
4. Install the required packages by running `pip install -r requirements.txt`.
5. Specify a working chat model name in `app.y` on line `10`, that is eligible with your openai key.

## Usage

To use TerminalGPT, navigate to the directory where you cloned the repository and run the following command:

This will launch the script, and you will be prompted to enter text. Type your prompt and press enter to receive a response from GPT-4.

The first message will ask for you to set the chat setting - the default is general
This setting helps nudge the chat bot in a better direction for giving the user their desired generation

To exit the script, type "quit" and press enter.
