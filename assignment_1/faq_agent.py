# faq_agent.py

class FAQAgent:
    def __init__(self):
        self.faqs = {
            "what is your name": "I'm your friendly FAQ bot 🤖.",
            "what do you do": "I answer common questions to help users quickly.",
            "how can i contact support": "You can email support@example.com.",
            "what are your working hours": "We operate Monday to Friday, 9am to 5pm."
        }

    def process(self, query: str) -> str:
        normalized = query.strip().lower()
        return self.faqs.get(normalized, "Sorry, I don't have an answer for that.")

if __name__ == "__main__":
    agent = FAQAgent()
    queries = [
        "What is your name",
        "How can I contact support",
        "Do you offer refunds?"
    ]
    for q in queries:
        print(f"User: {q}")
        print(f"Agent: {agent.process(q)}\n")
