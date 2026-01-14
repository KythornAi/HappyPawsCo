# CLAUDE.md - Project Instructions for Claude

**Project:** HappyPawsCo
**Type:** UK Pet Products E-commerce Store
**Launch Date:** January 30, 2026
**GitHub:** github.com/KythornAi/HappyPawsCo

---

## Quick Start

**Before doing any work:**
1. Check `00_Session_Summary/` for the latest `SESSION_HANDOVER_*.md` file
2. Read pending tasks and context from that session
3. Use the proper agents/skills (don't do things manually)

---

## User Communication Preferences

- **Be direct and honest** - Don't sugarcoat issues
- **Challenge assumptions** - Point out if going down wrong path
- **UK English always** - colour, behaviour, favourite (not American spelling)
- **Conversational tone** - Like chatting with a smart friend
- **No unnecessary emojis** - Only use if explicitly requested

---

## Agents & Skills - USE THESE!

**CRITICAL:** Always use the proper agent/skill for each task. This ensures consistency across Claude Desktop, Terminal, and VS Code.

### For Blog Work:
| Task | Use This | Location |
|------|----------|----------|
| Polish blog drafts | Blog Publisher Agent | `.claude/agents/blog-publisher/` |
| Generate image prompts | Blog Image Prompter Agent | `.claude/agents/blog-image-prompter/` |
| Pre-publish review | Blog Quality Checker Skill | `.claude/skills/blog-quality-checker/` |
| SEO optimization | SEO Blog Optimizer Skill | `.claude/skills/seo-blog-optimizer/` |

### For Other Work:
| Task | Use This | Location |
|------|----------|----------|
| Product copy | Product Copy Writer Skill | `.claude/skills/product-copy-writer/` |
| Pinterest pins | Pinterest Pin Creator Skill | `.claude/skills/pinterest-pin-creator/` |
| Content calendar | Content Calendar Planner Skill | `.claude/skills/content-calendar-planner/` |
| Lead magnets | Lead Magnet Creator Skill | `.claude/skills/lead-magnet-creator/` |

---

## Key File Locations

```
00_Knowledge_Base/       # Reference docs (brand voice, approved claims, etc.)
00_Session_Summary/      # Session handover files
11_HappyPawsCo_Blogs/    # ALL blog content (single source of truth)
  ├── drafts/2026-blogs/    # Draft blogs from Make.com
  ├── polished/2026-blogs/  # Polished, ready for review
  └── published/2026-blogs/ # Published to Shopify
.claude/agents/          # Agents (blog-publisher, blog-image-prompter)
.claude/skills/          # Skills (11 active)
```

---

## Blog Workflow

1. **Draft arrives** from Make.com → `11_HappyPawsCo_Blogs/drafts/2026-blogs/[slug]/draft.html`
2. **Polish with Blog Publisher Agent** (not manually!)
3. **Generate image prompts** with Blog Image Prompter Agent
4. **Review with Blog Quality Checker** before publishing
5. **Move to published/** folder after Shopify upload

**Important:** Blogs with ZERO product links should be flagged and put on hold.

---

## Session Handover Format

**Location:** `00_Session_Summary/`
**Naming:** `SESSION_HANDOVER_[MONTH]_[DAY]_[YEAR].md`

Examples:
- `SESSION_HANDOVER_JAN_14_2026.md`
- `SESSION_HANDOVER_JAN_14_2026_EVENING.md` (if multiple same day)

**Include in handover:**
- What was accomplished
- Git commits made
- What's still pending
- Priority for next session
- Any decisions made

---

## Brand Voice Essentials

### DO:
- UK English spelling (colour, favourite, travelling, behaviour)
- Warm, conversational, empathetic tone
- First-person plural ("we" for HappyPawsCo)
- Light touch optimization (polish, don't rewrite)

### DON'T:
- NO em-dashes (–) - AI indicator
- NO "canine companions" or "feline friends" - too academic
- NO fabricated claims or statistics
- NO American spelling or terms

### Reference Files:
- `00_Knowledge_Base/HAPPYPAWSCO_BRAND_VOICE.md`
- `approved-claims.md` - Only use verified facts

---

## Quality Standards Summary

**Core Principle:** Do it right the first time. No "we'll fix it later."

### Blog Standards:
- Title: 50-60 chars with primary keyword
- Meta: 150-160 chars with CTA
- 3-5 internal product links MINIMUM
- All images with descriptive alt text
- UK English throughout

### Technical Standards:
- Proper file naming (lowercase-with-hyphens for directories)
- No TODO sections or placeholders
- Document everything in session handover
- Commit and push regularly

---

## Git Protocol

**Repository:** KythornAi/HappyPawsCo
**Branch:** main (solo project)

**Commit format:** `[Action] [Component] - [Brief description]`
- Good: `Add polished versions of 5 draft blogs`
- Bad: `update` or `fix stuff`

---

## When Context Runs Low

If nearing end of context:
1. Create session handover in `00_Session_Summary/`
2. Follow standard naming: `SESSION_HANDOVER_[MONTH]_[DAY]_[YEAR].md`
3. Document: accomplished, pending, priorities, files modified
4. Commit any uncommitted work to git
5. Push to GitHub

---

## Key Reference Files

**Read these for detailed guidance:**
- `00_Knowledge_Base/HOW_WE_WORK_TOGETHER.md` - Full workflow documentation
- `00_Knowledge_Base/QUALITY_STANDARDS.md` - Complete quality checklist
- `00_Knowledge_Base/AI_PHRASES_TO_AVOID.md` - Banned AI phrases
- `approved-claims.md` - Verified facts only (hallucination prevention)

---

## Current Status (January 2026)

**Active Workflows:**
- Make.com → Blog Publisher → Shopify pipeline
- Pinterest automation via Make.com
- Lead magnet development

**Skills:** 11 active
**Agents:** 2 complete (Blog Publisher, Blog Image Prompter)
**MCP Servers:** github, filesystem, everything, thinking, google-workspace

---

**Remember:** Use the proper agents and skills. Consistency matters across all Claude instances.
