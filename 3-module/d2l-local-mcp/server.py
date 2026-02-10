"""Local MCP Server — system time access via stdio transport."""

from datetime import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local-tools")


@mcp.tool()
def get_current_datetime() -> str:
    """Get the current local date and time."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S (%A)")


if __name__ == "__main__":
    mcp.run(transport="stdio")
