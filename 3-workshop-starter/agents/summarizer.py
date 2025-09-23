from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


def summarizer(state) -> str:
    """
    Generate summary report using LLM when conversation ends.

    Args:
        state: Current conversation state with messages

    Returns:
        Formatted summary string
    """
    messages = state.get("messages", [])

    if not messages:
        return "No conversation to summarize."

    # Extract conversation text
    conversation_text = ""
    for msg in messages:
        # Messages are now always dicts
        conversation_text += f"{msg.get('content', '')}\n"

    if not conversation_text.strip():
        return "No conversation content to summarize."

    # System prompt for summarization
    system_prompt = """You are a keen observer at a Singapore kopitiam who has been listening to the conversation.

Generate a concise summary of the conversation that captures:
1. Key topics discussed
2. The dynamics between participants
3. Any memorable quotes or highlights
4. The overall mood and flow of the conversation

Format your summary in a clear, engaging way that captures the essence of kopitiam banter.
Keep it concise but insightful."""

    user_prompt = f"""Here's the conversation that took place:

{conversation_text}

Please provide a summary of this kopitiam conversation."""

    try:
        # Call LLM
        llm = ChatOpenAI(model="gpt-5-nano", temperature=1)

        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ])

        if isinstance(response.content, list):
            summary = " ".join(str(item) for item in response.content).strip()
        else:
            summary = str(response.content).strip()

        # Format with header
        return f"=== KOPITIAM CONVERSATION SUMMARY ===\n\n{summary}"

    except Exception as e:
        # Fallback to basic summary if LLM fails
        return f"""=== KOPITIAM CONVERSATION SUMMARY ===

Total messages: {len(messages)}

Unable to generate detailed summary at this time.
The conversation has been logged for review."""
