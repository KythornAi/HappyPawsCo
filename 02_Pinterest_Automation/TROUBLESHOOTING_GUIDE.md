# Enhanced Pinterest Prompt - Troubleshooting Guide

## Quick Links
- **Enhanced Automation:** `ENHANCED_Pinterest_Prompt_v2.blueprint.json`
- **Summary:** `ENHANCEMENT_SUMMARY.md`
- **Quick Reference:** `QUICK_REFERENCE_Enhanced_Prompt.md`
- **Comparison:** `BEFORE_AFTER_COMPARISON.md`

---

## Issue 1: Text Still Appearing in Images

### Symptoms
- AI generating phrases like "showing text overlay" in visual descriptions
- Pin concepts include "with title" or "headline visible"
- Text rendering despite multiple warnings

### Diagnosis Steps

1. **Check the actual output JSON:**
   ```bash
   # Look at the "visual" field in generated pins
   # Search for keywords: "text", "title", "headline", "words", "letters"
   ```

2. **Review temperature setting:**
   - Current: 0.9 (high creativity)
   - Issue: May be ignoring constraints for creativity

3. **Verify prompt is actually being used:**
   - Confirm Module 19 has the enhanced prompt
   - Check Make.com scenario is using enhanced blueprint

### Solutions

#### Solution A: Lower Temperature (Recommended First)
**Location:** Module 19 > mapper > temperature

**Change from:**
```json
"temperature": "0.9"
```

**Change to:**
```json
"temperature": "0.7"
```

**Impact:** Reduces creativity, increases literal rule-following

---

#### Solution B: Add Explicit Negative Prompt List
**Location:** Module 19 > mapper > messages > content

**Add this section after the main warning:**
```
FORBIDDEN WORDS IN "VISUAL" FIELD:
These words MUST NEVER appear in your visual descriptions:
- "text"
- "title"
- "headline"
- "words"
- "caption"
- "overlay"
- "showing [any text]"
- "with [any text]"
- "displaying"
- "reading"

If you include ANY of these words, the generation has FAILED.
```

---

#### Solution C: Add JSON Schema Validation
**Location:** After output format section

**Add:**
```
VALIDATION BEFORE SUBMISSION:
Run this check on your JSON:
1. Search "visual" field for the word "text"
2. If found → DELETE that pin and regenerate
3. Search for quotation marks around any words (indicates text)
4. If found → DELETE that pin and regenerate
```

---

#### Solution D: Add Another Warning at the Very End
**Location:** Just before "Now generate 3 Pinterest pin IMAGE concepts"

**Add:**
```
⚠️⚠️⚠️ FINAL FINAL WARNING ⚠️⚠️⚠️

Before you submit, read each "visual" field out loud.
If you hear ANYTHING about text, titles, words, or captions → REGENERATE.

The visual field should ONLY describe:
- A pet (breed)
- Doing something (using product)
- In a place (UK setting)
- With specific lighting and colors

NOTHING ELSE. Especially no text.
```

---

## Issue 2: Pets Still Halfway Out of Products

### Symptoms
- Dogs with only front half in hammocks
- Cats with back legs hanging out of beds
- Partial pet visibility
- Awkward, unrealistic positions

### Diagnosis Steps

1. **Identify which product types are problematic:**
   - Car products (hammocks, seats)?
   - Bedding products (beds, blankets)?
   - Carriers?
   - All of the above?

2. **Check if breed matters:**
   - Larger breeds (Labradors) more problematic?
   - Smaller breeds (French Bulldogs) better?

3. **Review actual visual descriptions:**
   - Do they say "fully in" but image still shows halfway?
   - Or do descriptions themselves lack "fully" language?

### Solutions

#### Solution A: Add Percentage Requirement
**Location:** Product usage logic section

**Add to EACH product type:**
```
- Pet's ENTIRE BODY must be visible (100% visibility from nose to tail)
- NO body parts hanging out, dragging, or partially obscured
- If you can't see the whole pet properly using the product, regenerate
```

---

#### Solution B: Add Specific Bad Examples for Your Problematic Products
**Location:** After critical rule #2

