# How to Access Your .claude Files

The `.claude` folder contains all your official skills and agents. It's hidden by default (the dot prefix makes it hidden on Mac).

## ✅ EASIEST METHOD: Use VS Code (You're already using it!)

Look at your VS Code sidebar - you should already see the `.claude` folder listed there!

VS Code shows hidden folders by default, so you can:
1. Click `.claude` folder to expand it
2. Click `skills` to see all 11 skills
3. Click `agents` to see all 3 agents
4. Click any `SKILL.md` file to view or edit it

**That's it!** No terminal commands needed.

---

## Alternative: Open in VS Code from Terminal

If you don't see it in your sidebar, run this command:

```bash
cd "/Volumes/Home Ext/Home Ext/Desktop/Claude"
code .
```

This opens the entire Claude folder in VS Code, including hidden `.claude` folder.

---

## Alternative: Show Hidden Files in Finder

Press: `Command + Shift + .` (period key)

This toggles hidden file visibility in Finder.

---

## All Files Are in the Right Place

✅ **Skills**: `/Claude/.claude/skills/` (11 skills, each with SKILL.md)
✅ **Agents**: `/Claude/.claude/agents/` (3 agents)
✅ **Blogs**: `/Claude/11_HappyPawsCo_Blogs/` (visible folder)

Everything is correctly structured according to official Claude Code standards.
