# Enhanced Pinterest Prompt - Quick Reference

## File Location
`/Volumes/Home Ext/Home Ext/Desktop/Claude/02_Pinterest_Automation/ENHANCED_Pinterest_Prompt_v2.blueprint.json`

---

## The 6 Major Fixes

### 1. NO TEXT IN IMAGES (🚨 #1 Priority)
**Problem:** Text appearing in 5/6 pins despite negative prompts

**Fix Applied:**
- Massive warning section at top with visual separators
- Multiple explicit "NO TEXT" instructions
- Examples of CORRECT vs WRONG
- Pre-submission checklist requires verification
- Emphasized "copy space = EMPTY SPACE for Canva later"

**Key Phrase Added:**
> "You are creating the BASE PHOTOGRAPH only. Text will be added in post-production."

---

### 2. REALISTIC PRODUCT USAGE (🚨 #2 Priority)
**Problem:** Pets halfway out of hammocks/beds (unusable images)

**Fix Applied:**
- Dedicated "CRITICAL RULE #2" section
- Explicit examples for every product type
- "Pet must be COMPLETELY and COMFORTABLY using product"
- Magazine-worthy standard set

**Key Examples Added:**
- ✅ "Cocker Spaniel fully settled inside grey car hammock"
- ❌ "Dog's head and front paws in hammock, rear half hanging out"

---

### 3. VISUAL COHESION ACROSS 3 PINS
**Problem:** Pins don't look like a cohesive set

**Fix Applied:**
- Mandatory consistency rules for all 3 pins
- Identical color palette: #937F71, #EEECE6, #E0CFBD
- Identical lighting: soft diffused UK window light
- Identical photography style: 85mm f/1.8 editorial
- Same decor aesthetic across all 3

**Framework Added:**
> "These 3 pins will be posted together as a SET - they MUST look cohesive and branded."

---

### 4. COPY SPACE FOR CANVA OVERLAYS
**Problem:** Inconsistent clear space for text overlays

**Fix Applied:**
- Dedicated "COPY SPACE REQUIREMENTS" section
- Specified exactly what NOT to put in upper third
- "Copy space should be BORING and EMPTY"
- Built into visual field template

**Ideal Copy Zones:**
- Soft gradient wall
- Out-of-focus blank wall
- Blurred window with diffused light

---

### 5. THREE DISTINCT ANGLES/PERSONAS
**Problem:** Need variety for repurposing

**Fix Applied:**
- Clear 3-persona framework:
  - PIN 1: Close-up detail shot
  - PIN 2: Mid-range lifestyle shot
  - PIN 3: Wide environmental shot
- Different breeds per pin
- Different UK settings per pin
- Maintained cohesive aesthetic

---

### 6. UK AUTHENTICITY & OPTIMIZATION
**Problem:** Need authentic British context

**Fix Applied:**
- Specific UK home types (Victorian terrace, cottage, 1930s semi)
- British car models (Nissan Qashqai, VW Golf, Range Rover)
- UK lighting conditions (overcast, soft diffused)
- British spelling enforced
- UK hashtags: #UKDogs #DogMumUK #PetLifeUK #BritishPets
- Titles under 45 characters

---

## The Pre-Submission Checklist

Every pin generation must pass these checks:

### 1. TEXT CHECK
- [ ] No text/words/letters in image description?
- [ ] Upper third described as clear copy space?

### 2. PRODUCT USAGE CHECK
- [ ] Pet FULLY visible (not halfway out)?
- [ ] Pet PROPERLY using product as intended?
- [ ] Would UK pet owner think "that's realistic"?

### 3. VISUAL COHESION CHECK
- [ ] All 3 pins have SAME lighting quality?
- [ ] All 3 pins use SAME warm earth tone palette?
- [ ] All 3 pins have SAME photography style?
- [ ] Would these 3 pins look cohesive posted together?

### 4. SETTING CHECK
- [ ] Setting appropriate for product type?
- [ ] Setting authentically British?
- [ ] Benefit of product VISIBLE in scene?

### 5. PINTEREST UK CHECK
- [ ] Title under 45 characters?
- [ ] Description includes 3-4 UK hashtags?
- [ ] British spelling used throughout?

**Rule:** If ANY answer is "NO," regenerate that pin.

---

## Expected Results

### Before Enhancement
- Usability: 1/6 pins (17%)
- Realism: Inconsistent, frequent halfway-out positions
- Cohesion: Pins look unrelated
- Copy Space: Variable

### After Enhancement (Projected)
- Usability: 5/6+ pins (80%+)
- Realism: 90%+ realistic product usage
- Cohesion: 95%+ sets feel branded
- Copy Space: 95%+ pins have clear upper third

---

## Visual Field Template (New Standard)

