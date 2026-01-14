# Blog Publisher Agent - Quick Reference

## What It Does
Takes blog drafts and transforms them into polished, Shopify-ready HTML while maintaining factual accuracy.

---

## Quick Start

**Trigger the agent with any of these phrases:**
- "Publish this blog"
- "Prepare blog for Shopify"
- "Review and fix this blog"
- "Make blog Shopify-ready"
- "Polish this blog"

**Then paste your blog content.**

---

## What Gets Fixed

### ✅ Automatically Corrected
- SEO (titles, headers, meta descriptions, keywords)
- Brand voice (UK English, tone, first-person plural)
- Grammar and spelling
- Content structure (headings, paragraphs, lists)
- HTML formatting for Shopify
- Image optimization (filenames, alt text)
- Internal product links

### ❌ Never Added (Hallucination Prevention)
- New facts or statistics not in original
- Fabricated claims or product features
- Made-up quotes or testimonials
- Personal anecdotes not in original
- Medical claims or diagnoses
- Unverified competitor comparisons

---

## Output You'll Receive

1. **Clean Shopify HTML** - Ready to copy/paste
2. **Changes Summary** - What was fixed and why
3. **Flags** - Issues that need your attention
4. **Metadata** - Title, description, keywords for Shopify settings

---

## Example Usage

```
You: "Publish this blog"

[Paste blog content from Make.com]

Agent:
- Analyzes with blog-quality-checker skill
- Fixes 8 issues (3 SEO, 2 brand voice, 3 formatting)
- Outputs Shopify-ready HTML
- Shows what changed
- Flags any gaps
```

---

## Quality Safeguards

**Conservative Approach:**
- Polishes existing content
- Never invents new facts
- Flags missing research instead of fabricating
- References approved-claims.md for verified facts only

**Brand Standards:**
- UK English spelling (colour, behaviour, favourite)
- Warm, empathetic, conversational tone
- First-person plural ("we", "our")
- Safety-focused
- Inclusive (dogs AND cats)

---

## Requirements

**Required Skill:**
- `blog-quality-checker` ✅ (installed)

**Optional Resources:**
- `approved-claims.md` from GitHub (verified facts reference)

---

## Common Scenarios

**Scenario 1: Blog from Make.com is 90% ready**
→ Quick polish, minor SEO fixes, output HTML in 2-3 minutes

**Scenario 2: Blog needs structural improvements**
→ Fix headings, break paragraphs, add lists, format properly

**Scenario 3: Blog missing research/facts**
→ Flag the gaps, DON'T fabricate, polish what's there

**Scenario 4: Brand voice is off**
→ Convert to UK English, adjust tone, ensure compliance

---

## Tips for Best Results

1. **Provide complete drafts** - Agent polishes, doesn't write from scratch
2. **Keep research in draft** - Agent preserves facts, won't add new ones
3. **Review flags** - Agent will note anything it couldn't fix
4. **Check internal links** - Verify product links are correct
5. **Use approved-claims.md** - Upload verified facts to GitHub for reference

---

## What Success Looks Like

**Before (Make.com draft):**
- Good content, minor issues
- Inconsistent formatting
- Missing meta tags
- Some brand voice inconsistencies

**After (Blog Publisher Agent):**
- ✅ SEO optimized (title, meta, keywords, headers)
- ✅ Perfect brand voice (UK English, warm tone)
- ✅ Clean Shopify HTML
- ✅ Proper structure (H1, H2, H3, lists)
- ✅ Internal product links
- ✅ Image alt text optimized
- ✅ Ready to publish immediately

---

## Files

- `agent.json` - Agent metadata and configuration
- `agent.md` - Full instructions and guidelines (detailed)
- `README.md` - This quick reference guide

---

## Version
1.0.0 - Initial release (January 8, 2025)

---

## Support

For issues or improvements, discuss with Claude in your working session.

---

🐾 **Ready to make your blogs shine!** ✨
