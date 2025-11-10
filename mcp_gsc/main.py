import os

from .gsc_server import mcp, run_oauth_server

def main():
    """Run the MCP server."""

    transport = os.environ.get("MCP_TRANSPORT", "sse").lower()
    if transport == "stdio":
        mcp.run()
    else:
        run_oauth_server()

if __name__ == "__main__":
    main()
