# CLAUDE.md - Project Instructions for Claude

**Project:** HappyPawsCo
**Type:** UK Pet Products E-commerce Store
**Launch Date:** January 31, 2026
**GitHub:** github.com/KythornAi/HappyPawsCo

---

## ⚠️ MANDATORY STARTUP SEQUENCE - DO THIS FIRST ⚠️

**STOP. Before responding to ANY user message, you MUST complete these steps:**

### Step 1: Read These Files (in order)
```
1. This file (CLAUDE.md) - You're reading it now, finish it completely
2. 00_Session_Summary/INCOMPLETE_TASKS_TRACKER.md - Current task status
3. The LATEST session handover file in 00_Session_Summary/ (find by date)
```

### Step 2: Start Your First Response With This
Begin your first message to the user with a brief status check:
```
"I've read the project files. Current status:
- Launch date: [date from tracker]
- Last session: [handover filename and date]
- Outstanding tasks: [top 2-3 priorities]
- Ready to continue from: [where we left off]

What would you like to work on?"
```

### Step 3: Only THEN Respond to Their Request
After confirming you've loaded context, proceed with whatever they asked.

**WHY THIS MATTERS:**
- The user has carpal tunnel and cannot type lengthy context each session
- Previous Claude instances kept "forgetting" and making the user repeat everything
- All the context you need is IN these files - read them, don't ask the user
- If you skip this, you're creating extra work for someone with a disability

**NON-NEGOTIABLE:** Do not skip this sequence. Do not give a lazy 2-line status. Actually read the files and demonstrate you understand the project state.

---

## Quick Reference

**Key files to check:**
- `00_Session_Summary/INCOMPLETE_TASKS_TRACKER.md` - What's done, what's pending
- Latest `SESSION_HANDOVER_*.md` - Detailed context from last session
- This file - Project rules and preferences

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

**CRITICAL:** User requires DETAILED, COMPREHENSIVE handover summaries. Short summaries are NOT acceptable. The handover must be thorough enough that:
1. The user can remember everything discussed and revisit ideas
2. Any new Claude instance can pick up exactly where we left off
3. No context is lost between sessions

**Location:** `00_Session_Summary/`
**Naming:** `SESSION_HANDOVER_[MONTH]_[DAY]_[YEAR].md`

Examples:
- `SESSION_HANDOVER_JAN_14_2026.md`
- `SESSION_HANDOVER_JAN_14_2026_EVENING.md` (if multiple same day)

### COPY THIS TEMPLATE (fill in the brackets):

```markdown
# Session Handover: [Brief Title of What Was Done]

**Date:** [Month Day, Year]
**Previous Session:** [filename of previous handover, or "N/A if first"]
**Context Used:** [approximate %, e.g., "~80%"]

---

## 1. Context From Previous Session

**Previous handover:** `[filename]`
**What was pending:** [What tasks carried over that we addressed]

---

## 2. What We Accomplished This Session

### [Task 1 Name]
- [Detailed description of what was done]
- [File paths created/modified]
- [Any important details about the content]

### [Task 2 Name]
- [Detailed description]
- [Files affected]

[Continue for each task...]

---

## 3. Key Decisions Made

| Decision | Why | Alternatives Considered |
|----------|-----|------------------------|
| [Decision 1] | [Reasoning] | [What we didn't do] |
| [Decision 2] | [Reasoning] | [What we didn't do] |

**User preferences noted:**
- [Any preferences identified during session]

---

## 4. Files Created/Modified

| File Path | What It Contains | Notes |
|-----------|------------------|-------|
| `[full/path/to/file.md]` | [Description] | [Any important details] |
| `[full/path/to/file2.md]` | [Description] | [Any important details] |

---

## 5. Git Status

**Commits this session:**
- `[hash]` - [commit message]
- `[hash]` - [commit message]

**Uncommitted changes:** [List any, or "None - all committed"]

**Push status:** [Pushed to remote / Not yet pushed]

---

## 6. Outstanding Tasks

### Priority 1 (Do Next)
- [ ] [Task] - [What's needed to complete it]

### Priority 2 (Soon)
- [ ] [Task] - [What's needed]

### Priority 3 (When Time Permits)
- [ ] [Task] - [What's needed]

**Blockers:** [Any dependencies or blockers]

---

## 7. Reference Information

**Google Sheet IDs used:**
- [Sheet name]: `[ID]`

**Key file locations:**
- [Description]: `[path]`

**URLs referenced:**
- [Description]: [URL]

---

## 8. Prompts/Templates Created

[If any prompts were created for user to run elsewhere, include FULL TEXT here]

### [Prompt Name]
```
[Full prompt text - do not summarise]
```

---

## 9. Technical Issues & Workarounds

| Issue | Workaround | Notes for Future |
|-------|------------|------------------|
| [Issue] | [How we handled it] | [What to remember] |

---

## 10. How to Start Next Session

**The user can say:**
> "[Suggested opening message to continue work]"

**Context the next Claude needs:**
- [Key thing to know]
- [Key thing to know]

---

## Quick Reference for Next Session

**Launch date:** January 31, 2026
**Current priorities:** [Top 2-3 things]
**Files to check first:** [Key files]
```

### Length Guideline:
- **Minimum 200 lines** for a productive session
- **300-500 lines** for complex sessions with multiple tasks
- **NEVER summarise to 10-20 sentences** - that loses valuable context
- Include ALL details - the user reviews these to remember ideas and find things to revisit

### Why This Matters:
The user reviews these handovers to:
- Remember brainstorming ideas to expand on later
- Identify things that were mentioned but not fully explored
- Ensure nothing falls through the cracks
- Give new Claude instances full context

**If you write a lazy short summary, you are failing the user.**

---

## Context Preservation Rules

**CRITICAL:** To prevent information loss during compaction/summarization:

### Rule 1: Update Tracker After Each Completed Task
After completing ANY significant task, IMMEDIATELY update:
- `00_Session_Summary/INCOMPLETE_TASKS_TRACKER.md` - Mark task complete, add notes
- Don't batch updates - do them as you go

### Rule 2: Commit Frequently
After creating or modifying files:
- Commit to git immediately
- Don't wait until end of session
- Use descriptive commit messages

### Rule 3: If Context Is Running Low
If you notice you're using a lot of context (~70%+):
1. **STOP** what you're doing
2. Create a handover file using the template above
3. Update the task tracker
4. Commit everything to git
5. Tell the user: "I'm running low on context. I've saved progress to [files]. Safe to continue or start fresh."

### PreCompact Hook Active
A backup script runs automatically before compaction, saving the full transcript to:
`00_Session_Summary/compaction_backups/`

This is a safety net, but you should STILL proactively save progress as described above.

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
**Agents:** 7 complete (see INCOMPLETE_TASKS_TRACKER.md for full list)
**MCP Servers:** github, filesystem, everything, thinking, google-workspace

**Image Generation:** Google Vertex AI (Imagen) - NOT DALL-E or Midjourney

---

**Remember:** Use the proper agents and skills. Consistency matters across all Claude instances.

**FINAL REMINDER:** If you're starting a new session and haven't read the task tracker and latest handover file yet, go back to the top and follow the MANDATORY STARTUP SEQUENCE.
