# Claude Code Cheat Sheet - HappyPawsCo

Quick reference for commands, agents, and skills. Print this or keep it handy.

---

## Most Used Commands

| Command | What It Does |
|---------|--------------|
| `/compact` | Compress conversation (frees up context) |
| `/context` | Show how much context you've used (visual grid) |
| `/cost` | Show token/cost usage this session |
| `/clear` | Clear conversation history |
| `/help` | Get help on any command |
| `/memory` | Edit CLAUDE.md files |
| `/model` | Switch AI model |

---

## Git & Code Commands

| Command | What It Does |
|---------|--------------|
| `/review` | Request code review |
| `/security-review` | Security review of pending changes |
| `/rewind` | Undo conversation and/or code changes |
| `/plan` | Enter planning mode (safe, no code changes) |

---

## Session Management

| Command | What It Does |
|---------|--------------|
| `/rename <name>` | Name this session for easy finding later |
| `/resume` | Resume a previous session |
| `/export` | Export conversation to file |
| `/exit` | Exit Claude Code |

---

## Project Skills (Say These or Claude Uses Automatically)

### Blog Work
| Skill | When to Use |
|-------|-------------|
| `blog-quality-checker` | "Run blog quality checker on this post" |
| `seo-blog-optimizer` | "Optimise this blog for SEO" |
| `content-research-writer` | "Help me write a blog with citations" |

### Pinterest & Marketing
| Skill | When to Use |
|-------|-------------|
| `pinterest-pin-creator` | "Create Pinterest pins for this blog" |
| `pinterest-health-check` | "Check my Pinterest automation setup" |
| `content-calendar-planner` | "Plan my content calendar" |
| `lead-magnet-creator` | "Create a lead magnet PDF" |

### Research & Strategy
| Skill | When to Use |
|-------|-------------|
| `niche-gap-researcher` | "Find gaps in our market" |
| `competitive-ads-extractor` | "Analyse competitor ads" |
| `lead-research-assistant` | "Find leads for our products" |

### Writing
| Skill | When to Use |
|-------|-------------|
| `product-copy-writer` | "Write product copy for this item" |

---

## Project Agents (More Powerful, Use for Bigger Tasks)

| Agent | What It Does | How to Invoke |
|-------|--------------|---------------|
| `blog-publisher` | Polish drafts, add product links | "Use blog publisher agent on this draft" |
| `blog-image-prompter` | Generate image prompts | "Generate image prompts for this blog" |
| `pinterest-pin-strategist` | 3 pin strategies per blog | "Create pin strategies for this blog" |
| `keyword-research` | Find 50-100 rankable topics | "Run keyword research agent" |
| `product-database` | Query product sheet | "Check product database for harnesses" |
| `content-inventory-alignment` | Validate product mentions | "Check if blog mentions match products" |
| `research-gap-filler` | Fill missing research | "Fill research gaps for this product" |

---

## Quick Phrases (Copy-Paste These)

### Starting a Session
```
Hey Claude, what's the current status?
```

### Blog Work
```
Polish this blog using the blog publisher agent
```
```
Generate image prompts for this blog
```
```
Run the blog quality checker before I publish
```

### Research
```
Run the keyword research agent for 50 topics
```
```
Find niche gaps in the UK pet travel market
```

### Pinterest
```
Create 3 pin strategies for this blog
```
```
Check my Pinterest automation is working
```

### Content Planning
```
Plan my content calendar for next month
```
```
What's on the incomplete tasks tracker?
```

### Housekeeping
```
Update the task tracker with what we did
```
```
Create a session handover summary
```
```
Commit and push our changes
```

---

## MCP Servers Available

| Server | What It Gives You |
|--------|-------------------|
| `github` | GitHub repo access, PRs, issues |
| `google-workspace` | Google Sheets, Docs, Drive |
| `filesystem` | File operations |
| `thinking` | Extended reasoning |

---

## Emergency Commands

| Situation | Command |
|-----------|---------|
| Running out of context | `/compact` |
| Need to see context usage | `/context` |
| Something went wrong | `/rewind` |
| Need to save progress | "Create a session handover now" |
| Check what's pending | "Read the incomplete tasks tracker" |

---

## File Locations to Remember

| What | Where |
|------|-------|
| Task tracker | `00_Session_Summary/INCOMPLETE_TASKS_TRACKER.md` |
| Session handovers | `00_Session_Summary/SESSION_HANDOVER_*.md` |
| Blog drafts | `11_HappyPawsCo_Blogs/drafts/2026-blogs/` |
| Polished blogs | `11_HappyPawsCo_Blogs/polished/2026-blogs/` |
| Research brief | `00_Knowledge_Base/HappyPawsCo_Research_Brief_Condensed.md` |
| Brand voice | `00_Knowledge_Base/HAPPYPAWSCO_BRAND_VOICE.md` |
| Agents | `.claude/agents/` |
| Skills | `.claude/skills/` |

---

## Google Sheet IDs

| Sheet | ID |
|-------|-----|
| Content Calendar | `1a7vymBudx8x8-62zPRzzv4Bru3jUciiGooGDy1wzXT4` |
| Pinterest Workflow | `1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE` |
| Product Database | (check tracker if needed) |

---

## Tips

1. **Tab completion works** - Type `/` then Tab to see all commands
2. **Claude reads CLAUDE.md automatically** - Project rules are always loaded
3. **PreCompact hook is active** - Transcripts backup before compaction
4. **Commit frequently** - Don't wait until end of session
5. **Update tracker as you go** - Not at the end

---

**Last Updated:** January 16, 2026
