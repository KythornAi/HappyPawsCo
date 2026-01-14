# Installing Claudebase Marketplace - Instructions

**Created:** January 7, 2025, 11:30 PM
**Updated:** January 7, 2025, 11:45 PM
**Status:** ⚠️ Plugin marketplace commands not available in current Claude Code version

## Important Discovery

After testing, we discovered that plugin marketplace commands like `/plugin discover` and `claude plugin marketplace add` are **not available in the current version of Claude Code** you're running.

The `/plugin` command in your `.claude/plugin.md` file is a **custom slash command** for managing MCP servers, not the official marketplace feature mentioned in recent Claude Code documentation.

## What This Means

You can still:
✅ Install individual MCP servers using `claude mcp add`
✅ Browse marketplace repositories online (GitHub links below)
✅ Create custom skills, agents, and slash commands in `.claude/` directories
❌ Cannot use `/plugin discover` interactive browser (not available yet)
❌ Cannot use `claude plugin marketplace add` commands (not available yet)

---

---

## What is Claudebase Marketplace?

A comprehensive plugin marketplace containing:
- **24 Skills** - Specialized capabilities
- **14 Agents** - Autonomous workers for specific tasks
- **21 Commands** - Custom slash commands

**Focus Areas:**
- Full-stack development
- Content creation & documentation
- Project management
- Security & testing
- DevOps automation

**GitHub Repository:** https://github.com/claudebase/marketplace

---

## Installation Methods to Try

### Method 1: Using Plugin Marketplace Command (Recommended)

According to the official docs, you can add a marketplace from a Git repository:

```bash
claude plugin marketplace add claudebase https://github.com/claudebase/marketplace.git
```

**OR try the shorthand:**

```bash
claude plugin marketplace add claudebase claudebase/marketplace
```

### Method 2: Direct Git URL

If the above doesn't work, try:

```bash
claude plugin marketplace add https://github.com/claudebase/marketplace.git
```

### Method 3: Add to Configuration File Manually

If commands don't work, you can manually edit `.claude/settings.json` and add:

```json
{
  "extraKnownMarketplaces": [
    {
      "name": "claudebase",
      "url": "https://github.com/claudebase/marketplace.git"
    }
  ]
}
```

Then restart Claude Code.

---

## After Installation

Once installed, you can:

1. **Browse plugins:**
   ```bash
   /plugin discover
   ```

2. **Search for specific plugins:**
   - Type to filter by name, description, or marketplace
   - Filter by "claudebase" to see only plugins from this marketplace

3. **Install specific plugins:**
   ```bash
   /plugin install <plugin-name>
   ```

4. **View installed plugins:**
   ```bash
   /plugin list
   ```

5. **View marketplace info:**
   ```bash
   /plugin marketplace list
   ```

---

## What You'll Find Inside

Based on the GitHub repository, here's what Claudebase offers:

### Content Creation & Documentation
- Documentation generators
- README creators
- API documentation tools
- Technical writing assistants

### Project Management
- Task trackers
- Sprint planning tools
- Workflow automation
- Team collaboration helpers

### Development Tools
- Code generators
- Testing suites
- Deployment automation
- CI/CD helpers

### Security & Testing
- Security scanners
- Penetration testing tools
- Code review automation
- Vulnerability detection

---

## Troubleshooting

**If you get "command not found":**
- Make sure you're in `/Volumes/Home Ext/Home Ext/Desktop/Claude` directory
- Try: `claude plugin --help` to see available commands

**If plugins don't show up:**
- Restart Claude Code
- Run: `claude plugin marketplace list` to verify it's installed

**If you get permission errors:**
- Check that you have git installed: `git --version`
- Try cloning the repo manually first to test access

---

## Alternative: Browse Online First

Before installing, you can browse the marketplace online:

**GitHub:** https://github.com/claudebase/marketplace

Check the README and marketplace.json file to see what's available!

---

## After You Restart Tomorrow

**Your MCP Setup Will Have:**

1. ✅ GitHub MCP (connected)
2. ✅ Filesystem MCP (connected)
3. ✅ Everything MCP (connected)
4. ✅ Thinking MCP (connected)
5. ✅ SEO MCP (will connect after restart)
6. 🎁 Claudebase Marketplace (to be installed)

---

**Good luck! You're building an amazing toolkit for HappyPawsCo content creation! 🐾✨**

---

**Next Session Ideas:**
- Explore what's in Claudebase marketplace
- Test the SEO MCP with a blog post
- Create a HappyPawsCo brand knowledge base
- Build a Pinterest Agent (when ready!)
