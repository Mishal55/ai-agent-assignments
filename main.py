
from assignment_7.webSearch import web_search_tool


def run_agent():
    print("🤖 Tavily Web Search Agent")
    query = input("🔍 Enter your search query: ")
    print("\n📡 Searching...\n")
    result = web_search_tool(query)
    print("✅ Results:\n")
    print(result)

if __name__ == "__main__":
    run_agent()
