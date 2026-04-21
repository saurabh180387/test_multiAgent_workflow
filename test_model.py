from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(model="gemini-pro")

# print(llm.invoke("Hello").content)

import google.generativeai as genai
import os

genai.configure(api_key="********************")

print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
