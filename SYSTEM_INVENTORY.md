# HappyPawsCo Claude Code System Inventory

**Last Updated**: January 11, 2026
**Purpose**: Complete reference of all skills, agents, and their locations

---

## How to View Hidden .claude Folder

The official Claude Code files are in `.claude/` (hidden folder).

### Option 1: VS Code (RECOMMENDED - You're already using it!)
VS Code shows hidden folders by default. In your VS Code sidebar, you can see:
- `.claude/skills/` - All 11 skills
- `.claude/agents/` - All 3 agents

Just click the folder to expand and edit any file.

### Option 2: Terminal
```bash
# Navigate to Claude directory
cd "/Volumes/Home Ext/Home Ext/Desktop/Claude"

# List all skills
ls -1 .claude/skills/

# List all agents  
ls -1 .claude/agents/

# Open a specific skill in VS Code
code .claude/skills/blog-quality-checker/SKILL.md
```

### Option 3: Finder (If needed)
Press `Command + Shift + .` in Finder to toggle hidden files visibility.

---

## 📚 ALL SKILLS (11 Total)

**Location**: `.claude/skills/`
**Structure**: Each skill has ONE file: `SKILL.md` (with YAML frontmatter)

| # | Skill Name | Purpose | File Path |
|---|------------|---------|-----------|
| 1 | blog-quality-checker | Pre-publish review system for HappyPawsCo blogs | `.claude/skills/blog-quality-checker/SKILL.md` |
| 2 | competitive-ads-extractor | Extract and analyze competitor ads from ad libraries | `.claude/skills/competitive-ads-extractor/SKILL.md` |
| 3 | content-calendar-planner | Strategic content planning across blogs, Pinterest, product launches | `.claude/skills/content-calendar-planner/SKILL.md` |
| 4 | content-research-writer | Research, outline, draft, and refine content with citations | `.claude/skills/content-research-writer/SKILL.md` |
| 5 | file-organizer | Intelligently organize files and folders | `.claude/skills/file-organizer/SKILL.md` |
| 6 | lead-magnet-creator | Create professional lead magnets (PDFs, slide decks, guides) | `.claude/skills/lead-magnet-creator/SKILL.md` |
| 7 | lead-research-assistant | Identify high-quality leads for products/services | `.claude/skills/lead-research-assistant/SKILL.md` |
| 8 | pinterest-health-check | Validate Pinterest automation configuration | `.claude/skills/pinterest-health-check/SKILL.md` |
| 9 | pinterest-pin-creator | Create effective Pinterest pins for lead magnet campaigns | `.claude/skills/pinterest-pin-creator/SKILL.md` |
| 10 | product-copy-writer | Brand voice copywriting for product descriptions | `.claude/skills/product-copy-writer/SKILL.md` |
| 11 | seo-blog-optimizer | Comprehensive SEO optimization for blog content | `.claude/skills/seo-blog-optimizer/SKILL.md` |

---

## 🤖 ALL AGENTS (3 Total)

**Location**: `.claude/agents/`
**Structure**: Each agent has `agent.json`, `agent.md`, and `README.md`

| # | Agent Name | Purpose | Config | Instructions |
|---|------------|---------|--------|--------------|
| 1 | blog-publisher | Polishes draft blogs to HappyPawsCo standards | `.claude/agents/blog-publisher/agent.json` | `.claude/agents/blog-publisher/agent.md` |
| 2 | blog-image-prompter | Generates AI image prompts for blog headers | `.claude/agents/blog-image-prompter/agent.json` | `.claude/agents/blog-image-prompter/agent.md` |
| 3 | skill-creator | Creates new skills with proper YAML structure | `.claude/agents/skill-creator/agent.json` | `.claude/agents/skill-creator/agent.md` |

---

## 📂 Blog Structure

**Location**: `11_HappyPawsCo_Blogs/`

```
11_HappyPawsCo_Blogs/
├── drafts/2026-blogs/          ← 9 draft blogs awaiting processing
├── polished/2026-blogs/        ← 2 polished blogs ready for review
└── published/2026-blogs/       ← 1 published blog (live on Shopify)
```

**Drafts (9 blogs)**:
1. clean-slow-feeder-dog-bowl/
2. dog-dental-health-uk-vet-guide/
3. dog-highway-code-car-safety/
4. dog-car-seat-cover-muddy-paws/
5. measure-dog-harness-step-by-step/
6. new-year-pet-travel-resolutions/
7. orthopedic-support-road-trips/
8. protect-dog-paws-seasonal-hazards/
9. stop-cat-litter-tracking-guide/ (CAT blog)

**Polished (2 blogs - awaiting your review)**:
1. protect-dog-paws-seasonal-hazards/ ✅ Ready
2. clean-slow-feeder-dog-bowl/ ⚠️ Needs product links added

**Published (1 blog)**:
1. cat-litter-tracking-solutions/ (Live on Shopify)

---

## 🔧 MCP Servers (4 Active)

1. **github** - GitHub repository management
2. **filesystem** - File operations
3. **everything** - Testing/demonstration server
4. **thinking** - Sequential thinking for complex problems

---

## 📖 Knowledge Base Files

**Location**: `00_Knowledge_Base/`

- `AI_PHRASES_TO_AVOID.md` - Master list of banned AI phrases
- `AGENTS_REFERENCE.md` - Agent documentation
- `HOW_WE_WORK_TOGETHER.md` - Workflow documentation
- `HappyPawsCo_Research_Brief_Condensed.md` - Research database
- `QUALITY_STANDARDS.md` - Quality standards for all work

---

## 🎯 Quick Commands

### View All Skills
```bash
ls -1 "/Volumes/Home Ext/Home Ext/Desktop/Claude/.claude/skills/"
```

### Open a Skill in VS Code
```bash
code "/Volumes/Home Ext/Home Ext/Desktop/Claude/.claude/skills/blog-quality-checker/SKILL.md"
```

### View All Agents
```bash
ls -1 "/Volumes/Home Ext/Home Ext/Desktop/Claude/.claude/agents/"
```

### Check Blog Status
```bash
# Drafts
ls -1 "/Volumes/Home Ext/Home Ext/Desktop/Claude/11_HappyPawsCo_Blogs/drafts/2026-blogs/"

# Polished
ls -1 "/Volumes/Home Ext/Home Ext/Desktop/Claude/11_HappyPawsCo_Blogs/polished/2026-blogs/"
```

---

## ✅ Verification Status

- [x] All 11 skills standardized to `SKILL.md` only
- [x] All skills have proper YAML frontmatter
- [x] All unnecessary files removed (skill.json, README.md)
- [x] All skills in official `.claude/skills/` location
- [x] All 3 agents properly structured
- [x] Blog workflow folders organized
- [ ] Test skills after Claude Code restart (your action)
- [ ] Remove old `/Skills/` folder after verification (your action)

---

## 🚀 Next Steps

1. **Verify in VS Code**: Open `.claude/skills/` in your VS Code sidebar - you should see all 11 skill folders
2. **Test a Skill**: Try invoking a skill to ensure it works (e.g., ask me to review blog quality)
3. **Review Polished Blogs**: Check the 2 blogs in `polished/2026-blogs/`
4. **Remove Old Folder**: Delete `/Skills/` folder once you verify everything works

---

**All files are in the correct official Claude Code locations and ready to use.**