```json
{
  "visual": "A professional 9:16 vertical photorealistic editorial lifestyle photograph of [SPECIFIC UK BREED] [ACTIVELY AND COMPLETELY USING PRODUCT - fully visible, properly positioned, realistic usage] in [APPROPRIATE UK SETTING - specific British home type]. Soft diffused natural daylight (overcast UK window light), upper third has clear copy space (soft gradient warm taupe wall, slightly blurred), 85mm f/1.8 shallow depth of field, warm earth tone palette (#937F71 taupe, #EEECE6 cream, #E0CFBD beige), editorial aesthetic, authentic British home, cinematic quality. Absolutely no text or typography in image."
}
```

---

## Color Palette (Mandatory)

**Primary Colors (all 3 pins):**
- #937F71 - Warm taupe
- #EEECE6 - Soft cream
- #E0CFBD - Warm beige

**Accent Colors (optional, use sparingly):**
- Soft sage green
- Dusty rose
- Warm grey

**Avoid:**
- Bright primary colors
- Neon
- Stark white
- Harsh blacks

---

## UK Breeds (Rotate Across 3 Pins)

**Dogs:**
- Labrador Retriever
- Cocker Spaniel
- French Bulldog
- Beagle
- Border Terrier
- Springer Spaniel
- Golden Retriever

**Cats:**
- British Shorthair
- Tabby
- Ginger cat
- Tortoiseshell

---

## UK Settings (Vary Across 3 Pins, Same Aesthetic)

**Home Types:**
- Victorian terraced house
- 1930s semi-detached
- Modern new build flat
- Cottage
- Edwardian home

**Room Types:**
- Living room corner by window
- Bedroom nook
- Conservatory with plants
- Kitchen corner
- Utility room
- Home office
- Garden room
- Hallway

---

## Product-Specific Guidance

### Food Products (bowls, feeders, mats)
- ON THE FLOOR in UK kitchens/utility rooms
- Pet ACTIVELY USING (eating, licking, drinking)
- Pet fully visible, properly positioned over bowl

### Car Products (hammocks, harnesses, carriers)
- INSIDE vehicles (back seat or boot)
- Dog/cat FULLY IN/ON product, completely visible
- British car models visible
- Pet looks comfortable and secure (NOT half-in/half-out)

### Walking Products (harnesses, leads, coats)
- Being WORN by pet during walks
- UK outdoor settings (parks, pavements, countryside)
- Pet doing activity naturally
- Full pet visible, product properly fitted

### Anxiety/Calm Products (beds, mats, toys)
- Quiet UK home settings (living room, bedroom, conservatory)
- Pet genuinely calm/relaxed while FULLY using them
- Pet completely in bed/on mat
- Cosy British home atmosphere

### Bedding/Sleep Products
- Pet FULLY in bed/on blanket
- Complete, realistic sleeping/resting position
- NO half-in/half-out positions
- Pet looks genuinely comfortable and settled

---

## Import Instructions

1. Go to Make.com dashboard
2. Click "Create a new scenario"
3. Click three dots menu > "Import Blueprint"
4. Upload: `ENHANCED_Pinterest_Prompt_v2.blueprint.json`
5. Reconnect Google Sheets connection
6. Reconnect Google Vertex AI connection
7. Save and activate

---

## Fine-Tuning Options

### If text still appears:
- Lower temperature from 0.9 to 0.7
- Add another warning section at the very end
- Add explicit negative prompt list

### If realism issues persist:
- Add more product-specific examples
- Lower temperature to 0.7
- Add "entire body visible" requirement

### If cohesion issues persist:
- Reduce temperature for more consistent adherence
- Add reference image links for desired aesthetic
- Add more bad examples showing what NOT to do

### If copy space inconsistent:
- Make upper third requirement percentage-based ("30% must be clear")
- Add technical requirements (e.g., "solid color gradient only")
- Provide more specific examples

---

## Key Metrics to Track

1. **Usability Rate:** % of pins useable without fixes
2. **Text Appearance:** % of pins with unwanted text
3. **Realistic Usage:** % of pins showing proper product usage
4. **Visual Cohesion:** % of 3-pin sets that look branded
5. **Copy Space Quality:** % of pins with clear upper third

**Target:** 80%+ across all metrics

---

## Why This Works

The enhanced prompt uses proven AI prompt engineering techniques:

1. **Repetition with Variation** - Same rules stated multiple ways
2. **Concrete Examples** - Shows exactly what to do/not do
3. **Visual Hierarchy** - Emojis and separators make sections unmissable
4. **Pre-Submission Forcing** - Checklist creates self-correction loop
5. **Brand Campaign Framing** - Elevates quality standard
6. **Explicit Templates** - Provides exact format to follow

**Result:** AI has clear guardrails and high standards to meet.

---

## Support

**Full Documentation:** See `ENHANCEMENT_SUMMARY.md`

**Original Automation:** `(Working - Blog to Pinterest Pins) Blog Pinterst Pin Creation Automation V 24.12.25.blueprint.json`

**Enhanced Automation:** `ENHANCED_Pinterest_Prompt_v2.blueprint.json`

---

**Last Updated:** December 25, 2024
