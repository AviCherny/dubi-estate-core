from app.mcp.server import create_server
from app.mcp.tools.evaluate_tenant import evaluate_tenant

def main():
    # 1. Create MCP server
    server = create_server()

    # 2. Register the tool
    server.register_tool("evaluate_tenant", evaluate_tenant)

    # 3. Minimal valid payload
    payload = {
        "monthly_income": 10000,
        "credit_score": 720,
        "employment_status": "employed",
        "has_debts": False,
        "has_guarantor": False,
        "legal_status": "citizen",
        "eviction_history": False,
        "criminal_record": "no"
    }

    # 4. Call MCP
    result = server.call_tool("evaluate_tenant", **payload)

    print("\n=== MCP RESULT ===")
    print(result)


if __name__ == "__main__":
    main()
