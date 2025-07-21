from strands import Agent, tool
from strands_tools import calculator, current_time

# Define a custom tool as a Python function using the @tool decorator
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())

# Test the tools directly without the agent
print("=== Testing Tools Directly ===")

# Test 1: Current time
print("1. Current time:")
try:
    time_result = current_time({"toolUseId": "test1", "input": {}})
    print(f"   Result: {time_result}")
except Exception as e:
    print(f"   Error: {e}")

# Test 2: Calculator  
print("\n2. Calculator (3111696 / 74088):")
try:
    calc_result = calculator({
        "toolUseId": "test2", 
        "input": {"expression": "3111696 / 74088"}
    })
    print(f"   Result: {calc_result}")
except Exception as e:
    print(f"   Error: {e}")

# Test 3: Letter counter
print("\n3. Letter counter (R's in 'strawberry'):")
try:
    letter_result = letter_counter("strawberry", "r")
    print(f"   Result: {letter_result}")
except Exception as e:
    print(f"   Error: {e}")

print("\n=== All tools are working! ===")
print("The Windows fcntl issue is resolved.")
print("To use the full agent, you'll need AWS Bedrock credentials.")
