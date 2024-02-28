# VertexAI x LangChain workshop

## we need to authenticate with Google Cloud 

To use VertexAI, we need:

- a GCP project
- a custom service account with a JSON key named `vertexai-sa.json` in the root of this project
- a role that can use VertexAI associated with the service account

The service account needs to have this role:

![service account role](./vertexai-role.png)

! PLEASE GIT IGNORE THE JSON KEY FILE !