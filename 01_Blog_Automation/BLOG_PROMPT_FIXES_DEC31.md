# Blog Prompt Fixes - December 31, 2024
**Issues identified by user - to be fixed in blueprint**

---

## ISSUES TO FIX

### 1. "The good news" - Repetitive AI phrase
**Problem:** Every blog uses "the good news" which sounds repetitive and AI-generated

**Fix:** Add to BANNED GENERIC AI PHRASES section:
```
- "The good news is..."
- "Good news:"
- "The good news:"
```

**Replace with variations:**
```
✅ "What helps is..."
✅ "Something that works well is..."
✅ "Here's what makes a difference..."
✅ "What experienced owners find is..."
✅ Direct statement without setup phrase
```

---

### 2. Double quotes still appearing
**Problem:** Blogs still have ""example"" (doubled quotes)

**Current rule location:** Line ~2095 in blueprint (SHOPIFY COMPATIBILITY REQUIREMENTS section)

**Strengthen the rule:**
```
4. QUOTES IN TEXT (CRITICAL - FINAL CHECK REQUIRED):
When quoting words or phrases in your blog content, use SINGLE quotes, not double quotes.
NEVER output doubled quotes like ""this"" or ""that"".

CORRECT EXAMPLES:
✓ The term 'orthopedic' gets thrown around a lot
✓ What does 'supportive' actually mean?
✓ Some call it a 'game-changer'
✓ You can also leave words unquoted if single quotes feel awkward

FORBIDDEN EXAMPLES:
❌ The term ""orthopedic"" gets thrown around (NEVER DO THIS)
❌ What does ""supportive"" mean? (NEVER DO THIS)
❌ Use double quotes like "this" inside <p> tags (avoid - use single quotes instead)

FINAL MANDATORY CHECK BEFORE SUBMITTING:
Scan your ENTIRE blog output for any instance of:
- "" (two quote marks together)
- " followed immediately by another "
If you find ANY, you have FAILED this task and must fix them to single quotes or remove quotes entirely.

This is a CRITICAL formatting error that breaks Shopify's HTML parser.
```

---

### 3. Highway Code Rule 57 over-linked
**Problem:** Highway Code hyperlinked more than twice per blog

**Current rule location:** Line ~1941 in blueprint (MENTION LIMIT section)

**Current rule:**
```
MENTION LIMIT (KEEP IT TIGHT):
Mention "Highway Code" by name no more than 2 times in the entire blog.
```

**Strengthen to:**
```
HIGHWAY CODE MENTION & LINK LIMIT (CRITICAL):
- Mention "Highway Code" by name MAXIMUM 2 times in the entire blog
- Link it MAXIMUM 2 times (once per mention)
- After 2 mentions, refer to "Rule 57" or "the rule" or "legal requirements" WITHOUT repeating "Highway Code"
- Do NOT link Highway Code more than twice even if you mention "Rule 57" later

CORRECT PATTERN:
✓ First mention: "The <a href='https://www.gov.uk/guidance/the-highway-code'>Highway Code</a> states..."
✓ Second mention: "Under <a href='https://www.gov.uk/guidance/the-highway-code'>Highway Code</a> Rule 57..."
✓ Later mentions: "Rule 57 requires..." OR "This legal requirement..." (no link, no "Highway Code" mention)

FORBIDDEN:
❌ Linking Highway Code 3+ times
❌ Mentioning "Highway Code" 3+ times (use "Rule 57" instead)
```

---

### 4. Flatbed Back-Seat Extender missing from muddy paws content
**Problem:** Blog keeps missing the flatbed product when discussing muddy paws/mess

**Product details:**
- Name: Flatbed Back-Seat Extender
- Key benefit: Rigid surface prevents pets falling into footwell
- Use case: Longer journeys, family trips to coast, muddy paws

**Fix:** Add specific trigger in PRODUCT LINKING RULES section

**Current location:** Line ~2467 (SEAT PROTECTION TRIGGER)

**Current rule:**
```
SEAT PROTECTION TRIGGER (MUST if slot available): If the blog mentions mud, wet coats, mess, slipping, or seat protection:
- MUST link 1 hammock/cover/flatbed as comfort/cleanliness product (not restraint language)
```

