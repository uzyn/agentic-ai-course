# Prompt Engineering Assignment: Cafe Order Processing System

## Objective
Use prompt engineering to create a natural language order processing system that converts customer orders into structured JSON for a cafe's ordering system.

## Task Description
You will develop a system that takes natural language cafe orders and converts them into machine-readable JSON format. The system should handle various ways customers might phrase their orders.

## The Challenge

A cafe wants to automate their ordering system. When the staff asks:
> "What would you like to have today?"

Customers respond naturally, such as:
- "2x Americano, 1 large fries and 3 hamburger"
- "I'll have a cappuccino and two croissants please"
- "Can I get three iced lattes, make one of them decaf"
- "One burger meal with coke, and an extra order of fries"

## Requirements

Create a prompt that converts these natural language orders into strict JSON output like:

```json
{
  "items": [
    {"name": "Americano", "quantity": 2, "size": "regular"},
    {"name": "Fries", "quantity": 1, "size": "large"},
    {"name": "Hamburger", "quantity": 3, "size": "regular"}
  ],
  "total_items": 6
}
```

## Deliverables

### 1. Code File (.py or .ipynb)
### 2. Documentation (README.md)
- Your system prompt
- 5 example inputs and their JSON outputs

## Example Code Structure

```python
import json
from openai import OpenAI

client = OpenAI()

def process_order(customer_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Your prompt here"},
            {"role": "user", "content": customer_input}
        ],
        temperature=0.1  # Low temperature for consistent output
    )
    return json.loads(response.choices[0].message.content)

# Test with various inputs
orders = [
    "2x Americano, 1 large fries and 3 hamburger",
    "I'll have a cappuccino and two croissants please",
    # Add more test cases
]

for order in orders:
    print(f"Input: {order}")
    print(f"Output: {process_order(order)}")
    print()
```

