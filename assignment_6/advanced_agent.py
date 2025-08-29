# advanced_support_agent.py

import datetime

# Guardrail Function
def check_guardrails(query: str) -> bool:
    offensive_words = ["angry", "worst", "bad", "refund", "hate", "complaint"]
    return any(word in query.lower() for word in offensive_words)

# Logging Function
def log_event(event: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[LOG {timestamp}] {event}")

# Tool 1: FAQ Handler
def faq_tool(query: str) -> str:
    log_event(f"faq_tool called with query='{query}'")
    faqs = {
        "return policy": "You can return products within 30 days.",
        "shipping time": "Shipping usually takes 3–5 business days.",
        "payment methods": "We accept credit cards, PayPal, and bank transfers."
    }
    for key in faqs:
        if key in query.lower():
            return faqs[key]
    return "Sorry, I couldn't find an answer to that FAQ."

# Tool 2: Order Status
def order_status(order_id: str) -> str:
    log_event(f"order_status called with order_id='{order_id}'")
    return f"Order {order_id} is out for delivery and will arrive tomorrow."

# Tool 3: Order Lookup
def order_lookup(order_id: str) -> str:
    log_event(f"order_lookup called with order_id='{order_id}'")
    return f"Order {order_id} contains: 1x T-shirt, 2x Jeans, Total: $89.99"

# Agent Class
class AdvancedSupportAgent:
    def __init__(self, customer_id: str):
        self.order_id = "ORD123"
        self.customer_id = customer_id
        self.tool_choice = "auto" 

    def process(self, query: str) -> str:
        log_event(f"Processing query='{query}' with customer_id='{self.customer_id}'")

        # Guardrail check
        if check_guardrails(query):
            log_event("Guardrail triggered — offensive or negative sentiment detected")
            return "Please keep the conversation respectful. I'm here to help."

        # Escalation logic
        if "human" in query.lower() or "not helpful" in query.lower():
            log_event("Escalation triggered — handing off to human agent")
            return "I'm escalating this to a human support agent. Please hold..."

        # Tool routing (auto mode)
        if "order status" in query.lower():
            return order_status(self.order_id)
        elif "order details" in query.lower() or "cart" in query.lower():
            return order_lookup(self.order_id)
        elif any(keyword in query.lower() for keyword in ["return", "shipping", "payment"]):
            return faq_tool(query)

        return "I'm not sure how to help with that. Can you rephrase?"

# Test Queries
if __name__ == "__main__":
    agent = AdvancedSupportAgent(customer_id="CUST789")
    queries = [
        "What is your return policy?",
        "Check my order status",
        "Show me order details",
        "I'm really angry about this product",
        "What payment methods do you accept?",
        "I want to talk to a human",
        "Tell me about shipping time",
        "My cart is missing items",
        "This is the worst experience ever"
    ]

    for q in queries:
        print(f"User: {q}")
        print(f"Bot: {agent.process(q)}\n")
