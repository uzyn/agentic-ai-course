from typing import TypedDict, Optional, Annotated
import operator


class State(TypedDict):
    """
    Overall state of the entire LangGraph system.
    """
    messages: Annotated[list, operator.add]
    volley_msg_left: int
    next_speaker: Optional[str]
