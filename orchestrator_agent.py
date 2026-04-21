# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent # type: ignore
from tools.simple_tool import get_time_info
from agents.worker_agent import worker_agent


llm = ChatGoogleGenerativeAI(
    model="gemini-pro",   # fast + free tier friendly
    temperature=0
)

@tool
def worker_agent_tool(query: str) -> str:
    """Delegate work to worker agent"""
    result = worker_agent.invoke({
        "messages": [("user", query)]
    })
    return result["messages"][-1].content

orchestrator_tools = [
    get_time_info,
    worker_agent_tool
]

def orchestrator_prompt(state):
    return {
        "messages": [
            ("system", """You are an orchestrator agent.

STRICT RULES:
- You MUST choose the correct tool.
- Do NOT answer directly if a tool is relevant.
- Use get_time_info for time queries.
- Use worker_agent_tool for data analysis.

Always prefer tool usage over direct answers.
""")
        ] + state["messages"]
    }

# orchestrator_agent = create_react_agent(
#     llm,
#     orchestrator_tools,
#     state_modifier=orchestrator_prompt
# )


orchestrator_agent = create_react_agent(
    llm,
    orchestrator_tools,
    prompt="""
You are an orchestrator agent.

STRICT RULES:
- You MUST choose the correct tool.
- Do NOT answer directly if a tool is relevant.
- Use get_time_info for time-related queries.
- Use worker_agent_tool for data analysis queries.

Always prefer tool usage over direct answers.
"""
)