from langchain.tools import tool
from  datetime import datetime
@tool
def get_time_info(city: str) -> str:
    """Return mocked time info"""
    return f"Time in {city} is {datetime.now()}"