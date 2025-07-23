# Pizza Restaurant AI Agents

This project simulates a pizza restaurant interaction using a multi-agent system. The agents handle different roles in a conversation with a customer — from greeting, to showing the menu, to taking the order.

## 🧠 Agents Overview

### 1. Welcome Agent
- Greets the customer warmly.
- Asks them to have a seat.
- Hands off to the **Waiter Agent**.

### 2. Waiter Agent
- Shows the pizza menu:
  - Pepperoni
  - Margherita
  - Veggie
- Then hands off to the **Order Agent**.

### 3. Order Agent
- Takes the pizza order when the customer mentions a pizza name.

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or newer
- `.env` file with your API key:
  ```env
  GEMINI_API_KEY=your_api_key_here
Install Dependencies
bash
Copy
Edit
pip install python-dotenv
Note: The project depends on a custom module named agents. Make sure it’s available in your working environment.

Project Structure
bash
Copy
Edit
.
├── main.py            # Main script that runs the conversation
├── connection.py      # Loads config and external model settings
├── .env               # Contains GEMINI_API_KEY
└── README.md          # Documentation file
🚀 Running the Project
bash
Copy
Edit
python main.py
You’ll be prompted to type messages, and the system will respond using the agents in sequence.

⚙️ Configuration Details
Model used: gemini-2.0-flash

API Endpoint: https://generativelanguage.googleapis.com/v1beta/openai/

The system uses a RunConfig to manage interaction settings and tracing.

💬 Example Interaction
text
Copy
Edit
user: hello
Welcome Agent:
Welcome to the pizza restaurant! Please have a seat.

Waiter Agent:
Here's our menu:
1. pepperoni
2. margherita
3. veggie

Order Agent:
What pizza would you like to order?
📌 Notes
Make sure the .env file exists and includes your Gemini API key.

You can expand the system by adding more agents (e.g., Payment Agent, Feedback Agent).

yaml
Copy
Edit
