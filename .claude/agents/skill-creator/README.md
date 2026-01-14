# Skill Creator Agent

**Version**: 1.0.0  
**Created**: January 10, 2026  
**Purpose**: Ensures all new skills are created with proper YAML frontmatter and official structure from the start

---

## Why This Agent Exists

**Problem**: Previously, skills were created inconsistently:
- Some had YAML frontmatter, some didn't
- Some in `/Skills/`, some in `.claude/skills/`
- Some used `skill.md`, some used `SKILL.md`
- This created technical debt and required manual fixes

**Solution**: This agent creates skills correctly THE FIRST TIME.

---

## How to Use

**Trigger phrases:**
- "Create a new skill for [purpose]"
- "Build a skill that [does X]"
- "Make a skill to [solve Y]"
- "Create skill"
- "New skill"

**What happens:**
1. Agent asks clarifying questions
2. Generates proper skill name (lowercase-with-hyphens)
3. Writes clear description with trigger keywords
4. Creates YAML frontmatter with validation
5. Writes comprehensive skill content
6. Saves to `.claude/skills/[name]/SKILL.md`
7. Validates everything before confirming

---

## Quality Guarantees

Every skill created by this agent will have:

✅ Proper YAML frontmatter starting at line 1  
✅ Official `.claude/skills/` location  
✅ `SKILL.md` filename (uppercase, case-sensitive)  
✅ Directory name matching YAML `name:` field  
✅ Description with trigger keywords  
✅ Clear, actionable instructions  
✅ Real-world examples  
✅ Validation before saving  

---

## Example

**User**: "Create a skill for checking blog post readability"

**Agent Output**:

**File**: `.claude/skills/blog-readability-checker/SKILL.md`

```markdown
---
name: blog-readability-checker
description: Analyzes blog post readability and reading level. Check readability, analyze reading level, improve clarity, simplify language, assess comprehension difficulty.
---

# Blog Readability Checker

[Full skill content with purpose, instructions, examples...]
```

**Result**: Skill works immediately, no fixes needed.

---

## What Makes This Different

**Before this agent:**
- Skills created manually
- YAML often forgotten
- Structure inconsistent
- Required cleanup later

**With this agent:**
- Automated creation process
- YAML guaranteed
- Structure always correct
- Zero technical debt

---

## Files

- `agent.json` - Agent metadata and triggers
- `agent.md` - Comprehensive creation instructions (this is the "brain")
- `README.md` - This file (quick reference)

---

**Status**: ✅ ACTIVE  
**Last Updated**: January 10, 2026
