# HappyPawsCo Quality Standards

**Version**: 1.0  
**Effective Date**: January 10, 2026  
**Purpose**: Ensure all work is done right the first time - no shortcuts, no technical debt

---

## Core Principle

**DO IT RIGHT THE FIRST TIME**

No "we'll fix it later." No half-measures. No shortcuts that create technical debt.

If something is worth building, it's worth building correctly from the start.

---

## 1. SKILLS

### Required Structure:

```
.claude/skills/
└── skill-name/
    └── SKILL.md
```

### YAML Frontmatter (MANDATORY):

```yaml
---
name: lowercase-with-hyphens
description: Clear description with trigger keywords (max 1024 chars)
---
```

### Standards Checklist:

- [ ] File location: `.claude/skills/[name]/SKILL.md`
- [ ] Filename: `SKILL.md` (uppercase, case-sensitive)
- [ ] YAML starts at line 1 (no blank lines before `---`)
- [ ] `name:` field matches directory name exactly
- [ ] `description:` includes natural trigger keywords
- [ ] `description:` under 1024 characters
- [ ] Proper YAML syntax (closing `---` present)
- [ ] Clear, actionable instructions
- [ ] Real-world examples included

### How to Create:

**Use the Skill Creator Agent**:
- Say: "Create a skill for [purpose]"
- Agent handles all validation automatically
- Ensures proper structure from the start

**Manual Creation (NOT RECOMMENDED)**:
- Only if Skill Creator Agent unavailable
- Must follow ALL checklist items above
- Must validate YAML before saving

---

## 2. AGENTS

### Required Structure:

```
.claude/agents/
└── agent-name/
    ├── agent.json
    ├── agent.md
    └── README.md
```

### agent.json Format:

```json
{
  "name": "agent-name",
  "version": "1.0.0",
  "description": "Clear description",
  "triggers": ["trigger phrase 1", "trigger phrase 2"],
  "capabilities": ["capability 1", "capability 2"],
  "created": "YYYY-MM-DD",
  "lastUpdated": "YYYY-MM-DD"
}
```

### agent.md Requirements:

- Must have clear Purpose section
- Must have Core Workflow section
- Must have step-by-step Instructions
- Must include Examples
- Must have Quality Checklist
- Minimum 200 lines for complex agents

### README.md Requirements:

- Quick reference guide
- When to use this agent
- What it does vs. doesn't do
- Example usage
- Files documentation

### Standards Checklist:

- [ ] Location: `.claude/agents/[name]/`
- [ ] All 3 files present (agent.json, agent.md, README.md)
- [ ] Clear trigger phrases in agent.json
- [ ] Comprehensive instructions in agent.md
- [ ] No placeholders or "TODO" sections
- [ ] Examples provided
- [ ] Quality checks built-in

---

## 3. BLOGS

### Required Structure:

```
11_HappyPawsCo_Blogs/
├── drafts/2026-blogs/[blog-slug]/
│   └── draft.html
├── polished/2026-blogs/[blog-slug]/
│   ├── published.html
│   ├── image-prompts.md
│   └── images/
└── published/2026-blogs/[blog-slug]/
    ├── published.html
    ├── image-prompts.md
    └── images/
```

### Blog Quality Standards:

**SEO (Critical):**
- [ ] Title 50-60 chars with primary keyword
- [ ] Meta description 150-160 chars with CTA
- [ ] One H1 tag with keyword
- [ ] H2/H3 hierarchy logical
- [ ] Keyword density 1-2%
- [ ] 3-5 internal product links MINIMUM
- [ ] Image alt text descriptive with keywords

**Brand Voice (Critical):**
- [ ] UK English spelling (colour, behaviour, favourite)
- [ ] Warm, conversational tone
- [ ] First-person plural ("we" for brand)
- [ ] NO banned AI phrases (see AI_PHRASES_TO_AVOID.md)
- [ ] No location-based language (urban/rural)
- [ ] No academic language (canine companions, feline friends)

**Content (Critical):**
- [ ] Factually accurate
- [ ] No fabricated claims
- [ ] Safety information included
- [ ] Complete coverage of topic
- [ ] Reading level Grade 8-10

**Technical (Important):**
- [ ] Appropriate word count for topic type
- [ ] No typos or grammar errors
- [ ] All links working
- [ ] Mobile-optimized
- [ ] Images compressed (<200KB each)

### Workflow:

1. Draft from Make.com → `drafts/2026-blogs/`
2. Blog Publisher Agent polishes → `polished/2026-blogs/`
3. User reviews and approves
4. User moves to → `published/2026-blogs/`
5. User publishes to Shopify

**CRITICAL**: Blogs with ZERO product links must be flagged before polishing.

---

## 4. DOCUMENTATION

### Knowledge Base Files:

**Location**: `00_Knowledge_Base/`

**Required Files:**
- AGENTS_REFERENCE.md - All agent documentation
- AI_PHRASES_TO_AVOID.md - Banned phrases master list
- HOW_WE_WORK_TOGETHER.md - Workflows and lessons
- QUALITY_STANDARDS.md - This document
- approved-claims.md - Hallucination prevention

### Session Summaries:

**Location**: `00_Session_Summary/`

**Format**: `SESSION_HANDOVER_[DATE].md`

**Must Include:**
- What was accomplished
- What was started but not finished
- Next priorities
- Files modified
- Decisions made
- Issues found and fixed

### Standards:

- [ ] Update documentation when changes made
- [ ] No "TODO" sections left unresolved
- [ ] Clear next steps documented
- [ ] All decisions explained
- [ ] Technical debt flagged immediately

---

## 5. FILE NAMING

### General Rules:

