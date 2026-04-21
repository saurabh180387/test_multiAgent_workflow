# def route_query(user_input):
#     if "analyze" in user_input.lower():
#         return "worker"
#     if "time" in user_input.lower():
#         return "time"
#     return "llm"



# if __name__ == "__main__":
#     print("Ask either:")
#     print("1. Time query (e.g., 'What is the time in Bangalore?')")
#     print("2. Data analysis (e.g., 'Analyze 10,20,30')\n")
#     print("Type 'exit' or 'quit' to quit.\n")

#     while True:
#         user_input = input("User: ")

#         # Exit condition
#         if user_input.lower() in ["exit", "quit"]:
#             print("Exiting...")
#             break

#         try:
#             result = orchestrator_agent.invoke({
#                 "messages": [("user", user_input)]
#             })

#             print("Response:", result["messages"][-1].content)

#         except Exception as e:
#             print("Error:", str(e))

from agents.orchestrator_agent import orchestrator_agent
from tools.simple_tool import get_time_info
from agents.orchestrator_agent import worker_agent_tool


def route_query(user_input: str):
    text = user_input.lower()

    if "time" in text:
        return "time"
    elif "analyze" in text or any(char.isdigit() for char in text):
        return "worker"
    else:
        return "llm"


if __name__ == "__main__":
    print("Ask either:")
    print("1. Time query (e.g., 'What is the time in Bangalore?')")
    print("2. Data analysis (e.g., 'Analyze 10,20,30')")
    print("\nType 'exit' or 'quit' to quit.\n")

    while True:
        user_input = input("User: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        try:
            route = route_query(user_input)

            # 🔹 Route execution
            if route == "time":
                print("[Routing → Time Tool]")
                response = get_time_info.invoke(user_input)

            elif route == "worker":
                print("[Routing → Worker Agent]")
                response = worker_agent_tool.invoke(user_input)

            else:
                print("[Routing → Orchestrator Agent]")
                result = orchestrator_agent.invoke({
                    "messages": [("user", user_input)]
                })
                response = result["messages"][-1].content

            print("Response:", response)

        except Exception as e:
            print("Error:", str(e))