from mcp.server.fastmcp import FastMCP
from tools import email_operations

mcp = FastMCP("email_operations_mcp")
mcp.add_tool(email_operations.get_email_address_by_username)
mcp.add_tool(email_operations.send_email)

if __name__ == "__main__":
    mcp.run("stdio")
