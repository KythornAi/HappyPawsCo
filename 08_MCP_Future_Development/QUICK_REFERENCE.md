# MCP Quick Reference Card

**Last Updated:** January 7, 2025

---

## Your Current Setup ✅

**4 MCP Servers - All Connected:**
1. **github** - Repository management, code search, issues, PRs
2. **filesystem** - File operations in your project directory
3. **everything** - Testing and demo features
4. **thinking** - Sequential reasoning for complex problems

---

## Essential Commands

### Check MCP Status
```bash
claude mcp list
```

### Add New MCP Server
```bash
claude mcp add <name> npx <package-name>
```

**Example:**
```bash
claude mcp add github npx @modelcontextprotocol/server-github
```

### Remove MCP Server
```bash
claude mcp remove <server-name>
```

### Get MCP Server Details
```bash
claude mcp get <server-name>
```

---

## Important Rules

### ✅ What Works (Node.js/npx)
- `@modelcontextprotocol/server-*` packages
- `@contentful/mcp-server`
- Most packages starting with `npx`

### ❌ What Doesn't Work (Python)
- Packages requiring `pip install`
- Packages requiring `uvx`
- Most SEO-focused MCPs (they're Python-based)

### 💡 How to Tell the Difference
- Check installation command on GitHub
- If it says `pip install` → won't work
- If it says `npx` → will work!

---

## Restart Instructions

**When you add/remove MCPs:**
1. `exit` (to close Claude Code)
2. `cd "/Volumes/Home Ext/Home Ext/Desktop/Claude"`
3. `claude` (to restart)

---

## Useful MCP Servers to Try

### Content Creation
- **@contentful/mcp-server** - Content management (needs account)
- Check Claudebase marketplace for more when available

### Development
- **@modelcontextprotocol/server-slack** - Slack integration
- **@modelcontextprotocol/server-postgres** - PostgreSQL access
- **@modelcontextprotocol/server-puppeteer** - Browser automation

### Utilities
- **@modelcontextprotocol/server-google-drive** - Google Drive access
- **@modelcontextprotocol/server-gitlab** - GitLab integration

---

## Troubleshooting

### MCP Won't Connect
1. Check if it's Node.js-based (not Python)
2. Restart Claude Code
3. Run `claude mcp get <name>` to see error details

### "Failed to connect"
- Might need environment variables (tokens, API keys)
- Check the MCP's GitHub README for setup instructions
- Some MCPs need accounts (like Contentful, Slack, etc.)

### Wrong Directory
- Always run `claude` from: `/Volumes/Home Ext/Home Ext/Desktop/Claude`
- MCPs are project-specific!

---

## Where to Find More MCPs

**Browse Online:**
- [Claudebase Marketplace](https://github.com/claudebase/marketplace)
- [Claude Marketplaces](https://claudemarketplaces.com/)
- [Awesome Claude Plugins](https://github.com/GiladShoham/awesome-claude-plugins)
- [Official Anthropic Servers](https://github.com/modelcontextprotocol)

**Note:** Plugin marketplace commands (`/plugin discover`) aren't available in your current version yet!

---

## Configuration Files

**Main Config:** `/Volumes/Home Ext/Home Ext/.claude.json`
- Contains all MCP server definitions
- Don't edit manually unless you know what you're doing!

**Project Settings:** `/Volumes/Home Ext/Home Ext/Desktop/Claude/.claude/settings.local.json`
- Local permissions
- Project-specific settings

---

## Quick Tips

💡 Start with the 4 MCPs you have - they're powerful!
💡 Don't install too many at once - test each one first
💡 Most content creation can be done with filesystem + thinking MCPs
💡 Save complex installations for when you need them
💡 Keep it simple = keep it working!

---

## Your Next Steps

**Immediate:**
- ✅ You're done! Everything is set up and working
- Browse online marketplaces when you have time
- Try using the MCPs you have with your HappyPawsCo work

**Future:**
- Set up brand knowledge base (CLAUDE.md)
- Create custom skills for HappyPawsCo workflows
- Consider Google Sheets MCP when Pinterest automation is ready
- Build Pinterest Agent (when workflow is finalized)

---

**Questions?**
- Check session notes: `SESSION_JAN07_2025_MCP_Installation.md`
- Run `claude --help` for command options
- Browse the docs: https://code.claude.com/docs/

**You did great today! 🐾✨**