**Example for car hammocks:**
```
CAR HAMMOCK SPECIFIC RULES:

✅ CORRECT:
"Golden Retriever completely lying down in grey car hammock, full body visible from head to tail, relaxed position in back seat"

❌ WRONG - Halfway Out:
"Labrador with front paws in hammock, rear half on car seat"

❌ WRONG - Partially Obscured:
"Dog in hammock with only head visible"

❌ WRONG - Awkward Position:
"Beagle half standing, half sitting in hammock"

The entire dog must be COMFORTABLY LYING or SITTING in the hammock, full body visible.
```

---

#### Solution C: Add Measurement Requirement
**Location:** Visual field template

**Change to:**
```
"[ACTIVELY AND COMPLETELY USING PRODUCT - 100% of pet visible, properly positioned with entire body supported by product, realistic comfortable usage]"
```

---

#### Solution D: Add Reference to Magazine Standard
**Location:** Pre-submission checklist

**Add to Product Usage Check:**
```
□ Would this image pass editorial review for Country Living Pets magazine? → Must be YES
□ Is this how a pet ACTUALLY uses this product in real life? → Must be YES
□ Can you see the pet's entire body in a natural, comfortable position? → Must be YES
```

---

## Issue 3: Pins Still Look Inconsistent as a Set

### Symptoms
- Different lighting across 3 pins (bright vs dim vs overcast)
- Different color tones (warm vs cool vs neutral)
- Different photography styles (editorial vs stock vs casual)
- Don't look like they're from the same photoshoot

### Diagnosis Steps

1. **Compare the 3 generated pins:**
   - Do they mention different lighting? (morning vs evening vs midday)
   - Do they describe different color palettes?
   - Do they vary camera settings? (different f-stops, lenses)

2. **Check if AI is interpreting "different" too broadly:**
   - Does "different angle" become "different everything"?

### Solutions

#### Solution A: Add "SAME PHOTOSHOOT" Language Throughout
**Location:** Visual cohesion section

**Add emphasis:**
```
Think of this as ONE PHOTOSHOOT with three different camera angles.
Same photographer, same day, same lighting setup, same color grading.
Only the ANGLE and BREED change. Everything else IDENTICAL.
```

---

#### Solution B: Lower Temperature
**Location:** Module 19 > temperature

**Lower from 0.9 to 0.7** - Reduces variation tendency

---

#### Solution C: Add Explicit "Copy Previous Pin" Instruction
**Location:** The 3 personas section

**Modify to:**
```
PIN 2 - MID-RANGE LIFESTYLE SHOT:
- COPY ALL SETTINGS FROM PIN 1:
  - Same lighting direction and softness
  - Same warm earth tone palette (#937F71, #EEECE6, #E0CFBD)
  - Same time of day (if Pin 1 is morning, Pin 2 is morning)
  - Same photography style (85mm f/1.8)
- ONLY CHANGE:
  - Breed (different from Pin 1)
  - Camera angle (mid-range instead of close-up)
  - Room (different UK room, same aesthetic)

PIN 3 - WIDE ENVIRONMENTAL SHOT:
- COPY ALL SETTINGS FROM PINS 1 & 2:
  - Same lighting, same colors, same style
- ONLY CHANGE:
  - Breed (different from Pins 1 & 2)
  - Camera angle (wide instead of close or mid)
  - Room (different UK room, same aesthetic)
```

---

#### Solution D: Add Color Palette Enforcement to Each Visual
**Location:** Visual field template

**Change to:**
```
"A professional 9:16 vertical photorealistic editorial lifestyle photograph of [BREED] [ACTION] in [SETTING]. MANDATORY: Warm earth tone color palette using ONLY #937F71 taupe, #EEECE6 cream, #E0CFBD beige throughout entire image. Soft diffused natural daylight (overcast UK window light, consistent with other pins in this set)..."
```

---

#### Solution E: Add Reference Pin Concept
**Location:** Before the 3 personas section

**Add:**
```
COHESION REFERENCE EXAMPLE:

Imagine you're creating pins for "Best Orthopedic Dog Beds UK"

Pin 1: Close-up of cream Labrador's peaceful sleeping face in grey orthopedic bed, morning light streaming through window, warm taupe walls, 85mm f/1.8

Pin 2: Mid-shot of brown Cocker Spaniel fully curled in same style grey orthopedic bed beside fireplace, same morning light quality, same warm taupe interior, 85mm f/1.8

Pin 3: Wide shot of black French Bulldog resting in same style grey orthopedic bed in conservatory, same morning light flooding room, same warm taupe and cream palette, 85mm f/1.8

Notice: SAME lighting time/quality, SAME colors, SAME style, SAME bed type
Only different: breeds, angles, specific rooms
```

