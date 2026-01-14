# Recommended MCPs and Skills for HappyPawsCo
**Purpose:** Essential tools to enhance Claude's capabilities
**Created:** December 29, 2024
**Updated:** January 8, 2025
**Status:** Active Installation + Recommendations

---

## ✅ Currently Active (January 8, 2025)

### MCP Servers (4 Installed & Configured)

1. **github** ✅ ACTIVE
   - Full repository access
   - Read/write capabilities
   - Authentication configured
   - Used for: Resource storage, version control

2. **filesystem** ✅ ACTIVE
   - Local file operations
   - Working directory: `/Volumes/Home Ext/Home Ext/Desktop/Claude`
   - Used for: Agents, skills, local resources

3. **everything** ✅ ACTIVE
   - Testing and demonstration server
   - Protocol feature testing
   - Used for: MCP protocol validation

4. **thinking** ✅ ACTIVE
   - Sequential thinking for complex problems
   - Chain-of-thought reasoning
   - Used for: Complex problem-solving

**Configuration Location:** `/Volumes/Home Ext/Home Ext/.claude.json`

### Skills (11 Installed & Active)

**Custom Skills (7):**
1. ✅ pinterest-health-check
2. ✅ lead-magnet-creator
3. ✅ pinterest-pin-creator
4. ✅ product-copy-writer
5. ✅ content-calendar-planner (cat/dog balance)
6. ✅ seo-blog-optimizer (cat keyword focus)
7. ✅ blog-quality-checker (pre-publish review)

**Marketplace Skills (4 from ComposioHQ):**
8. ✅ content-research-writer (blog research + citations)
9. ✅ file-organizer (smart asset management)
10. ✅ competitive-ads-extractor (Pinterest inspiration)
11. ✅ lead-research-assistant (find pet owner audiences)

**Skills Location:** `.claude/skills/` + `Skills/` (mirrored)

### Agents (2 Built & Tested)

1. **blog-publisher** ✅ COMPLETE
   - Location: `.claude/agents/blog-publisher/`
   - Purpose: Polish Make.com blogs for Shopify
   - Status: Tested successfully, zero hallucination
   - Processing: ~5 min per blog

2. **blog-image-prompter** ✅ COMPLETE
   - Location: `.claude/agents/blog-image-prompter/`
   - Purpose: Generate AI image prompts for Vertex AI
   - Status: Ready to use
   - Output: 3-5 prompts per blog with SEO metadata

---

## What Are MCPs and Skills?

### MCPs (Model Context Protocols)
- **What:** Tools that extend Claude's capabilities
- **How:** Installed via command line or Cursor settings
- **Benefit:** Claude can do more (generate PDFs, access APIs, etc.)
- **Example:** Document Generator MCP creates PDFs directly

### Skills
- **What:** Reusable knowledge/instructions for Claude
- **How:** Downloaded from GitHub or Claude marketplace
- **Benefit:** Pre-built workflows and best practices
- **Example:** Content creation skills with proven templates

---

---

## 📋 Recommended MCPs (Not Yet Installed)

### 1. Document Generator MCP ⭐ TOP PRIORITY (NOT INSTALLED)

**What It Does:**
- Generates Word (.docx) and PDF documents directly from Claude
- No manual export needed
- Professional formatting

**Why You Need It:**
- Create lead magnets as PDFs instantly
- Generate slide decks automatically
- Save hours of manual formatting

**Installation:**
```bash
npx document-generator-mcp@latest
```

**Use Cases:**
- "Create a 7-page lead magnet PDF about winter car safety"
- "Generate a slide deck from this content"
- "Convert this markdown to a formatted PDF"

