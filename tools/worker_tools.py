from langchain.tools import tool

@tool
def analyze_numbers(data: str) -> str:
    """Analyze comma separated numbers"""
    nums = [int(x.strip()) for x in data.split(",")]
    mean = sum(nums) / len(nums)
    return f"Mean={mean}, Max={max(nums)}, Min={min(nums)}"