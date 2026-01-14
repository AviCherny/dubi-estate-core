from typing import Dict, Callable, Any
from app.mcp.tools.plan_trip import plan_trip


class MCPServer:
    """
    MCPServer is a lightweight gateway responsible for:
    - Registering available tools
    - Dispatching tool calls by name
    - Staying completely unaware of business logic

    It does NOT:
    - Validate business rules
    - Make decisions
    - Know domain concepts
    """

    def __init__(self) -> None:
        """
        Initializes an empty tool registry.

        The registry maps:
        - tool name (str)
        - to a callable Python function

        Tools are registered explicitly during server bootstrap.
        """
        #MCP maintains a mapping between tool names (strings) and the actual Python functions that implement them.
        self.tools: Dict[str, Callable[..., Any]] = {}

    def register_tool(self, name: str, func: Callable[..., Any]) -> None:
        """
        Registers a tool in the MCP server.

        Args:
            name: Public tool name exposed to MCP clients
            func: The function that will be executed when the tool is called

        This allows the MCP server to remain generic and extensible.
        """
        self.tools[name] = func

    def call_tool(self, name: str, **kwargs: Any) -> Any:
        """
        Executes a registered tool by name.

        Args:
            name: The tool name requested by the client
            **kwargs: Raw input payload (typically JSON)

        Returns:
            The tool result as a serializable object

        Raises:
            KeyError: If the requested tool is not registered
        """
        if name not in self.tools:
            raise KeyError(f"Tool '{name}' is not registered")

        tool_func = self.tools[name]
        return tool_func(**kwargs)


def create_server() -> MCPServer:
    """
    Creates and configures an MCPServer instance.

    This is the main bootstrap entry point and is intended to be:
    - Used by the application runtime
    - Wrapped later by an AWS Lambda handler

    All tools exposed by MCP must be registered here.
    """
    server = MCPServer()
    # Register MCP tools here
    server.register_tool("plan_trip", plan_trip)
    return server
