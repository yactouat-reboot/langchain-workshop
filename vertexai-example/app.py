from dotenv import load_dotenv
load_dotenv()

import os
import sys

from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate

# using the latest model from Google
model = VertexAI(model_name="gemini-pro")

# getting application description from the command line arg
application_description = sys.argv[1]

# code generation: let's start with a Docker Compose file
print("Generating a Docker Compose...")
docker_compose_prompt_template = """Write the docker compose file for {application_description}.
Choose the best technology stack for this specific application.
DO NOT add formatting, such as backticks, in your answer. Just output the code.
I should be able to copy-paste it in a docker-compose.yml file and run it with `docker-compose up`."""
docker_compose_prompt = docker_compose_prompt_template.format(
    application_description=application_description,
)
docker_compose_res = model.invoke(docker_compose_prompt)
# print(docker_compose_res)
# write the result to a file
with open('./out/docker-compose.yml', 'w') as f:
    f.write(docker_compose_res)

# code generation: with a Docker Compose file, write the application service Dockerfile
print("Generating a Dockerfile...")
dockerfile_prompt_template = """You are a software developer.
Write the Dockerfile for the application service that is described in the Docker Compose file below, delimited with dashes.
---
{docker_compose}
---
DO NOT add formatting, such as backticks, in your answer. Just output the code.
I should be able to copy-paste your output in a Dockerfile and build the image it with `docker build -t myimage .`
Add comments in the output Dockerfile explaining your choices and your code."""
dockerfile_prompt = dockerfile_prompt_template.format(
    docker_compose=docker_compose_res,
)
dockerfile_res = model.invoke(dockerfile_prompt)
# print(dockerfile_res)
# write the result to a file
with open('./out/Dockerfile', 'w') as f:
    f.write(dockerfile_res)