---

## Issue 4: Copy Space Still Inconsistent

### Symptoms
- Sometimes upper third is clear, sometimes it's busy
- Pet faces or main subjects appearing in text zone
- Shelves, artwork, or clutter in upper third

### Diagnosis Steps

1. **Review generated "visual" descriptions:**
   - Do they specifically mention upper third?
   - Do they describe what's in the background?

2. **Check if compositional language is vague:**
   - "Copy space in upper third" vs "Upper third is soft gradient wall"

### Solutions

#### Solution A: Make Copy Space Percentage-Based
**Location:** Copy space requirements section

**Change to:**
```
Upper 30% of Every Pin (Measured from Top):
- This zone MUST be described as one of these:
  1. "Soft gradient warm taupe wall (upper 30% clear)"
  2. "Out-of-focus cream painted wall (upper 30% empty)"
  3. "Blurred window light with no details (upper 30% for text)"
  4. "Soft bokeh background, no distinct elements (upper 30% available)"

⛔ FORBIDDEN in upper 30%:
- Pet's face or head
- Shelves, frames, artwork
- Windows with visible details
- Patterns or textures
- Any focal point
```

---

#### Solution B: Add Technical Composition Rule
**Location:** Visual field template

**Add:**
```
"Composition: Subject (pet + product) positioned in middle to lower 70% of frame, upper 30% contains ONLY out-of-focus wall in warm taupe gradient, suitable for text overlay"
```

---

#### Solution C: Add Visual Examples of Good Copy Space
**Location:** Copy space requirements section

**Add:**
```
COPY SPACE EXAMPLES (Choose One):

Example 1: "Upper third shows out-of-focus warm taupe wall (Farrow & Ball 'Mouse's Back'), soft gradient from light to slightly darker taupe, no texture or detail visible, perfect empty space for overlay text"

Example 2: "Upper third is blurred cream window light, no window frame visible, just soft diffused glow, completely empty of focal elements"

Example 3: "Upper third shows soft bokeh background of warm beige tones, no distinct shapes or objects, gradient-like quality, ready for text placement"
```

---

## Issue 5: UK Authenticity Lacking

### Symptoms
- Generic "American-looking" homes
- Non-UK car models mentioned
- American spelling creeping in
- Generic hashtags instead of UK-specific

### Diagnosis Steps

1. **Check titles and descriptions:**
   - "Gray" vs "Grey"?
   - "Favorite" vs "Favourite"?

2. **Review settings described:**
   - "Generic modern home" vs "Victorian terrace"?

3. **Check hashtags:**
   - Generic #Dogs or UK #UKDogs?

### Solutions

#### Solution A: Add UK Spell-Check to Checklist
**Location:** Pre-submission checklist

**Modify Pinterest UK Check to:**
```
5. PINTEREST UK CHECK:
   □ Title uses British spelling (grey NOT gray, favourite NOT favorite)?
   □ Description uses British spelling (colour, cosy, programme)?
   □ Hashtags are UK-specific (#UKDogs #DogMumUK #PetLifeUK #BritishPets)?
   □ No American spellings detected (color, favorite, gray, program)?
   □ Title under 45 characters?

AUTOMATIC FAIL if ANY American spelling found. Regenerate with British spelling.
```

---

#### Solution B: Add Mandatory UK Elements List
**Location:** UK authenticity section

**Add:**
```
MANDATORY UK ELEMENTS CHECKLIST:

Every pin MUST include at least 2 of these UK-specific details:

ARCHITECTURE:
- Victorian terrace features (bay windows, high ceilings, picture rails)
- 1930s semi details (pebbledash, stained glass, tiled hallway)
- Cottage elements (exposed beams, inglenook fireplace, low ceilings)

DECOR:
- Farrow & Ball paint colors (specific names like "Elephant's Breath", "Mouse's Back")
- British brands visible (Emma Bridgewater ceramics, William Morris patterns)
- UK-style radiators (not baseboard heating)

OUTDOOR:
- British gardens (privet hedges, cottage garden plants, sash windows visible)
- UK street furniture (if applicable)
- British weather light (often diffused, overcast quality)

VEHICLES (if applicable):
- Nissan Qashqai interior
- VW Golf boot
- Range Rover Evoque back seat
- Ford Fiesta interior
```

