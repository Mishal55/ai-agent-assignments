
def get_weather(city: str) -> str:
    # Mocked weather data
    mock_data = {
        "Karachi": "32°C, sunny",
        "Lahore": "30°C, partly cloudy",
        "Islamabad": "28°C, rainy",
        "New York": "22°C, windy",
        "Tokyo": "26°C, humid"
    }
    return mock_data.get(city, "Weather data not available for this city.")

# Step 2: Tool that wraps the function
class WeatherTool:
    def fetch(self, city: str) -> str:
        return get_weather(city)

# Step 3: Agent that uses the tool
class WeatherAgent:
    def __init__(self):
        self.tool = WeatherTool()

    def process(self, query: str) -> str:
        # Basic city extraction from query
        for city in ["Karachi", "Lahore", "Islamabad", "New York", "Tokyo"]:
            if city.lower() in query.lower():
                weather = self.tool.fetch(city)
                return f"The weather in {city} is {weather}."
        return "Please ask about a known city like 'What's the weather in Karachi?'"

# Step 4: Test queries
if __name__ == "__main__":
    agent = WeatherAgent()
    queries = [
        "What's the weather in Karachi?",
        "Tell me about Lahore weather.",
        "Is it raining in Islamabad?",
        "Weather update for Tokyo?",
        "How's the weather in New York?"
    ]

    for q in queries:
        print(f"User: {q}")
        print(f"Agent: {agent.process(q)}\n")
