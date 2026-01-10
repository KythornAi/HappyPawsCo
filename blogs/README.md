# HappyPawsCo Blog Organization

## Folder Structure

```
blogs/
├── drafts/
│   └── 2026-blogs/          # Blogs waiting to be polished
├── polished/
│   └── 2026-blogs/          # Agent-polished blogs awaiting review
└── published/
    └── 2026-blogs/          # Final approved blogs (ready for/live on Shopify)
```

## Workflow

### Step 1: Draft Blog
**Location**: `blogs/drafts/2026-blogs/`

**What goes here:**
- Older blogs from Make.com experiments (early 2025)
- New blogs from current Make.com automation
- The 5 existing blogs on pre-launch site
- Any blog content needing polish

**File naming**: `blog-title-slug.md` or `blog-title-slug.html`

---

### Step 2: Polish with Blog Publisher Agent
**Location**: Local or via agent

**Process:**
1. Run Blog Publisher Agent on draft
2. Agent checks for:
   - SEO optimization
   - UK English spelling
   - Brand voice compliance
   - Banned AI phrases removal
   - Grammar and structure
   - Internal product links
3. Agent outputs polished HTML

---

### Step 3: Agent Output
**Location**: `blogs/polished/2026-blogs/`

**What goes here:**
- Blog Publisher Agent outputs
- Ready for your proofread
- Includes changes summary from agent

**Your task**: Review and proofread

---

### Step 4: Final Approval
**Location**: `blogs/published/2026-blogs/`

**What goes here:**
- Blogs you've reviewed and approved
- Ready to publish to Shopify
- Archive of live content

**You manually move** files from polished/ to published/ after review

---

## Future Automation

When we build Shopify auto-publishing:
- Blogs in `published/` folder will auto-sync to Shopify
- Until then, you manually copy/paste to Shopify after moving to published/

---

## Year Folders

**2026**: Launch year - all current blogs
- Includes pre-launch blogs (treated as 2026 since first public viewing is 2026)
- All Make.com experiment blogs from 2025

**Future years**: Add 2027-blogs/, 2028-blogs/ as needed

---

## Quality Standards

All blogs must meet HappyPawsCo standards before moving to published/:

✅ SEO optimized (title, meta, headers, keywords)
✅ UK English spelling (colour, behaviour, favourite)
✅ Warm, conversational brand voice
✅ NO banned AI phrases (see `brand/ai-phrases-to-avoid.md`)
✅ No location-based language (urban/rural)
✅ Proper HTML structure
✅ Internal product links (2-3 minimum)
✅ No fabricated facts or claims
✅ Cat/dog balance maintained

---

## Related Resources

- **AI Phrases Guide**: `brand/ai-phrases-to-avoid.md`
- **Approved Claims**: `brand/approved-claims.md`
- **Blog Publisher Agent**: `.claude/agents/blog-publisher/agent.md`
- **Image Prompter Agent**: `.claude/agents/blog-image-prompter/agent.md`

---

🐾 **Remember**: Quality over speed. Every blog represents HappyPawsCo's commitment to helping pet families.