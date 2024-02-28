# LangChain workshop

## setting up LangChain + first interaction

```python
from langchain_openai import ChatOpenAI

# we create an instance of Chat-GPT programmatically
chat_gpt = ChatOpenAI()

res = chat_gpt.invoke("what is LangChain and what can I do with it?")
print(res)
```

... we have a classic case of LLM hallucination here with out first response =>

```python
content='LangChain is a blockchain platform that focuses on providing solutions for language learning and education. It aims to offer a decentralized marketplace for language services, such as online tutoring, translation services, and language content creation.\n\nWith LangChain, users can access a wide range of language learning resources, connect with language tutors and experts, and engage in language exchange programs. Users can also earn rewards and incentives for participating in the platform, such as tokens that can be used to pay for services or exchanged for other cryptocurrencies.\n\nOverall, LangChain offers a decentralized and secure platform for language enthusiasts to improve their language skills, connect with other learners and instructors, and potentially earn rewards for their participation.'
```

LangChain is not a blockchain platform ! What happened here is that the LLM does not have LangChain docs into his knowledge base (the things it knows) so it tries to generate a response based on the input it received.

## The goal of our program

We want to create an agent that is able to look into the web IF he does not know something to reduce hallucinations:

- user asks a question
- LLM verifies if it has the information in its knowledge base (self-ask technique)
- if not, we crawl the wbe to find the answer