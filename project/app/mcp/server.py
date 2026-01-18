from typing import Dict, Callable, Any


class MCPServer:
    """
    MCPServer is a lightweight gateway responsible for:
    - Registering available tools
    - Dispatching tool calls by name
    - Wrapping execution with an error boundary

    It does NOT:
    - Contain business logic
    - Know domain concepts
    - Orchestrate flows
    """

    def __init__(self) -> None:
        """
        Initializes an empty tool registry.

        The registry maps:
        - tool name (str)
        - to a callable Python function
        """
        self.tools: Dict[str, Callable[..., Any]] = {}

    def register_tool(self, name: str, func: Callable[..., Any]) -> None:
        """
        Registers a tool in the MCP server.
        """
        self.tools[name] = func

    def call_tool(self, name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Executes a registered tool by name and wraps execution with
        a unified error boundary.

        MCP responsibility:
        - Never crash outward
        - Always return a structured response
        """
        if name not in self.tools:
            return {
                "status": "ERROR",
                "tool": name,
                "error": f"Tool '{name}' is not registered"
            }

        tool_func = self.tools[name]

        try:
            result = tool_func(**kwargs)
            return {
                "status": "SUCCESS",
                "tool": name,
                "data": result
            }
        except Exception as e:
            return {
                "status": "ERROR",
                "tool": name,
                "error": str(e)
            }


def create_server() -> MCPServer:
    """
    Creates and configures an MCPServer instance.

    This is the main bootstrap entry point and is intended to be:
    - Used by the application runtime
    - Wrapped later by an AWS Lambda handler
    """
    server = MCPServer()
    return server
