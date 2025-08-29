from tavilySearch import tavily_search

def web_search_tool(input_query: str) -> str:
    try:
        results = tavily_search(input_query)
        return "\n\n".join(results)
    except Exception as e:
        return f"Error: {str(e)}"
