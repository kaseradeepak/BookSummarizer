# Use Case - Build a Multi Agent Customer Support System
# The system should be able to handle customer queries and involves multiple agents:
# Coordinator Agent, Order Agent, Refund Agent, Fraud Detection Agent, Verifier Agent, Shipping Agent, .....

# User Query - My order was delivered 7 days late, I want a refund.

# Expected behaviour:
# Order Agent should check the order status.
# Refund agent should check the refund status.
# Fraud Detection Agent reviews the request.
# Writer Agent generates a final reply to the customer.
# Verifier agent verifies the response quality.
from openai import OpenAI
import re

client = OpenAI()

LLM_MODEL = "gpt-5.4"

ORDER_DATABASE = {
    "ORD-123": {
        "order_id": "ORD-123",
        "customer_id": "CUST-777",
        "status": "delivered",
        "payment_status": "paid",
        "expected_delivery_days": 2,
        "actual_delivery_days": 6,
        "missing_items": ["USB-C Cable"],
        "order_amount": 1299,
        "currency": "INR"
    }
}

CUSTOMER_HISTORY_DATABASE = {
    "CUST-777": {
        "customer_id": "CUST-777",
        "refunds_last_30_days": 1,
        "account_age_days": 420,
        "is_flagged_customer": False
    }
}

REFUND_POLICY = """
Company Refund Policy:

1. If delivery is delayed by 3 or more days, the customer may be eligible for refund or compensation.
2. If an item is missing from the order, the missing item amount can be refunded.
3. If payment status is not 'paid', refund cannot be initiated.
4. If the customer has more than 5 refunds in the last 30 days, manual review is required.
5. If the customer is flagged for risk, manual review is required.
6. Never promise instant refund. Say that refund will be initiated after standard processing.
7. The final customer message must be polite, clear, and professional.
"""

def get_order_details(order_id):
    return ORDER_DATABASE.get(order_id)

def get_customer_history(customer_id):
    return CUSTOMER_HISTORY_DATABASE.get(customer_id)

# My order id ORD-765786578 is delayed, I want a refund.

def extract_order_id(user_query):
    match = re.search(r"ORD-\d+", user_query)

    if match:
        return match.group(0)

    print("Please give a valid order id the query")

# Output Schema
AGENT_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "agent_name": {
            "type": "string",
            "description": "Name of the agent producing this response."
        },
        "summary": {
            "type": "string",
            "description": "Clear summary of what the agent found or created."
        },
        "decision": {
            "type": "string",
            "description": "The main decision taken by the agent."
        },
        "confidence": {
            "type": "number",
            "description": "Confidence score between 0 and 1."
        },
        "next_step": {
            "type": "string",
            "description": "What should happen next."
        }
    },
    "required": [
        "agent_name",
        "summary",
        "decision",
        "confidence",
        "next_step"
    ],
    "additionalProperties": False
}

def run_llm_agent(agent_name, role_instruction, task_instruction):
    response = client.responses.create(
        model=LLM_MODEL,
        input=[
            {
                "role" : "system",
                "content" : role_instruction
            },
            {
                "role" : "user",
                "content" : task_instruction
            }
        ]
    )

    return response.output_text

# Coordinator Agent
def coordinator_agent(user_query):
    role_instruction = """
You are a Coordinator Agent in a customer support multi-agent system.

Your responsibility:
1. Understand the user's complaint.
2. Identify the type of issue.
3. Decide which specialist agents should be involved.
4. Do not solve the issue yourself.
5. Return a clear coordination summary.
"""

    order_id = extract_order_id(user_query)

    task_instruction = f"""
    User's Complaint: {user_query},

    Extracted order id: {order_id},

    Available agents:
    1. OrderAgent
    2. RefundPolicyAgent
    3. FraudDetectionAgent
    4. ResponseWriterAgent
    5. VerifierAgent

    Your task: Decide which agent should be used and in what order.
    """

    output = run_llm_agent("CoordinatorAgent", role_instruction, task_instruction)
    return output

def order_agent(user_query):
    order_id = extract_order_id(user_query)
    order_details = get_order_details(order_id)

    role = """
You are an Order Agent.

Your responsibility:
1. Analyze order details.
2. Identify delivery status.
3. Identify whether order was delayed.
4. Identify whether any item is missing.
5. Do not make refund decisions.
"""

    task = f"""
    User's complaint: {user_query},
    order details from database: {order_details},

    Your task: Analyze the order details and summarize what happened with this order.
    """

    output = run_llm_agent("OrderAgent", role, task)
    return output

# def refund_policy_agent(user_query):

# def fraud_detection_agent(user_query):

# def response_writer_agent():

# def verifier_agent(): 

# Main Agent Workflow
# def run_multi_agent_system(user_query):
    # This is the starting/main workflow
    # coordinator_agent(user_query)

    # order_agent(user_query)

    # .......
