from dotenv import load_dotenv
load_dotenv()

import os
import sys

from langchain_google_vertexai import VertexAI

# using the latest model from Google
model = VertexAI(model_name="gemini-pro")

# sending one question to the model
question = "are you better than GPT-4?"
# res = model.invoke(question)
# print(res)

print("\n")

# sending multiple questions to the model
question2 = "what is the future of multimodality?"
# res = model.batch([question, question2])
# print(res)

# showing the generations from the question
result = model.generate([question])
# this will show an array of possible answers from the bot and their metadata
res = result.generations
print(res)