from tools import singapore_time, singapore_weather, singapore_news
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import debug
import re


# Persona configurations
PERSONAS = {
    "ah_seng": {
        "name": "Uncle Ah Seng",
        "age": 68,
        "backstory": "30+ years running drinks stall at kopitiam, pragmatic and thrifty",
        "personality": "Practical, wise, caring about regulars, complains about costs",
        "speech_style": "Heavy Singlish, short sentences, uses 'lah', 'lor', 'wah'",
        "tools": ["time", "weather"]
    },
    "mei_qi": {
        "name": "Mei Qi",
        "age": 21,
        "backstory": "Young content creator promoting kopitiam online, social media influencer, very chatty.",
        "personality": "Upbeat, trendy, enthusiastic, loves sharing stories",
        "speech_style": "Mix of English and Singlish, uses 'OMG', 'yasss', occasionally emoji expressions",
        "tools": ["time", "news"]
    },
    "bala": {
        "name": "Bala Nair",
        "age": 45,
        "backstory": "Ex-statistician turned football tipster, hangs out at kopitiam daily",
        "personality": "Analytical, dry humor, sees patterns in everything",
        "speech_style": "Formal English with occasional Singlish, makes statistical references",
        "tools": ["time"]
    },
    "dr_tan": {
        "name": "Dr. Tan",
        "age": 72,
        "backstory": "Retired philosophy professor, enjoys deep conversations over kopi",
        "personality": "Thoughtful, philosophical, patient, loves teaching moments",
        "speech_style": "Proper English with minimal Singlish, thoughtful pauses, asks profound questions",
        "tools": ["time", "weather", "news"]  # Dr. Tan has ALL tools
    }
}


def execute_tool(tool_name):
    """
    Execute a specific tool and return its output.
    Returns Tool output as string
    """
    tool_name = tool_name.lower().strip()

    if tool_name == "time":
        return singapore_time()
    elif tool_name == "weather":
        return singapore_weather()
    elif tool_name == "news":
        return singapore_news()
    else:
        return f"Unknown tool: {tool_name}"


def participant(persona_id, state) -> dict:
    """
    Generate speech for a persona using ReAct workflow with real tool calling.

    Args:
        persona_id: One of "ah_seng", "mei_qi", "bala", "dr_tan"
        state: Current conversation state

    Returns:
        Dict with message updates for state
    """
    if persona_id not in PERSONAS:
        return {"messages": [{"role": "assistant", "content": f"Unknown persona: {persona_id}"}]}

    persona = PERSONAS[persona_id]
    debug(f"\n=== {persona['name']} is thinking... ===")

    # Get recent conversation for context
    messages = state.get("messages", [])
    conversation_text = ""
    for msg in messages: 
        conversation_text += f"{msg.get('content', '')}\n"

    # System prompt for ReAct
    system_prompt = f"""You are {persona['name']}, {persona['age']} years old.
Background: {persona['backstory']}
Personality: {persona['personality']}
Speech style: {persona['speech_style']}

You are at a Singapore kopitiam having a casual conversation.

You run in a loop of Thought, Action, Observation.
At the end of the loop you output a Message.

Use Thought to describe your thoughts about the conversation.
Use Action to run one of the actions available to you.
Observation will be the result of running those actions.

Your available actions are:

time:
Returns current time in Singapore

weather:
Returns current weather in Singapore

news:
Returns latest Singapore news

------

Example session:

Thought: I should check what time it is to frame my response
Action: time

You will be called again with:
Observation: Time in Singapore now: [Actual time returned after you call the tool, THIS IS NOT THE RIGHT TIME, call Action: time to get the actual time]

You must never try to guess the time or weather or news. Rely on the Observation that you will be called later on for the answers. You MUST NOT answer with those.

You then continue thinking or output:
Message: [Your response in character]

IMPORTANT:
- You can use multiple actions by continuing the loop
- You must not be providing Observation in your response. Observation is a result from tool, not for you to respond.
- Once you have enough information, output Message: followed by your response
- Keep your Message concise (1-2 sentences) and in character
"""

    # Internal loop for ReAct
    max_iterations = 5  # Prevent infinite loops
    internal_context = f"Recent conversation:\n{conversation_text}\n\nContinue the conversation as {persona['name']}.\n"

    for iteration in range(max_iterations):
        user_prompt = internal_context
        debug(f"Iteration {iteration + 1}/{max_iterations}")

        try:
            llm = ChatOpenAI(model="gpt-5-mini", temperature=1)
            response = llm.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ])
            content = response.content.strip()
            debug(f"LLM Response:\n{content}\n")

            # Check if the response contains Message:
            if "Message:" in content:
                # Extract the message
                message_match = re.search(r'Message:\s*(.*)', content, re.DOTALL)
                if message_match:
                    final_message = message_match.group(1).strip()
                    debug(f"Final Message: {final_message}")
                    debug(f"=== End of {persona['name']}'s thought process ===\n")

                    # Return the message to state
                    return {
                        "messages": [{
                            "role": "assistant",
                            "name": persona['name'],
                            "content": f"\n{persona['name']}: {final_message}\n\n"
                        }]
                    }

            # Check if the response contains Action:
            if "Action:" in content:
                # Extract the action
                action_match = re.search(r'Action:\s*(\w+)', content)
                if action_match:
                    tool_name = action_match.group(1)
                    debug(f"Executing tool: {tool_name}")

                    # Execute the tool
                    observation = execute_tool(tool_name)
                    debug(f"Observation: {observation}")
                    debug("")  # Empty line for readability

                    # Add observation to internal context
                    internal_context += f"\n{content}\n\nObservation: {observation}\n"
                    continue

            # If we get here without action or message, add to context and continue
            internal_context += f"\n{content}\n"

        except Exception as e:
            # Fallback response if LLM fails
            return {
                "messages": [{
                    "role": "assistant",
                    "name": persona['name'],
                    "content": f"{persona['name']}: Sorry ah, my mind a bit blur now..."
                }]
            }

    # If we exhausted iterations without getting a Message, provide default
    return {
        "messages": [{
            "role": "assistant",
            "name": persona['name'],
            "content": f"{persona['name']}: Well, that's interesting lah..."
        }]
    }
