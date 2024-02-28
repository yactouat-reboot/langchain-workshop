from dotenv import load_dotenv
load_dotenv()

import os
import sys
# ! we verify that the environment variables are loaded
# print(os.getenv('OPENAI_API_KEY'))

from duckduckgo_search import DDGS
from langchain_openai import ChatOpenAI
# this import allows us to format prompts with variables
from langchain.prompts import PromptTemplate

from prompts import (
    answer_to_question_with_text_prompt_template,
    control_prompt_template,
    formatting_prompt_template
)

# we create an instance of Chat-GPT programmatically
chat_gpt = ChatOpenAI()

# we get the question from the command line
question = sys.argv[1]

# we check if the bot knows the answer to the question
knowledge_base_prompt = PromptTemplate.from_template(control_prompt_template)
control_prompt = knowledge_base_prompt.format(question=question)
knowledge_base_answer = chat_gpt.invoke(control_prompt)

# we format the answer in a JSON object
formatting_prompt = PromptTemplate.from_template(formatting_prompt_template)
formatting_response = chat_gpt.invoke(formatting_prompt.format(
    question=question,
    answer=knowledge_base_answer
))

if (formatting_response.content == "True"):
    # we display the raw bot answer
    print(knowledge_base_answer)
else:
    # when the bot does not know the answer, we trigger a web search with DuckDuckGo
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(question, safesearch='moderate', timelimit='y', max_results=8)]
        # we get all the `title` and the `body` of the results into a single text
        body_title_aggregate = "\n\n".join([f"\n---{r['title']}\n{r['body']}\n---" for r in results])
        answer_to_question_prompt_template = PromptTemplate.from_template(answer_to_question_with_text_prompt_template)
        answer_to_question_response = chat_gpt.invoke(answer_to_question_prompt_template.format(
            question=question,
            input_text=body_title_aggregate
        ))
        print(answer_to_question_response.content)

# TODO display all the results in a web page or another nice format