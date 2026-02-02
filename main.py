from mcp.server.fastmcp import FastMCP
import directory_operations

mcp = FastMCP("directory_operations_mcp")
mcp.add_tool(directory_operations.get_current_files)
mcp.add_tool(directory_operations.get_file_content)

if __name__ == "__main__":
    mcp.run("stdio")