**Strengthen to:**
```
SEAT PROTECTION TRIGGER (MUST if slot available): If the blog mentions mud, wet coats, mess, slipping, seat protection, or footwell safety:
- MUST link 1 seat protection product (hammock/cover/flatbed)
- PRIORITY: If "Flatbed Back-Seat Extender" exists in product list AND blog mentions muddy paws, mess, slipping, footwell, or longer journeys:
  - MUST link Flatbed product
  - MUST mention its rigid surface benefit (prevents falling into footwell)
  - Use language: "protects seats", "rigid surface", "prevents slipping into footwell", "stable platform for longer journeys"
- Alternative products (hammocks/covers) ONLY if Flatbed doesn't fit the context or isn't in product list
```

**Add specific mention in PRODUCT MATCHING section:**
```
FLATBED SPECIFIC SCENARIOS (MUST LINK if available):
- Blog mentions muddy paws + longer journeys → MUST link Flatbed
- Blog mentions footwell safety/slipping → MUST link Flatbed
- Blog mentions family trips/coast/countryside → MUST link Flatbed
- Blog mentions mess + stability → MUST link Flatbed

When linking Flatbed, include ONE of these feature sentences:
✓ "The rigid surface prevents them slipping into the footwell, especially on longer journeys."
✓ "It creates a stable platform so they can settle properly during family trips."
✓ "The flat, firm base stops muddy paws from ending up in the footwell."
```

---

### 5. How to rewrite/improve a blog
**User question:** "if i want the blog to rewrite a blog, do i just give it the same blog again? or is there a way of having it improve what it wrote before"

**Answer:**

**Option A: Full rewrite (using Make.com automation)**
- Change the blog status back to "SCHEDULED" in Google Sheets
- Run the automation again
- It will generate a completely new blog (different but following same rules)
- This gives you a fresh take, not just minor tweaks

**Option B: Manual improvements (using Claude Desktop - recommended for small edits)**
- Copy the existing blog HTML
- Paste into Claude Desktop chat
- Ask: "Please fix these issues: [list specific problems]"
- Example: "Remove all instances of 'the good news', fix any double quotes, make sure Highway Code is only linked twice"
- This is faster for targeted fixes

**Option C: Create a "blog improvement" module in Make.com (future enhancement)**
- Would need a new Make scenario
- Input: Existing blog URL or HTML
- Prompt: "Improve this blog by fixing [common issues]"
- Output: Revised HTML
- This doesn't exist yet but could be built

**Recommendation for user:**
- Quick fixes (1-3 specific issues): Use Claude Desktop (Option B)
- Want completely different angle/approach: Rerun automation (Option A)
- Batch improvements to 10+ blogs: Build improvement automation (Option C)

---

## SUMMARY OF CHANGES NEEDED IN BLUEPRINT

### Location: Line 2138 (anthropic-claude module, content field)

**Changes to make:**

1. **Add to BANNED GENERIC AI PHRASES** (around line ~1766):
```
- "The good news is..."
- "Good news:"
- "The good news:"
```

2. **Strengthen QUOTES IN TEXT rule** (around line ~2095):
Add mandatory final check and clearer examples (see full text above)

3. **Strengthen HIGHWAY CODE MENTION LIMIT** (around line ~1941):
Add explicit 2-link maximum and pattern examples (see full text above)

4. **Add FLATBED-SPECIFIC TRIGGER** (around line ~2467):
Add priority trigger for Flatbed product with specific scenarios and feature sentences (see full text above)

---

## IMPLEMENTATION STEPS

1. Open Make.com scenario: "Official Imagen Blog Automation"
2. Find the Anthropic Claude module (module after Google Sheets filter)
3. Click to edit the prompt
4. Make the 4 changes above
5. Save the scenario
6. Test with a blog about car mess/muddy paws to verify Flatbed is mentioned
7. Test with any blog to verify Highway Code only linked 2x max
8. Test to verify no "the good news" phrases appear
9. Test to verify no double quotes ""like this""

---

## TESTING CHECKLIST

After implementing fixes, test with these blog topics:

✅ **Test 1: Car mess blog**
- Should link Flatbed product
- Should mention rigid surface/footwell benefit
- Highway Code linked max 2 times
- No "the good news" phrases
- No double quotes

✅ **Test 2: Highway Code-focused blog**
- Highway Code mentioned max 2 times
- Highway Code linked max 2 times
- Later mentions use "Rule 57" or "the rule"
- No double quotes
- No "the good news" phrases

✅ **Test 3: General pet care blog**
- No "the good news" phrases
- No double quotes
- Product links appropriate to topic

---

**Status:** Ready to implement in Make.com blueprint
**Date:** December 31, 2024
**Next step:** User to update Make.com scenario with these fixes
