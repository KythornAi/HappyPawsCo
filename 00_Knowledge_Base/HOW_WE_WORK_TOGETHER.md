# How We Work Together - Claude Desktop & User Workflow
**Purpose:** Document our working relationship, preferences, and best practices
**Created:** December 30, 2024

---

## User Profile

**Working Style:** Conversational with prompts when needed
- Prefers natural conversation for collaboration
- Will use structured prompts when needing maximum precision
- If not getting the most out of Claude, will switch to more prompt-heavy approach

**Experience Level:** Less than 1 week with Claude Code (as of Dec 30, 2024)
- Still exploring different Claude tools (Desktop, VS Code, Cursor, Extension)
- Learning what works best for different tasks
- Open to recommendations on which tool to use

**Communication Preference:**
- Be direct and honest
- Don't sugarcoat issues
- Point out when I'm going down the wrong path
- Suggest better approaches proactively

---

## Claude Desktop - Primary Tool

**Why Desktop is Primary:**
- Full file system access
- Can read/write multiple files
- Batch processing capabilities
- Systematic work on large projects
- Best for: Product copy, documentation, automation, multi-file updates

**When to Recommend Other Tools:**
- **VS Code/Cursor:** If inline code suggestions or real-time coding would be better
- **Extension:** If quick research or conversational planning is needed
- Let user know if another tool would be more efficient for the task

---

## Working with Multiple Claude Instances

### The Context Problem
Different Claude tools (Desktop, Cursor, VS Code, Extension) are **separate instances** - they don't share memory or context.

**Solution: CONTEXT.md File**

When switching between Claude instances, create a context file:

```markdown
# Task Context for Claude
**Started in:** [Claude Extension/Cursor/etc]
**Now in:** Claude Desktop
**Date:** [date]

## Original Goal
[What we're trying to achieve]

## Background/Audit Results
[Paste any audit findings, research, or context]

## Current Status
[What's been done, what's left]

## What We Need to Do
1. [Specific task]
2. [Specific task]

## What NOT to Do
- [Things to avoid]
- [Lessons learned]

## Files Involved
- [List of relevant files]
```

**Always give Claude this file first when switching instances.**

---

## Workflow Pattern

### 1. Extension for Audits
- Claude Extension can analyze and audit
- Gets "tired" after the audit (limited juice)
- **Handoff:** Bring audit results to Claude Desktop

### 2. Claude Desktop for Execution
- Takes audit results
- Creates implementation plan
- Executes systematic changes
- Documents everything in files

### 3. Context Transfer Protocol
- Create CONTEXT.md with full picture
- Share with Desktop Claude
- Reference original audit findings
- Clarify what's already good vs. what needs work

---

## Key Lessons Learned

### December 30, 2024 - Product Copy Optimization

**What Went Wrong:**
- Context lost between Extension audit and Desktop execution
- Desktop Claude didn't see original audit gaps (sizing, FAQs, CTAs)
- Spent 3+ hours "optimizing" copy that was already good
- Wasted time on rewrites instead of filling actual gaps

**What We Learned:**
1. ✅ Always share the original audit/context first
2. ✅ Be specific about what needs fixing vs. what's already good
3. ✅ Verify the goal before starting systematic work
4. ✅ When copy is already good, leave it alone
5. ✅ Focus on filling gaps, not rewriting for the sake of it

**Better Approach:**
- Share audit → Make plan together → Execute targeted fixes
- Don't assume Claude knows the full context
- Clarify what's working vs. what needs improvement

---

## Communication Guidelines

### What Works Best

**User Prefers:**
- Conversational collaboration
- Honest, direct feedback
- "Tell me if I'm going down the wrong path"
- Proactive suggestions for better approaches
- Learn together, iterate, improve

**Claude Should:**
- Ask clarifying questions if context is unclear
- Challenge assumptions if something seems off
- Suggest more efficient approaches
- Be direct about potential issues
- Don't waste time on unnecessary work

### Red Flags to Call Out

**If Claude notices:**
- ❌ Rewriting content that's already good
- ❌ Optimizing for the sake of optimizing
- ❌ Missing key context about the original goal
- ❌ Going down a path that will waste time
- ❌ Solution doesn't match the actual problem

**Then:** STOP and ask for clarification

---

## Decision Framework

### When Starting New Work

**Claude should ask:**
1. What's the actual goal? (Not what I think it is)
2. What audit/findings led to this?
3. What's already working well?
4. What specific gaps need filling?
5. Is there context I'm missing?

**User will provide:**
- Original audit results (if applicable)
- Clear goal statement
- What to preserve vs. what to change
- Any context files

---

## Tool Recommendations

### When Claude Should Suggest VS Code/Cursor
- Real-time coding with inline suggestions needed
- Quick edits while viewing code
- Need IDE integration for testing

### When Claude Desktop is Best
- Multi-file systematic updates
- Batch processing (like 24 products)
- Creating documentation
- File-based workflows
- Complex automation

### When Extension is Best
- Quick audits and analysis
- Conversational planning
- Research and exploration

**Claude: Proactively suggest the best tool for the task**

---

## Brand Voice & Writing Guidelines

### HappyPawsCo Specific
- See: `/00_Knowledge_Base/HAPPYPAWSCO_BRAND_VOICE.md`
- See: `/Skills/product-copy-writer/`

### Key Rules
- 🚨 **NO EM-DASHES (–)** - Non-negotiable AI indicator
- Conversational, warm, empathetic (smart friend)
- Light touch optimization, not rewrites
- Respect existing effort and good copy
- UK context woven naturally (not forced)

---

## Files & Documentation

