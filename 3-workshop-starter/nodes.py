from typing import Literal
from state import State
from agents import coordinator, participant, summarizer


def human_node(state: State) -> dict:
    """
    Human input node - gets user input and sets volley count.
    """
    user_input = input("\nYou: ").strip()
    
    # TODO: Return


def check_exit_condition(state: State) -> Literal["summarizer", "coordinator"]:
    """
    Check if user typed 'exit' to end conversation.
    """
    messages = state.get("messages", [])
    
    # TODO: Return based on condition


def coordinator_routing(state: State) -> Literal["participant", "human"]:
    """
    Route from coordinator based on volley count.
    """
    volley_left = state.get("volley_msg_left", 0)

    # TODO: Return based on condition


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
