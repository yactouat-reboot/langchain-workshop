# VertexAI x LangChain coding agent workshop

## we need to authenticate with Google Cloud 

To use VertexAI, we need:

- a GCP project
- a custom service account with a JSON key named `vertexai-sa.json` in the root of this project
- a role that can use VertexAI associated with the service account

The service account needs to have this role:

![service account role](./vertexai-role.png)

! PLEASE GIT IGNORE THE JSON KEY FILE !

## how to build an app programmatically

- we need an input application description, which is only a business perspective description of the app, no technical choices in the description
- we ask the LLM what steps are required to build the described application
- with the answer, ask what folder structure we need to create the application
- for each item of the project structure, ask the LLM the minimal code to run the application, even if it's just a hello world app'