**DO:**
- ✅ Use lowercase-with-hyphens for directories
- ✅ Use UPPERCASE for official file types (SKILL.md, README.md)
- ✅ Use descriptive names (blog-quality-checker, not bqc)
- ✅ Match YAML name fields to directory names

**DON'T:**
- ❌ Use camelCase or PascalCase for directories
- ❌ Use underscores (use hyphens)
- ❌ Use abbreviations or acronyms
- ❌ Use spaces in filenames
- ❌ Use special characters

### Specific Formats:

| File Type | Format | Example |
|-----------|--------|---------|
| Skill directory | lowercase-with-hyphens | `blog-quality-checker/` |
| Skill file | `SKILL.md` (uppercase) | `SKILL.md` |
| Agent directory | lowercase-with-hyphens | `blog-publisher/` |
| Agent files | `agent.json`, `agent.md`, `README.md` | - |
| Blog slug | lowercase-with-hyphens | `dog-paw-care-guide/` |
| Blog files | `draft.html`, `published.html` | - |
| Knowledge docs | UPPERCASE_WITH_UNDERSCORES.md | `AI_PHRASES_TO_AVOID.md` |

---

## 6. GITHUB

### Repository Structure:

```
KythornAi/HappyPawsCo/
├── brand/
│   ├── ai-phrases-to-avoid.md
│   ├── approved-claims.md
│   └── README.md
├── products/
├── research/
└── blogs/
    ├── drafts/2026-blogs/
    ├── polished/2026-blogs/
    └── published/2026-blogs/
```

### Commit Standards:

**Format**: `[Action] [Component] - [Brief description]`

**Examples:**
- ✅ `Add AI phrases style guide - comprehensive banned phrases reference`
- ✅ `Update Blog Publisher Agent - add banned phrases section`
- ✅ `Fix blog folder structure - centralize in 11_HappyPawsCo_Blogs`

**DON'T:**
- ❌ `update` (too vague)
- ❌ `fix stuff` (not descriptive)
- ❌ `WIP` (don't commit unfinished work)

### Branch Strategy:

**Current**: All commits to `main` branch (solo project)  
**Future**: May add feature branches when team grows

---

## 7. QUALITY ENFORCEMENT

### Built-In Safeguards:

1. **Skill Creator Agent** - Ensures all new skills have proper YAML
2. **Blog Publisher Agent** - Removes banned AI phrases automatically
3. **Blog Quality Checker Skill** - Pre-publish validation
4. **Quality Standards Document** - This document (central reference)

### Manual Checks:

Before committing work:
- [ ] Run through relevant checklist above
- [ ] Verify file structure is correct
- [ ] Check YAML frontmatter (if applicable)
- [ ] Confirm no "TODO" or placeholder sections
- [ ] Validate all links work
- [ ] Test that it works as intended

### Red Flags (Stop and Fix):

🚨 "We'll fix this later"  
🚨 "Good enough for now"  
🚨 "TODO: add [critical component]"  
🚨 Missing YAML frontmatter  
🚨 Files in wrong location  
🚨 Inconsistent naming  
🚨 Incomplete documentation  

**If you see these: STOP. Fix it now.**

---

## 8. TECHNICAL DEBT POLICY

**Policy**: ZERO TOLERANCE

**Definition**: Technical debt is any shortcut, incomplete work, or "we'll fix it later" decision that creates future work.

**Prevention**:
1. Do it right the first time
2. Use quality enforcement agents
3. Follow all checklists
4. Document everything
5. No placeholders in production code

**If Technical Debt is Created**:
1. Flag it immediately in session summary
2. Add to todo list with HIGH priority
3. Fix before moving to next task
4. Document what went wrong
5. Update standards to prevent recurrence

---

## 9. FOLDER STRUCTURE STANDARDS

### Root-Level Organization:

```
/Volumes/Home Ext/Home Ext/Desktop/Claude/
├── .claude/
│   ├── agents/              # Official agents
│   └── skills/              # Official skills
├── 00_Knowledge_Base/       # Reference docs
├── 00_Session_Summary/      # Handover docs
├── 01_Blog_Automation/      # Make.com files
├── 11_HappyPawsCo_Blogs/    # All blog content
├── HPC_Trust_Badges/        # Trust badge assets
└── Skills/                  # OLD - to be removed after verification
```

### What Goes Where:

| Content Type | Location |
|--------------|----------|
| Agents | `.claude/agents/` |
| Skills | `.claude/skills/` |
| Blog drafts | `11_HappyPawsCo_Blogs/drafts/2026-blogs/` |
| Blog polished | `11_HappyPawsCo_Blogs/polished/2026-blogs/` |
| Blog published | `11_HappyPawsCo_Blogs/published/2026-blogs/` |
| Reference docs | `00_Knowledge_Base/` |
| Session notes | `00_Session_Summary/` |
| Make.com files | `01_Blog_Automation/` |

**Rule**: Each item has ONE correct location. No duplicates, no scattered files.

---

## 10. WHEN TO UPDATE THIS DOCUMENT

Update QUALITY_STANDARDS.md when:

- New file type is introduced
- New quality issue is discovered
- Standards are refined based on lessons learned
- New tools/agents/processes are added
- Technical debt is prevented by new safeguard

**Version History**:
- v1.0 (Jan 10, 2026): Initial standards based on skills migration and blog publisher enhancement

---

## REMEMBER

**Quality is not negotiable.**

Every shortcut creates future work. Every "we'll fix it later" becomes technical debt. Every half-measure compounds.

Do it right the first time, every time.

---

**Maintained By**: Claude Code Team  
**Last Updated**: January 10, 2026  
**Status**: ✅ ACTIVE
