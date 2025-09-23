from typing import Literal
from state import State
from agents import coordinator, participant, summarizer


def human_node(state: State) -> dict:
    """
    Human input node - gets user input and sets volley count.
    """
    user_input = input("\nYou: ").strip()

    human_message = {
        "role": "user",
        "content": f"You: {user_input}"
    }

    # Copy existing messages and append the new one
    messages = state.get("messages", []).copy()
    messages.append(human_message)

    return {
        "messages": messages,
        "volley_msg_left": 5
    }


def check_exit_condition(state: State) -> Literal["summarizer", "coordinator"]:
    """
    Check if user typed 'exit' to end conversation.
    """
    messages = state.get("messages", [])
    if messages:
        last_message = messages[-1]
        content = last_message.get("content", "")

        if "exit" in content.lower():
            return "summarizer"

    return "coordinator"


def coordinator_routing(state: State) -> Literal["participant", "human"]:
    """
    Route from coordinator based on volley count.
    """
    volley_left = state.get("volley_msg_left", 0)

    if volley_left > 0:
        return "participant"
    else:
        return "human"


def participant_node(state: State) -> dict:
    """
    Participant node - calls the appropriate participant and handles output.
    """
    next_speaker = state.get("next_speaker", "ah_seng")  # Default fallback

    # Call participant with the selected speaker
    result = participant(next_speaker, state)

    # Print and return messages
    if result and "messages" in result:
        messages = state.get("messages", []).copy()
        for msg in result["messages"]:
            print(msg.get("content", ""))
            messages.append(msg)

        return {"messages": messages}

    return {}


def summarizer_node(state: State) -> dict:
    """
    Summarizer node - generates and displays conversation summary.
    """
    print("\n=== CONVERSATION ENDING ===\n")

    # Generate and print summary
    summary = summarizer(state)
    print(summary)
    print("\nThank you! Come back to kopitiam anytime lah!")

    return {}  # Empty update to end
