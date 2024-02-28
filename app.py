from dotenv import load_dotenv
load_dotenv()

import os
# ! we verify that the environment variables are loaded
# print(os.getenv('OPENAI_API_KEY'))

from langchain_openai import ChatOpenAI
# this import allows us to format prompts with variables
from langchain.prompts import PromptTemplate

# we create an instance of Chat-GPT programmatically
chat_gpt = ChatOpenAI()
control_prompt_template = """Do you have the answer to the question below, delimited by dashes, in your knowledge base? 
-----------------------------------
{question}
-----------------------------------
If the answer is yes, give us your source."""

formatting_prompt_template = """You are given an answer in natural language, delimited by dashes below.
-----------------------------------
{answer}
-----------------------------------
Your job is to output a boolean from the answer:
- true, if the answer shows that the it knows the answer to the question, false otherwise."""

# initial_prompt = "What is LangChain and what can I do with it?"
initial_prompt = "What is the capital of France?"

# we check if the bot knows the answer to the question
knowledge_base_prompt = PromptTemplate.from_template(control_prompt_template)
control_prompt = knowledge_base_prompt.format(question=initial_prompt)
knowledge_base_answer = chat_gpt.invoke(control_prompt)

# we format the answer in a JSON object
formatting_prompt = PromptTemplate.from_template(formatting_prompt_template)
formatting_response = chat_gpt.invoke(formatting_prompt.format(answer=knowledge_base_answer))

if (bool(formatting_response.content)):
    print(knowledge_base_answer)
else:
    print("TODO make a web search to find the answer to the question.")