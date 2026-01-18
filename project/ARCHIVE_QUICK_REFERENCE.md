# Quick Reference: Travel Archive Migration

## Status: ✅ Complete

The Travel Planner system has been successfully archived. The active `app/` package now contains only Real Estate code.

## Quick Navigation

### Active Real Estate Code (`app/`)
- **Entry point**: `app/run.py`
- **Server**: `app/mcp/server.py`
- **Orchestrator**: `app/orchestrator.py` (DUBI supervisor)
- **Contracts**: `app/mcp/contracts/evaluate_tenant_contract.py`
- **Tools**: `app/mcp/tools/evaluate_tenant.py`

### Archive Reference (`archive_travel/`)
If you need to understand the Travel system:
- **Original flow**: `archive_travel/orchestrator.py`
- **Agents**: `archive_travel/agents/travel_agent.py`
- **Domain models**: `archive_travel/domain/models.py`
- **Weather tools**: `archive_travel/tools/weather_tool.py`

## What Each Folder Does Now

| Folder | Purpose | Status |
|--------|---------|--------|
| `app/agents/` | Real Estate agents | 🚀 Ready for development |
| `app/domain/` | Real Estate models | 🚀 Ready for development |
| `app/explainers/` | Real Estate explanations | 🚀 Ready for development |
| `app/tools/` | Real Estate tools | 🚀 Ready for development |
| `app/mcp/` | MCP server gateway | ✅ Active and working |
| `app/infra/` | Shared infrastructure | ✅ Active (LLM client) |
| `archive_travel/` | Travel system reference | 📚 Read-only archive |

## Development Guidelines

### ✅ DO
- Add Real Estate agents to `app/agents/`
- Add Real Estate models to `app/domain/models.py`
- Use MCP server pattern for new tools
- Import from `app/` submodules

### ❌ DON'T
- Import from `archive_travel/` in active code
- Add travel-related code to `app/`
- Modify stub files in `app/` (they redirect to archive)

## Testing

Run the application:
```bash
python -m app.run
```

Expected output:
```
=== MCP RESULT ===
{'status': 'SUCCESS', 'tool': 'evaluate_tenant', 'data': {...}}
```

## Full Migration Summary

See `ARCHIVE_MIGRATION_SUMMARY.md` for:
- Detailed list of what was moved
- Complete before/after directory structure
- All changes made to active code
- Future development roadmap
