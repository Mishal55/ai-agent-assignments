# math_agent.py


import re


def add(a: int, b: int) -> int:
    return a + b

class MathAgent:
    def process(self, query: str) -> str:
        # Extract numbers from query using regex
        match = re.search(r'(\d+)\s*\+\s*(\d+)', query)
        if match:
            a = int(match.group(1))
            b = int(match.group(2))
            result = add(a, b)
            return f"The result of {a} + {b} is {result}."
        else:
            return "Sorry, I can only help with addition questions like 'What is 5 + 7'."

if __name__ == "__main__":
    agent = MathAgent()
    queries = [
        "What is 5 + 7?",
        "Can you add 12 + 8?",
        "Tell me the result of 100 + 250"
    ]

    for q in queries:
        print(f"User: {q}")
        print(f"Agent: {agent.process(q)}\n")
