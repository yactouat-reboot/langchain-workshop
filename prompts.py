answer_to_question_with_text_prompt_template = """Your job is to answer questions with input text as a basis.
You are given a question in natural language, delimited by dashes below.
-----------------------------------
{question}
-----------------------------------
You are also given an input text, delimited by dashes below.
-----------------------------------
{input_text}
-----------------------------------
Use the input text to answer the question. If you can't answer the question, output "I don't know the answer".
"""

control_prompt_template = """Do you have the answer to the question below, delimited by dashes, in your knowledge base? 
-----------------------------------
{question}
-----------------------------------
If the answer is yes, give us your source."""

formatting_prompt_template = """You are a bot that always outputs True or False.
You are given a question in natural language, delimited by dashes below.
-----------------------------------
{question}
-----------------------------------
You are also given an answer in natural language, delimited by dashes below.
-----------------------------------
{answer}
-----------------------------------
You must output False if the answer says something like "I don't know the answer".
Only output the boolean, nothing else."""
