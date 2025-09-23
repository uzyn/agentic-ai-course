from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

from state import State
from agents import coordinator
from nodes import (
    human_node,
    check_exit_condition,
    coordinator_routing,
    participant_node,
    summarizer_node
)


load_dotenv(override=True)  # Override, so it would use your local .env file




def build_graph():
    """
    Build the LangGraph workflow.
    """

    builder = StateGraph(State)

    builder.add_node("human", human_node)
    builder.add_node("coordinator", coordinator)  # Use coordinator directly
    builder.add_node("participant", participant_node)
    builder.add_node("summarizer", summarizer_node)

    # Edges
    builder.add_edge(START, "human")

    builder.add_conditional_edges(
        "human",
        check_exit_condition,
        {
            "summarizer": "summarizer",
            "coordinator": "coordinator"
        }
    )

    builder.add_conditional_edges(
        "coordinator",
        coordinator_routing,
        {
            "participant": "participant",
            "human": "human"
        }
    )

    builder.add_edge("participant", "coordinator")

    builder.add_edge("summarizer", END)

    return builder.compile()


def main():
    print("=== SINGAPORE KOPITIAM CHATTER ===")
    print("Chat with our kopitiam regulars! Type 'exit' to end.\n")
    print("Setting: A bustling Singapore kopitiam on a typical afternoon...")
    print("The regulars are here - Uncle Ah Seng at his drinks stall,")
    print("Mei Qi with her phone, Bala checking football scores,")
    print("and Dr. Tan sipping his kopi-o.\n")

    graph = build_graph()

    print(graph.get_graph().draw_ascii())

    initial_state = State(
        messages=[],
        volley_msg_left=0,
        next_speaker=None
    )

    try:
        graph.invoke(initial_state)
    except KeyboardInterrupt:
        print("\n\nConversation interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Ending conversation...")


if __name__ == "__main__":
    main()
