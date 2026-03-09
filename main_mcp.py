from mcp.server.fastmcp import FastMCP
from tools import message_operations

mcp = FastMCP("seatalk_mcp")
mcp.add_tool(message_operations.send_seatalk_message)

if __name__ == "__main__":
    mcp.run("stdio")