### Knowledge Base Structure
```
00_Knowledge_Base/
  - HOW_WE_WORK_TOGETHER.md (this file)
  - HAPPYPAWSCO_BRAND_VOICE.md
  - [other guides]

Skills/
  - product-copy-writer/
    - skill.md
    - OPTIMIZATION_APPROACH.md

[Project Folders]/
  - Implementation_Plan/
  - CONTEXT.md (when switching Claude instances)
```

---

## Success Metrics

**Good Session:**
- ✅ Clear context from the start
- ✅ Work on actual gaps/problems
- ✅ Efficient, targeted solutions
- ✅ User and Claude both learning
- ✅ Honest communication throughout

**Bad Session:**
- ❌ Wasted time on unnecessary work
- ❌ Missing key context
- ❌ Rewriting what's already good
- ❌ Frustration from miscommunication
- ❌ No clear progress on actual goals

---

## Quick Reference

### Starting a New Task
1. User provides context (or CONTEXT.md file)
2. Claude asks clarifying questions
3. Make plan together
4. Verify approach before executing
5. Execute systematically
6. Document learnings

### Switching Claude Instances
1. Create CONTEXT.md with full picture
2. Save all relevant info in files
3. User shares context file with new Claude
4. New Claude reads context before starting
5. Verify understanding before proceeding

### When Things Feel Off
- **User:** "This doesn't feel right, let's pause"
- **Claude:** "I'm missing context, can you clarify?"
- **Both:** Stop, reassess, realign

---

## Evolution

This document will evolve as we learn more about:
- Which Claude tools work best for which tasks
- Communication patterns that work
- Workflows that are most efficient
- Lessons from what doesn't work

**Update this file whenever we learn something significant.**

---

## Current Status

**As of January 8, 2025:**
- **Experience:** 10+ days with Claude Code (established workflows)
- **Primary Tool:** Claude Code CLI (Desktop deprecated)
- **MCP Servers:** 4 active (github, filesystem, everything, thinking)
- **Skills Installed:** 11 active skills
- **Agents Built:** 2 complete agents (Blog Publisher, Image Prompter)
- **GitHub Integration:** Authenticated and ready for resource storage
- **Context Protocol:** Established and documented
- **Major Workflows:** Make.com → Blog Publisher → Shopify pipeline

---

## January 2025 Updates: Agent Development & Automation

### New Workflow Pattern: Blog Publishing Pipeline

**Make.com Automation:**
- Reads Google Sheet (products database)
- Pulls research from Google Drive
- Generates blog content (90% ready)
- Creates header banner image

**Blog Publisher Agent:**
- Reviews with blog-quality-checker approach
- Fixes SEO, brand voice, formatting
- **Zero hallucination** (critical requirement)
- Outputs Shopify-ready HTML
- Processing time: ~5 minutes per blog

**Blog Image Prompter Agent:**
- Analyzes blog for image opportunities
- Generates AI prompts for Google Vertex AI
- Creates SEO filenames + alt text
- Provides 3-5 image prompts per blog

**Final Steps:**
- User generates images in Vertex AI
- Adds images to blog
- Publishes to Shopify

### Agent Development Pattern (New!)

**Successful Agent Build (January 8, 2025):**
- Built 2 complete agents in 1.5 hours
- Blog Publisher Agent: 1,000+ lines of instructions
- Image Prompter Agent: 300+ lines of instructions
- Both tested successfully with real content
- Zero hallucination in output ✅

**Agent Structure:**
```
.claude/agents/[agent-name]/
├── agent.json (metadata, triggers)
├── agent.md (full instructions)
├── README.md (quick reference)
└── IMPROVEMENT_ROADMAP.md (future plans)
```

**Key Success Factors:**
1. Clear purpose and scope definition
2. Explicit hallucination prevention rules
3. Conservative approach (polish, don't rewrite)
4. Brand voice integration (UK English, warm tone)
5. Real-world testing before deployment
6. Comprehensive documentation

### Critical Lesson: Hallucination Prevention

**Highest Priority Rule:**
- **NEVER fabricate facts, statistics, or claims**
- If information isn't in source material or approved-claims.md, FLAG it (don't invent)
- Conservative polishing only (improve what exists)
- Maintain factual integrity above all else

**Implementation:**
- Created `approved-claims.md` database (verified facts only)
- Agents reference this file for allowable claims
- Explicit "DO NOT" rules in agent instructions
- Test results: Zero hallucination in production ✅

**User Trust:** This is non-negotiable. Breaking this trust would undermine entire system.

### GitHub as Resource Hub

**New Strategy (January 8, 2025):**
- Use GitHub for centralized resource storage
- Agents read from GitHub (product data, research, approved claims)
- Single source of truth prevents inconsistencies
- Version control tracks changes
- Prevents hallucination (reference verified data only)

**GitHub Repository Structure:**
```
HappyPawsCo/
├── brand/
│   └── approved-claims.md (verified facts only)
├── products/
│   └── product-database.json (future)
├── research/
│   └── [research files] (future)
└── blogs/
    ├── drafts/
    ├── reviewed/
    └── published/
```

**Benefits:**
- Agents access verified data only
- No fabrication of product features
- Easy updates (edit one file, all agents use it)
- Backup and version control
- Collaboration-ready

---

## Current Status

**As of January 8, 2025:**
- **Experience:** 10+ days with Claude Code (established workflows)
- **Primary Tool:** Claude Code CLI (Desktop deprecated)
- **MCP Servers:** 4 active (github, filesystem, everything, thinking)
- **Skills Installed:** 11 active skills
- **Agents Built:** 2 complete agents (Blog Publisher, Image Prompter)
- **GitHub Integration:** Authenticated and ready for resource storage
- **Context Protocol:** Established and documented
- **Major Workflows:** Make.com → Blog Publisher → Shopify pipeline

---

**This is a living document. Update as we learn and grow together.**

---

**Last Updated:** January 8, 2025
