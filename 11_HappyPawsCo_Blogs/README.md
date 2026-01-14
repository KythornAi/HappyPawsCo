# HappyPawsCo Blogs

Complete blog management system for HappyPawsCo content.

## Folder Structure

```
11_HappyPawsCo_Blogs/
├── drafts/
│   └── 2026-blogs/          # Raw blogs waiting to be polished
│       └── [blog-slug]/
│           ├── draft.md
│           ├── image-prompts.md (optional)
│           └── images/ (optional)
├── polished/
│   └── 2026-blogs/          # Agent-polished blogs awaiting review
│       └── [blog-slug]/
│           ├── published.html
│           ├── image-prompts.md
│           └── images/
└── published/
    └── 2026-blogs/          # Final approved blogs (ready for/live on Shopify)
        └── [blog-slug]/
            ├── published.html
            ├── image-prompts.md
            └── images/
```

## Complete Workflow

### Stage 1: Draft
**Location**: `drafts/2026-blogs/[blog-slug]/`

**What goes here:**
- Raw blogs from Make.com automation
- Older blogs from early Make.com experiments
- The 5 existing blogs on pre-launch site
- Any blog content needing polish

**Folder contents:**
- `draft.md` - Raw blog content
- `image-prompts.md` - (optional) If already generated
- `images/` - (optional) If images already created

---

### Stage 2: Polish with Blog Publisher Agent
**How to use:**
1. Point Blog Publisher Agent to draft file
2. Agent analyzes and polishes:
   - SEO optimization
   - UK English spelling
   - Brand voice compliance
   - Removes banned AI phrases
   - Grammar and structure
   - Adds internal product links
3. Agent outputs ready-to-publish HTML

---

### Stage 3: Polished Output
**Location**: `polished/2026-blogs/[blog-slug]/`

**What goes here:**
- Blog Publisher Agent output (HTML)
- Image prompts from Image Prompter Agent
- Images from Vertex AI (when created)

**Your task:** Proofread and review

**Folder contents:**
- `published.html` - Polished blog from agent
- `image-prompts.md` - Image prompts for Vertex AI
- `images/` - Generated images ready for blog

---

### Stage 4: Published
**Location**: `published/2026-blogs/[blog-slug]/`

**What goes here:**
- Blogs you've reviewed and approved
- Currently live on Shopify OR ready to publish
- Complete archive of all blog assets

**You manually move** entire blog folder from polished/ to published/ after review

**Folder contents:**
- `published.html` - Final approved HTML
- `image-prompts.md` - Image prompt reference
- `images/` - All blog images

---

## Example Blog Folder

```
cat-litter-tracking-solutions/
├── draft.md                  # Original from Make.com
├── published.html            # Polished by Blog Publisher Agent
├── image-prompts.md          # From Image Prompter Agent
└── images/
    ├── cat-litter-tracking-solution-uk-home.png
    ├── crystal-vs-clay-cat-litter-comparison.png
    ├── litter-tracking-mat-product-showcase.png
    ├── top-entry-litter-box-demonstration.png
    └── cat-litter-box-placement-diagram.png
```

---

## Quality Standards

All blogs must meet HappyPawsCo standards before moving to published/:

✅ SEO optimized (title, meta, headers, keywords)
✅ UK English spelling (colour, behaviour, favourite)
✅ Warm, conversational brand voice
✅ NO banned AI phrases (see `00_Knowledge_Base/AI_PHRASES_TO_AVOID.md`)
✅ No location-based language (urban/rural)
✅ Proper HTML structure
✅ Internal product links (2-3 minimum)
✅ No fabricated facts or claims
✅ Cat/dog balance maintained
✅ Images with SEO filenames and alt text

---

## Related Resources

**Agents:**
- Blog Publisher Agent: `.claude/agents/blog-publisher/`
- Blog Image Prompter Agent: `.claude/agents/blog-image-prompter/`

**Style Guides:**
- AI Phrases to Avoid: `00_Knowledge_Base/AI_PHRASES_TO_AVOID.md`
- Approved Claims: `00_Knowledge_Base/approved-claims.md`
- How We Work Together: `00_Knowledge_Base/HOW_WE_WORK_TOGETHER.md`

**Automation:**
- Make.com Blueprint: `01_Blog_Automation/FIXED_Quotes_And_Stats_Blog_Automation.blueprint.json`

---

## Future Automation

When we build Shopify auto-publishing:
- Blogs in `published/` folder will auto-sync to Shopify
- Until then, manually copy/paste HTML to Shopify after moving to published/

---

## Year Folders

**2026**: Launch year - all current blogs
- Includes pre-launch blogs (treated as 2026 since first public viewing is 2026)
- All Make.com experiment blogs from 2025

**Future years**: Add 2027-blogs/, 2028-blogs/ folders as needed

---

🐾 **Remember**: Quality over speed. Every blog represents HappyPawsCo's commitment to helping pet families.
