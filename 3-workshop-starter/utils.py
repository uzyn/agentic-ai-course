import os


def debug(message, prefix="DEBUG"):
    """
    Print debug message in gray if DEBUG env var is true.

    Args:
        message: The debug message to print
        prefix: Prefix for the debug message (default: "DEBUG")
    """
    if os.getenv("DEBUG", "false").lower() == "true":
        print(f"    \033[2m[{prefix}] {message}\033[0m")
