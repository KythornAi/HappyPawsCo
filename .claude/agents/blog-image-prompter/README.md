# Blog Image Prompter - Quick Reference

## What It Does
Analyzes blog content and generates detailed AI image prompts for Google Vertex AI, Midjourney, DALL-E, or other generators. Creates SEO-optimized filenames and alt text.

---

## Quick Start

**Trigger with:**
- "Create image prompts for this blog"
- "Generate image prompts"
- "I need images for this blog"

**Then paste your blog content.**

---

## What You'll Get

For each blog, you'll receive **3-5 complete image packages:**

### 1. Hero Image (Always)
- Eye-catching blog banner
- 16:9 ratio, photorealistic
- Represents main topic

### 2. Section Images (2-3)
- Support H2 sections
- Educational/illustrative
- Break up text

### 3. Product/Infographic (If applicable)
- Products in use
- Diagrams/comparisons
- Step-by-step guides

---

## Each Image Package Includes:

```
✅ Detailed AI prompt (ready to copy/paste)
✅ Alternative prompt (backup)
✅ SEO-optimized filename
✅ Keyword-rich alt text
✅ HTML code example
✅ Placement recommendation
```

---

## Brand Aesthetic (Built-In)

All prompts follow HappyPawsCo standards:
- **Setting:** Real UK homes (not studios)
- **Lighting:** Natural, warm, bright
- **Style:** Cosy, lived-in, Scandinavian/modern farmhouse
- **Colours:** Warm neutrals (cream, beige, soft grey)
- **Quality:** Professional but authentic

---

## Image Types

### Photorealistic (Pets/Products/Lifestyle)
- Real-looking pets in UK homes
- Products in use
- Lifestyle moments
- Warm, natural photography

### Illustrations (Infographics/Diagrams)
- Process diagrams
- Comparison charts
- Step-by-step guides
- Navy, cream, coral colours

---

## Output Format

```markdown
# Image Prompts for "[Blog Title]"

## Image 1: Hero Image
**Prompt:** [Detailed Vertex AI prompt]
**Alternative:** [Backup prompt]
**Filename:** primary-keyword-hero.jpg
**Alt Text:** [Descriptive with keywords]
**Placement:** Top of blog

[Repeat for each image...]

## Quick Reference Table
[All images summarized]
```

---

## How to Use the Prompts

### For Google Vertex AI:
1. Copy "Primary Prompt"
2. Paste into Vertex AI
3. Set quality: High resolution
4. Generate 2-3 variations
5. Choose best result

### For Midjourney:
1. Copy "Alternative Prompt" (if available)
2. Add parameters: `--ar 16:9 --v 6 --style raw`
3. Use `/imagine` command
4. Upscale best version

### For DALL-E:
1. Copy "Primary Prompt"
2. Keep under 400 characters if needed
3. Generate in 1024x1024
4. Crop to recommended ratio

---

## Examples

### Cat Care Blog Gets:
- Hero: Cat in UK home setting
- Section 1: Close-up of cat paw/litter
- Section 2: Litter tray comparison
- Infographic: Mat placement diagram
- Product: Cat using grooming brush

### Dog Training Blog Gets:
- Hero: Dog training session UK living room
- Section 1: Dog responding to command
- Section 2: Training treats comparison
- Infographic: Training steps diagram
- Product: Dog wearing training collar

---

## SEO Best Practices (Automatic)

**Filenames:**
- `cat-litter-tracking-solution.jpg` ✅
- `dog-anxiety-calming-bed-uk.jpg` ✅
- `IMG_1234.jpg` ❌

**Alt Text:**
- "Grey orthopedic dog bed with sleeping retriever in UK living room" ✅
- "Dog bed picture" ❌

---

## What Makes This Agent Special

### Brand Consistency
- Every prompt matches HappyPawsCo aesthetic
- UK-specific settings and details
- Warm, inclusive, authentic vibe

### SEO Optimization
- Keywords in filenames
- Descriptive alt text
- Search-friendly structure

### Ready to Use
- Copy/paste directly into generators
- No editing needed
- Multiple format options

### Realistic Expectations
- Prompts designed for actual UK homes
- Products shown in real use
- Achievable with AI generators

---

## Tips for Best Results

1. **Provide full blog** - More context = better image selection
2. **Mention products** - Agent will create product images if relevant
3. **Note seasonal content** - Will adjust for fireworks season, Christmas, etc.
4. **Specify if needed** - "I need infographics" or "Focus on cat images"
5. **Generate variations** - Create 2-3 of each image, pick best

---

## Integration with Blog Publisher Agent

**Workflow:**
```
Write blog
    ↓
Blog Publisher Agent polishes
    ↓
Blog Image Prompter generates prompts
    ↓
Create images in Vertex AI
    ↓
Add to blog
    ↓
Publish to Shopify
```

---

## Files

- `agent.json` - Agent metadata
- `agent.md` - Full instructions and templates
- `README.md` - This quick reference

---

## Version
1.0.0 - Initial release (January 8, 2025)

---

🎨 **Your AI image prompt generator for beautiful, on-brand HappyPawsCo visuals!** ✨
