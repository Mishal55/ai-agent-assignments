import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPEN_ROUTER_API_KEY")
model_name = "openrouter/mistral-7b"
# Input guardrail: allow only math-related queries
def input_guardrail(user_input: str) -> bool:
    allowed_keywords = ["calculate", "add", "subtract", "multiply", "divide", "math", "+", "-", "*", "/"]
    return any(keyword in user_input.lower() for keyword in allowed_keywords)

# Output guardrail: block political content
def output_guardrail(response: str) -> str:
    blocked_keywords = ["president", "prime minister", "politics", "election", "government", "senator", "minister"]
    if any(keyword in response.lower() for keyword in blocked_keywords):
        return "🚫 This topic is restricted. Please ask something else."
    return response

# Agent-like function using OpenRouter API
def run_guarded_agent(user_input: str) -> str:
    if not input_guardrail(user_input):
        return "🚫 Only math-related queries are allowed."

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant. Avoid political topics."},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        raw_output = response.json()["choices"][0]["message"]["content"]
        return output_guardrail(raw_output)

    except Exception as e:
        return f"❌ Agent error: {str(e)}"

# CLI execution
def main():
    print("🤖 Guarded Math Agent (OpenRouter)")
    while True:
        user_input = input("🗣️ You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        result = run_guarded_agent(user_input)
        print(f"💬 Agent: {result}")

if __name__ == "__main__":
    main()
