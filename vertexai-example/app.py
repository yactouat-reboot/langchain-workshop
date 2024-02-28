from dotenv import load_dotenv
load_dotenv()

import os
import sys

from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate

# using the latest model from Google
model = VertexAI(model_name="gemini-pro")

# code generation example: let's start with a Docker Compose file
llm = VertexAI(model_name="code-bison", max_output_tokens=1000, temperature=0.3)
docker_compose_prompt_template = """Write the docker compose file for {application_description}.
Choose the best technology stack for this specific application.
DO NOT add formatting, such as backticks, in your answer. Just output the code.
I should be able to copy-paste it in a docker-compose.yml file and run it with `docker-compose up`."""
docker_compose_prompt = docker_compose_prompt_template.format(
    application_description="a web application to manage recipes",
)
docker_compose_res = model.invoke(docker_compose_prompt)
# print(docker_compose_res)
# write the result to a file
with open('./out/docker-compose.yml', 'w') as f:
    f.write(docker_compose_res)