from dotenv import load_dotenv
load_dotenv()

import os
import pathlib
import sys

from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate

# using the latest model from Google
model = VertexAI(model_name="gemini-pro")

def human_in_the_loop(msg: str = "Do you want to proceed? (yes/no): ") -> bool:
    while True:
        confirmation = input(msg)
        if confirmation.lower() in ['yes', 'no']:
            return confirmation.lower() == 'yes'
        else:
            return False

def generate_folder_structure_script(application_description: str):
    # defining the architecture of our application
    print("Defining the architecture of our application...")
    application_initial_prompt_template = """You are a software architect.
    I want to build this application: {application_description}.
    What steps should I follow to create this application?
    You must chose the best technology stack for this specific application."""
    application_architecture_prompt = application_initial_prompt_template.format(
        application_description=application_description,
    )
    application_architecture_res = model.invoke(application_architecture_prompt)

    # create the folder structure of this application
    print("Generating the folder structure...")
    folder_structure_prompt_template = """You are a software developer.
    Given this architecture description below, delimited with dashes, create the folder structure for this application.
    ---
    {application_architecture_res}
    ---"""
    folder_structure_prompt = folder_structure_prompt_template.format(
        application_architecture_res=application_architecture_res,
    )
    folder_structure_res = model.invoke(folder_structure_prompt)
    # print(folder_structure_res)

    # write the Python script that creates the folder structure
    print("Writing the Python script that creates the folder structure...")
    folder_structure_generation_prompt_template = """You are a software developer.
    With this folder structure description below, delimited with dashes, write a Python script that creates the folder structure for this application.
    ---
    {folder_structure_res}
    ---
    The root of the project is the `out` folder, so all paths must start with this folder.
    DO NOT add formatting, such as backticks, in your answer. Just output the code.
    I should be able to run your output as is.
    """
    folder_structure_generation_prompt = folder_structure_generation_prompt_template.format(
        folder_structure_res=folder_structure_res,
    )
    folder_structure_generation_res = model.invoke(folder_structure_generation_prompt)
    with open('./out/scaffold.py', 'w') as f:
        f.write(folder_structure_generation_res.replace('```python', '').replace('```', ''))

def generate_docker_compose_from_folder_structure(folder_structure: str) -> str:
    docker_compose_prompt_template = """You are a software developer.
    Given this folder structure below, delimited with dashes, create a docker-compose file for this application.
    ---
    {folder_structure}
    ---"""
    docker_compose_prompt = docker_compose_prompt_template.format(
        folder_structure=folder_structure,
    )
    docker_compose_res = model.invoke(docker_compose_prompt)
    return docker_compose_res

if __name__ == "__main__":
    # if the `./out` directory does not exist, create it
    if not os.path.exists('./out'):
        os.makedirs('./out')

    # getting application description from the command line arg
    application_description = sys.argv[1]

    # listing the contents of the `./out` directory
    contents_of_out = list(pathlib.Path('./out').rglob("*"))
    # check if there any subfolders in the `./out` directory
    new_project = len(contents_of_out) <= 0

    if new_project:
        generate_folder_structure_script(application_description)

        # display the contents of the scripts in the terminal
        with open('./out/scaffold.py', 'r') as f:
            print(f.read())
        print("\n")
        
        # prompt the user for validation of the generated script
        if human_in_the_loop("are you happy with the contents of the ./out/scaffold.py file? (yes/no):"):
            # YOLO
            os.system('python ./out/scaffold.py')
        else:
            print("User denied. Exiting...")
            exit(1)
    
    docker_compose = generate_docker_compose_from_folder_structure(str(contents_of_out))
    # write the contents to a file
    with open('./out/docker-compose.yml', 'w') as f:
        f.write(docker_compose.replace('```yaml', '').replace('```', '').replace('./out/', ''))