---

#### Solution C: Add UK Brand References
**Location:** Setting aesthetic section

**Add:**
```
UK HOME DECOR REFERENCES:
- Paint: Farrow & Ball ("Elephant's Breath", "Mouse's Back", "Strong White")
- Textiles: Laura Ashley florals, William Morris prints, Sanderson fabrics
- Ceramics: Emma Bridgewater, Portmeirion, Denby
- Flooring: Fired Earth tiles, Amtico, Victorian encaustic tiles
- Furniture: IKEA UK (British homes context), Habitat, John Lewis

Mentioning these brands adds authentic British home context.
```

---

## Issue 6: JSON Output Errors

### Symptoms
- Invalid JSON returned
- Missing fields (visual, title, desc, alt)
- Wrong number of pins (not exactly 3)
- Special characters breaking JSON

### Diagnosis Steps

1. **Check Make.com error logs:**
   - JSON parsing errors?
   - Missing required fields?

2. **Review raw output:**
   - Are quotation marks escaped properly?
   - Are line breaks causing issues?

### Solutions

#### Solution A: Add JSON Validation Instructions
**Location:** Output format section

**Add:**
```
JSON VALIDATION REQUIREMENTS:

Before submitting, verify:
1. Exactly 3 objects in array (not 2, not 4, exactly 3)
2. Every object has all 4 fields: visual, title, desc, alt
3. All quotation marks inside strings are escaped: \"
4. No unescaped line breaks inside strings
5. No trailing commas
6. Valid JSON structure (use mental JSON validator)

TEST: If you pasted this into a JSON validator, would it pass? If NO, fix it.
```

---

#### Solution B: Add Character Escape List
**Location:** Output format section

**Add:**
```
CHARACTER ESCAPING RULES:

In JSON strings, these MUST be escaped:
- " → \"
- \ → \\
- New line → \\n (but avoid new lines in strings)

SAFE CHARACTERS (no escaping needed):
- Letters, numbers
- Spaces
- , . ! ? - ( )
- £ # @ (UK-relevant symbols)

If unsure, use simple language and avoid special characters.
```

---

#### Solution C: Simplify Output Format
**Location:** Output format section

**Modify template to be more explicit:**
```
[
  {
    "visual": "SINGLE LINE description here with no line breaks or special characters",
    "title": "Under 45 characters using only letters numbers spaces and basic punctuation",
    "desc": "Description with hashtags using only safe characters",
    "alt": "Simple alt text description"
  },
  {
    "visual": "Second pin description",
    "title": "Second title",
    "desc": "Second description",
    "alt": "Second alt"
  },
  {
    "visual": "Third pin description",
    "title": "Third title",
    "desc": "Third description",
    "alt": "Third alt"
  }
]

CRITICAL: Return ONLY this JSON. No "Here's your JSON:" prefix. No explanation after.
Just the JSON array starting with [ and ending with ]
```

---

## Issue 7: Product Type Confusion

### Symptoms
- Generating cat pins for dog products
- Showing bowls in cars or car seats in gardens
- Mixing up product categories

### Diagnosis Steps

1. **Check blog titles being tested:**
   - Are they clear about product type?
   - Do they specify dog vs cat?

2. **Review product usage logic section:**
   - Is the logic clear enough?

### Solutions

#### Solution A: Add Species Detection Requirement
**Location:** Critical analysis section

**Modify to:**
```
CRITICAL ANALYSIS REQUIRED:
1. Read the blog title carefully
2. IDENTIFY THE SPECIES:
   - Does it say "dog", "dogs", "canine", "puppy"? → Generate DOG pins only
   - Does it say "cat", "cats", "feline", "kitten"? → Generate CAT pins only
   - Does it say "pet" generically? → Choose either dog OR cat (not mixed)
3. Identify what PRODUCT or TOPIC it's about
4. Understand HOW that product is used in real life
5. Generate pins showing REALISTIC, COMPLETE usage by UK pet owners

SPECIES RULE: All 3 pins MUST be same species. No mixing dogs and cats in one set.
```

---

#### Solution B: Add Product-Setting Matrix
**Location:** After product usage logic

