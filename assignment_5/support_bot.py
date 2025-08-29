# customer_support_bot.py

def faq_tool(query: str) -> str:
    faqs = {
        "return policy": "You can return products within 30 days.",
        "shipping time": "Shipping usually takes 3–5 business days.",
        "payment methods": "We accept credit cards, PayPal, and bank transfers."
    }
    for key in faqs:
        if key in query.lower():
            return faqs[key]
    return "Sorry, I couldn't find an answer to that FAQ."

# Function Tool 2: Order Status
def order_status(order_id: str) -> str:
    return f"Order {order_id} is out for delivery and will arrive tomorrow."

# Function Tool 3: Order Lookup
def order_lookup(order_id: str) -> str:
    return f"Order {order_id} contains: 1x T-shirt, 2x Jeans, Total: $89.99"

# Main Bot Agent
class BotAgent:
    def __init__(self):
        self.order_id = "ORD123"  

    def process(self, query: str) -> str:
        # Escalation logic
        negative_keywords = ["angry", "bad", "worst", "refund", "complaint", "not happy"]
        if any(word in query.lower() for word in negative_keywords):
            return "I'm escalating this to a human support agent. Please hold..."

        # Order status
        if "order status" in query.lower():
            return order_status(self.order_id)

        # Order lookup
        if "order details" in query.lower() or "cart" in query.lower():
            return order_lookup(self.order_id)

        # FAQ handling
        faq_keywords = ["return", "shipping", "payment"]
        if any(keyword in query.lower() for keyword in faq_keywords):
            return faq_tool(query)

        return "I'm not sure how to help with that. Can you rephrase?"

# Test Queries
if __name__ == "__main__":
    agent = BotAgent()
    queries = [
        "What is your return policy?",
        "Check my order status",
        "Show me order details",
        "I'm really angry about this product",
        "What payment methods do you accept?",
        "Tell me about shipping time",
        "My cart is missing items",
        "I want a refund"
    ]

    for q in queries:
        print(f"User: {q}")
        print(f"Bot: {agent.process(q)}\n")