**Source:** [Document Generator MCP](https://mcpservers.org/servers/thiagotw10/document-generator-mcp)

---

### 2. Pandoc MCP Server ⭐ HIGH PRIORITY (NOT INSTALLED)

**What It Does:**
- Universal document converter (Markdown → PDF, DOCX, HTML, etc.)
- More formatting control than Document Generator
- Template support

**Why You Need It:**
- Better formatting control for lead magnets
- Template-based workflows
- Multiple output formats

**Installation:**
```bash
# Install Pandoc first
brew install pandoc

# Then install MCP server
npm install -g mcp-pandoc
```

**Use Cases:**
- "Convert this markdown to PDF using my template"
- "Generate HTML version of this guide"
- "Create DOCX with custom formatting"

**Source:** [Pandoc MCP Server](https://www.pulsemcp.com/servers/vivekvells-mcp-pandoc)

---

### 3. Image Generation MCP (If Available)

**What It Does:**
- Generates images from text prompts
- Integrates with Imagen, DALL-E, or Midjourney
- Batch processing

**Why You Need It:**
- Create Pinterest pin images automatically
- Generate product photography
- Consistent image style

**Status:** Check MCP marketplace for current options
**Alternative:** Use Google Vertex AI (Imagen) directly via Make.com

---

## Recommended Skills (Download These)

### 1. Claude Office Skills ⭐ ESSENTIAL

**What It Does:**
- Official skills for DOCX, PPTX, XLSX, and PDF creation
- Maximum formatting control
- Template-based workflows

**Why You Need It:**
- Professional document generation
- Full control over formatting
- Reusable templates

**Installation:**
```bash
cd "/Volumes/Home Ext/Home Ext/Desktop/Claude/Skills"
git clone https://github.com/tfriedel/claude-office-skills.git
```

**Use Cases:**
- Create branded Word templates
- Generate PowerPoint presentations
- Export to PDF with perfect formatting

**Source:** [Claude Office Skills](https://github.com/tfriedel/claude-office-skills)

---

### 2. Awesome Claude Skills Collections

**What They Do:**
- Curated collections of real-world skills
- Content creation workflows
- Marketing & SEO skills
- Brand voice analysis

**Why You Need Them:**
- See how others structure skills
- Steal patterns that work
- Adapt for HappyPawsCo
- Save hours of experimentation

**Installation:**
```bash
cd "/Volumes/Home Ext/Home Ext/Desktop/Claude/Skills"
git clone https://github.com/travisvn/awesome-claude-skills.git
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
git clone https://github.com/automationcreators/claude-code-skills.git
```

**What You'll Find:**
- Content creation workflows
- Marketing frameworks
- SEO optimization
- Brand voice templates
- Platform-specific guides

**Sources:**
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [automationcreators/claude-code-skills](https://github.com/automationcreators/claude-code-skills)

---

### 3. PDF Skill (Anthropic Official)

**What It Does:**
- Extract text and tables from PDFs
- Merge/split PDFs
- Analyze PDF content

**Why You Need It:**
- Analyze competitor PDFs
- Extract content from research
- Process existing documents

**Installation:**
- Check Claude marketplace or Anthropic documentation
- May be built into Cursor already

**Use Cases:**
- "Extract key points from this PDF"
- "Merge these PDFs into one document"
- "What does this PDF say about [topic]?"

---

### 4. Web Search MCP (If Available)

**What It Does:**
- Search the web for current information
- Access real-time data
- Research topics

**Why You Need It:**
- Current SEO research
- Competitor analysis
- Industry trends
- UK-specific information

**Status:** Check MCP marketplace
**Alternative:** Use web_search tool (may already be available)

---

## Installation Priority

### Phase 1: Essential (Do First)
1. ✅ **Document Generator MCP** - For lead magnets
2. ✅ **Claude Office Skills** - For document templates
3. ✅ **Awesome Claude Skills** - For inspiration and patterns

**Time:** 15-20 minutes

### Phase 2: Important (Do Next)
4. ✅ **Pandoc MCP Server** - For advanced formatting
5. ✅ **PDF Skill** - For document analysis

**Time:** 10-15 minutes

### Phase 3: Nice to Have (Add Later)
6. ✅ **Image Generation MCP** - If available
7. ✅ **Web Search MCP** - If available
8. ✅ **Other specialized MCPs** - As needed

**Time:** Varies

---

## How to Install MCPs in Cursor

### Method 1: Command Line (Recommended)

1. **Open Terminal in Cursor:**
   - View → Terminal (or Cmd+`)

2. **Install MCP:**
   ```bash
   npx document-generator-mcp@latest
   ```

3. **Follow prompts:**
   - May ask for configuration
   - May need to restart Cursor

### Method 2: Cursor Settings

1. **Open Settings:**
   - Cursor → Settings → Features → MCP

2. **Add MCP:**
   - Click "Add MCP"
   - Enter MCP name and configuration
   - Save

3. **Restart Cursor:**
   - May be required for MCPs to load

---

## How to Install Skills

### From GitHub:

1. **Navigate to Skills folder:**
   ```bash
   cd "/Volumes/Home Ext/Home Ext/Desktop/Claude/Skills"
   ```

2. **Clone repository:**
   ```bash
   git clone https://github.com/user/repo-name.git
   ```

3. **Verify installation:**
   - Check that folder appears in Skills directory
   - Files should include skill.json, skill.md, README.md

### From Claude Marketplace:

1. **Open Claude marketplace** (if available)
2. **Browse skills**
3. **Click "Install"**
4. **Follow prompts**

---

## Testing Your Installations

### Test Document Generator MCP:
```
Ask Claude: "Create a test PDF with the title 'Test Document' and some sample content"
```

### Test Claude Office Skills:
```
Ask Claude: "Create a Word document template for a lead magnet"
```

### Test Skills:
```
Ask Claude: "Use the content creation skill to help me write a blog post"
```

---

## Troubleshooting

### MCP Not Working:
1. **Check installation:**
   - Verify command completed successfully
   - Check for error messages

2. **Restart Cursor:**
   - Close and reopen Cursor
   - MCPs load on startup

3. **Check Cursor settings:**
   - Settings → Features → MCP
   - Verify MCP is listed and enabled

4. **Check logs:**
   - View → Output → MCP
   - Look for error messages

### Skills Not Loading:
1. **Check folder structure:**
   - Skills should be in `/Skills/` folder
   - Each skill needs skill.json file

2. **Verify file format:**
   - skill.json must be valid JSON
   - Check for syntax errors

3. **Restart Cursor:**
   - Skills are loaded on startup

---

## Recommended Installation Order

### Today (Quick Setup):
1. Document Generator MCP (5 mins)
2. Claude Office Skills (5 mins)
3. Test both (5 mins)

**Total: 15 minutes**

### This Week (Full Setup):
4. Pandoc MCP Server (10 mins)
5. Awesome Claude Skills collections (10 mins)
6. PDF Skill if available (5 mins)
7. Test everything (10 mins)

**Total: 35 minutes**

### Ongoing (As Needed):
8. Image Generation MCP (when available)
9. Web Search MCP (if needed)
10. Other specialized MCPs (as projects require)

---

## Quick Reference: Installation Commands

```bash
# Navigate to workspace
cd "/Volumes/Home Ext/Home Ext/Desktop/Claude"

# Install Document Generator MCP
npx document-generator-mcp@latest

# Install Pandoc (if not already installed)
brew install pandoc

# Install Pandoc MCP Server
npm install -g mcp-pandoc

# Navigate to Skills folder
cd Skills

# Clone Claude Office Skills
git clone https://github.com/tfriedel/claude-office-skills.git

# Clone Awesome Skills Collections
git clone https://github.com/travisvn/awesome-claude-skills.git
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
git clone https://github.com/automationcreators/claude-code-skills.git
```

---

## Next Steps

1. ✅ **Install Phase 1 MCPs** (Document Generator, Claude Office Skills)
2. ✅ **Test installations** (create a test PDF)
3. ✅ **Install Phase 2** (Pandoc, PDF Skill)
4. ✅ **Explore skills** (browse awesome-claude-skills)
5. ✅ **Start using** (create your first lead magnet with MCPs!)

---

**Last Updated:** January 8, 2025
**Status:**
- ✅ 4 MCPs Active
- ✅ 11 Skills Active
- ✅ 2 Agents Complete
- 📋 Document Generator & Pandoc recommended for future

