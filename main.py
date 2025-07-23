from agents import Agent, Runner
from connection import config
import asyncio
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX


# Order Agent
order_agent = Agent(
    name = "Order Agent",
    instructions="""
    You are an order agent in pizza restaurant.
    When a customer mentions a pizza name(e.g. pepperoni, margherita, veggie),you will take the order.
    Example: 
    "I want a pepperoni pizza"
    """
)

# Waiter Agent
waiter_agent = Agent(
    name = "Waiter Agent",
    instructions="""
    You are a waiter in pizza restaurant and provide a list of pizzas to the customer.
    ### Pizzas Menu:
    1. pepperoni
    2. margherita
    3. veggie
    After showing the menu , hand off to order agent to take the order.
    """,
    handoffs=[order_agent]
)

# Welcome Agent
welcome_agent = Agent(
    name = "Welcome Agent",
    instructions="""
    You are a Welcome to the pizza restaurant.
    greet the customer warmly.
    Ask  them to have a seat.
    hand off to the waiter agent to show the pizza menu.
    """,
    handoffs=[waiter_agent]
)

# Main runner

async def main():
    while True:
        msg = input("user:")
        result = await Runner.run(welcome_agent,msg, run_config=config)
        print(f"\n{result.last_agent.name}:")
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
        




