from dotenv import load_dotenv
load_dotenv()

import os
# ! we verify that the environment variables are loaded
# print(os.getenv('OPENAI_API_KEY'))

from langchain_openai import ChatOpenAI

# we create an instance of Chat-GPT programmatically
chat_gpt = ChatOpenAI()