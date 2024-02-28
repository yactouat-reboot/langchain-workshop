from dotenv import load_dotenv
load_dotenv()

import os
# ! we verify that the environment variables are loaded
# print(os.getenv('OPENAI_API_KEY'))

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


# we create an instance of Chat-GPT programmatically
chat_gpt = ChatOpenAI()
control_prompt_template = """Do you have the answer to the question below, delimited by dashes, in your knowledge base? 
-----------------------------------
{question}
-----------------------------------
If the answer is yes, give us your source.
If the source does not exist, then you don't know the answer.
"""
initial_prompt = "What is LangChain and what can I do with it?"

prompt = PromptTemplate.from_template(control_prompt_template)
control_prompt = prompt.format(question=initial_prompt)

res = chat_gpt.invoke(control_prompt)
print(res)