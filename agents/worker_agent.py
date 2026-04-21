from langgraph.prebuilt import create_react_agent
from tools.worker_tools import analyze_numbers

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",   #"gemini-1.5-flash"
    temperature=0
)

worker_tools = [analyze_numbers]




# def worker_prompt(state):
#     return {
#         "messages": [
#             ("system", "You are a data analysis expert. Always use tools for calculations.")
#         ] + state["messages"]
#     }

worker_agent = create_react_agent(
    llm,
    worker_tools,
    prompt="You are a data analysis expert. Always use tools for calculations."   # ✅ function, not string
)