**Add:**
```
PRODUCT-SETTING COMPATIBILITY MATRIX:

ALWAYS COMPATIBLE:
✅ Food bowls → Kitchen, utility room
✅ Car hammocks → Inside vehicles (back seat, boot)
✅ Dog beds → Living room, bedroom, conservatory
✅ Harnesses → Outdoor walking scenes, parks
✅ Toys → Any indoor room

NEVER COMPATIBLE:
❌ Food bowls in cars (wrong location)
❌ Car hammocks in kitchens (wrong location)
❌ Outdoor harnesses in bedrooms (wrong context)
❌ Car seats in gardens (wrong location)

If you're not 100% sure a product belongs in a setting, it doesn't. Choose the obvious match.
```

---

## General Troubleshooting Steps

### Step 1: Check Temperature Setting
**Most common fix:** Lower from 0.9 to 0.7

### Step 2: Verify Enhanced Prompt Is Active
```bash
# Extract Module 19 content from blueprint
jq '.flow[] | select(.id == 19) | .mapper.messages[0].content' ENHANCED_Pinterest_Prompt_v2.blueprint.json | head -c 200

# Should start with: "⚠️ CRITICAL INSTRUCTION ⚠️"
```

### Step 3: Test With Simple Blog Titles First
Start with clear, unambiguous titles:
- "Best Dog Beds for UK Homes"
- "Top Car Hammocks for Dogs UK"
- "Cosy Cat Beds Britain"

### Step 4: Review 10 Generations and Track Issues
Create tracking spreadsheet:
| Blog Title | Text Present? | Realistic Usage? | Cohesive Set? | Copy Space? | UK Authentic? | Useable? |
|------------|---------------|------------------|---------------|-------------|---------------|----------|
| Title 1    | Yes/No        | Yes/No           | Yes/No        | Yes/No      | Yes/No        | Yes/No   |

### Step 5: Identify Patterns
- Same issue every time? → Add more warnings
- Specific product types problematic? → Add product-specific examples
- Random failures? → Lower temperature

---

## Advanced Fixes

### If Nothing Else Works: Nuclear Option

**Add this at the VERY START of the prompt (before everything else):**

```
═══════════════════════════════════════════════════════════════
🚨🚨🚨 READ THIS FIRST OR FAIL 🚨🚨🚨
═══════════════════════════════════════════════════════════════

You will FAIL this task if you:
1. Put ANY text in the images (instant fail)
2. Show pets halfway out of products (instant fail)
3. Generate 3 pins that don't look cohesive (instant fail)
4. Use American spelling instead of British (instant fail)
5. Return invalid JSON (instant fail)

This is a PASS/FAIL task.
You either follow ALL rules perfectly, or you fail completely.
There is no partial credit.

Read every section below carefully. Your success depends on it.

═══════════════════════════════════════════════════════════════
```

---

## Monitoring & Iteration

### Create a Testing Log

Test batch of 20 blog titles, track:
- Success rate per issue type
- Common failure patterns
- Which products are problematic
- Temperature correlation

### Iterative Improvement

1. **Week 1:** Run 20 tests, identify top issue
2. **Week 2:** Add specific fix for top issue, test 20 more
3. **Week 3:** Add fix for second issue, test 20 more
4. **Week 4:** Fine-tune temperature based on results

### Success Criteria

Consider enhancement successful when:
- 80%+ usability rate achieved
- Text appears in <10% of pins
- 90%+ realistic product usage
- 90%+ cohesive sets
- 95%+ proper copy space
- 95%+ British spelling

---

## Support Files Reference

1. **Main Documentation:** `ENHANCEMENT_SUMMARY.md`
2. **Quick Reference:** `QUICK_REFERENCE_Enhanced_Prompt.md`
3. **Before/After:** `BEFORE_AFTER_COMPARISON.md`
4. **This Guide:** `TROUBLESHOOTING_GUIDE.md`

---

## Quick Fix Checklist

Problem: Text appearing → Lower temperature to 0.7, add more warnings
Problem: Halfway out pets → Add percentage requirements, product-specific examples
Problem: Inconsistent style → Add "SAME PHOTOSHOOT" language, lower temperature
Problem: Poor copy space → Make percentage-based (30%), add specific examples
Problem: Not UK enough → Add mandatory UK elements checklist
Problem: JSON errors → Add validation instructions, simplify format
Problem: Wrong products → Add species detection, product-setting matrix

---

**Last Updated:** December 25, 2024
