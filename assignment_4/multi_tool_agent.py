# multi_tool_agent.py

import re

# Tool 1: Math function
def add(a: int, b: int) -> int:
    return a + b

# Tool 2: Weather function (mocked)
def get_weather(city: str) -> str:
    mock_data = {
        "Karachi": "32°C, sunny",
        "Lahore": "30°C, partly cloudy",
        "Islamabad": "28°C, rainy",
        "New York": "22°C, windy",
        "Tokyo": "26°C, humid"
    }
    return mock_data.get(city, "Weather data not available for this city.")

# Agent class
class MultiToolAgent:
    def process(self, query: str) -> str:
        # Check for math query
        math_match = re.search(r'(\d+)\s*\+\s*(\d+)', query)
        if math_match:
            a = int(math_match.group(1))
            b = int(math_match.group(2))
            result = add(a, b)
            return f"The result of {a} + {b} is {result}."

        # Check for weather query
        for city in ["Karachi", "Lahore", "Islamabad", "New York", "Tokyo"]:
            if city.lower() in query.lower():
                weather = get_weather(city)
                return f"The weather in {city} is {weather}."

        return "Sorry, I can only help with addition or weather questions for known cities."

# Test cases
if __name__ == "__main__":
    agent = MultiToolAgent()
    queries = [
        "What's the weather in Karachi?",
        "Tell me about Lahore weather.",
        "What is 12 + 8?",
        "Add 100 + 250",
        "Is it raining in Islamabad?",
        "How's the weather in Tokyo?",
        "Can you calculate 5 + 7?"
    ]

    for q in queries:
        print(f"User: {q}")
        print(f"Agent: {agent.process(q)}\n")
