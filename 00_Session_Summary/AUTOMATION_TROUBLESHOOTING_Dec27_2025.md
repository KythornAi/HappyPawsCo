# Automation Troubleshooting Guide
**Date:** December 27, 2024
**Issues Fixed:** Blog & Pinterest image generation failures

---

## Problem Summary

**Reported Issue:** Both blog and Pinterest automations stopped generating images after user cleared old topics and added new ones.

**Symptoms:**
- Blog text generated successfully ✅
- Status changed from SCHEDULED → AWAITING_REVIEW ✅
- Drive links created ✅
- BUT: Image files were 0 bytes, named "Untitled", empty when clicked ❌

---

## Root Causes Identified

### Issue 1: Blog Automation - Module 11 Data Field Not Mapped

**Problem:** Module 11 (Google Drive - Upload a File) had an empty Data field

**What was happening:**
- Module 18 (Imagen) WAS generating images (422KB JPEG buffers) ✅
- Module 11 was creating file metadata in Drive ✅
- BUT Module 11 wasn't receiving the image data from Module 18 ❌
- Result: 0-byte "Untitled" files with mime type `application/octet-stream`

**Fix Applied:**
1. Opened Module 11 (Google Drive - Upload a File)
2. Changed "File" section from "Google Drive - Download a File" to "Map" mode
3. This revealed the **Data** field
4. Mapped Data field to: `{{18.Generated Images[].Image Data}}`
5. Also set File Name to: `{{20.Blog_Title (B)}}.jpg`
6. Folder ID: Left as Drive folder ID string

**Key Learning:** The Data field must have the image buffer mapped, not just the file name/folder

---

### Issue 2: Pinterest Automation - Wrong Folder Mapping

**Problem:** Images uploading to parent folder instead of blog-specific subfolders

**What was happening:**
- Module 21 (Imagen) generating images correctly (1.4-1.5MB PNGs) ✅
- Module 25 (Create Folder) creating blog-specific subfolders ✅
- Module 11 (Upload File) uploading images ✅
- BUT images were in parent folder, subfolders were empty ❌

**Fix Applied:**
1. Changed Module 11 Folder ID from static parent ID to `{{25.Folder ID}}`
2. This uploads images INTO the subfolder created by Module 25
3. File Name already correct: `{{20.Blog_Title (A)}}_Pin_{{24.Bundle order position}}`

**Key Learning:** Module 11 needs dynamic folder reference from Module 25, not static parent folder

---

### Issue 3: Pinterest Images - Text Appearing in Generated Images

**Problem:** Hex color codes from brand palette appearing as text overlay in images

**What was happening:**
- Negative prompt configured in Module 21 ✅
- Temperature set to 0.7 in Module 19 ✅
- BUT text still appearing: "CLEAN WOPT #EEECE6 #ISOFFBD #E0CFBD" ❌

**Why it happened:**
- Module 19 (Gemini) was creating prompts with brand colors like this:
  `warm earth tone palette (#937F71 taupe, #EEECE6 cream, #E0CFBD beige)`
- Imagen API was interpreting the hex codes as something to DISPLAY rather than just color guidance
- Even with comprehensive negative prompt, the hex codes triggered text rendering

**Fix Applied:**

**Change 1 - Module 19 Prompt:**
- **OLD:** `warm earth tone palette (#937F71 taupe, #EEECE6 cream, #E0CFBD beige)`
- **NEW:** `warm earth tone palette with soft taupe, warm cream, and gentle beige tones`

**Change 2 - Module 21 Negative Prompt:**
- **OLD:** `"text, words, letters, numbers, font, typography, watermark, logo..."`
- **NEW:** Added: `", hex codes, color codes, hashtags, #"` to the end

**Result:** No more text appearing in images ✅

**Key Learning:** Remove ALL symbols/codes from prompts that could be rendered as text, even color codes

---

## Complete Configuration Reference

### Blog Automation - Module 11 (Google Drive Upload)

**Correct Settings:**
```
Drive: [Your Google Drive connection]

Folder ID: 1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4
(or your specific Drive folder ID)

File Name: {{20.Blog_Title (B)}}.jpg

File Section: MAP mode (not "Download a File")

Data: {{18.Generated Images[].Image Data}}

Convert a File: No
```

**Critical Fields:**
- **Data field MUST be mapped** to Module 18 image output
- **File section MUST be on "Map"** not "Download a File"
- File Name should include `.jpg` extension

---

### Pinterest Automation - Module 11 (Google Drive Upload)

**Correct Settings:**
```
Drive: [Your Google Drive connection]

Folder ID: {{25.Folder ID}}
(dynamic reference to created subfolder, NOT static parent ID)

File Name: {{20.Blog_Title (A)}}_Pin_{{24.Bundle order position}}

File Section: MAP mode

Data: {{21.Generated Images[].Image Data}}

Convert a File: No
```

**Critical Fields:**
- **Folder ID MUST reference Module 25** to upload into subfolders
- **Data field MUST be mapped** to Module 21 image output
- File Name includes bundle position for multiple pins per blog

---

### Pinterest Automation - Module 19 (Gemini Prompt Creator)

**Correct Prompt Format:**
```
Visual description should include:
- "warm earth tone palette with soft taupe, warm cream, and gentle beige tones"

NOT:
- "warm earth tone palette (#937F71 taupe, #EEECE6 cream, #E0CFBD beige)"

Remove ALL hex codes, hashtags, or symbols that could render as text
```

---

### Pinterest Automation - Module 21 (Imagen)

**Correct Negative Prompt:**
```
"negativePrompt": "text, words, letters, numbers, font, typography, watermark, logo, headline, title, caption, label, sign, writing, script, coherent text, gibberish text, overlay text, rendered text, any readable characters, alphabet letters, hex codes, color codes, hashtags, #"
```

**Must include:** `hex codes, color codes, hashtags, #` to prevent color codes rendering as text

---

## Diagnostic Checklist

When images aren't generating, check in this order:

### Step 1: Verify Image Generation
- Check Module 18 (Blog) or Module 21 (Pinterest) output
- Look for "Generated Images[]" → "Image Data" with buffer size
- Should show size like 422KB or 1.5MB
- If this is empty → problem is with Imagen module, not upload

### Step 2: Check Module 11 Input
- Look at Module 11 "Input" section
- Should show "DataBuffer, codepage: binary" with size
- If shows "Bundle 1: empty" → Data field not mapped correctly

### Step 3: Check Module 11 Output
- Look at Module 11 "Output" section
- Size should match input (e.g., 1546209 bytes)
- Name should be your blog title, not "Untitled"
- Mime Type should be image/jpeg or image/png, not application/octet-stream

### Step 4: Check Drive
- Open the Drive folder
- For Pinterest: check INSIDE the blog-specific subfolders
- File size should match Module 11 output
- Should be viewable image, not "No preview available"

---

## Quick Fixes Reference

| Problem | Module | Fix |
|---------|--------|-----|
| Empty images (0 bytes) | Module 11 | Map Data field to `{{18.Generated Images[].Image Data}}` |
| Images in wrong folder | Module 11 | Change Folder ID to `{{25.Folder ID}}` |
| Text appearing in images | Module 19 | Remove hex codes from color descriptions |
| Text appearing in images | Module 21 | Add `hex codes, hashtags` to negative prompt |
| File named "Untitled" | Module 11 | Set File Name to `{{20.Blog_Title}}.jpg` |
| "No preview available" | Module 11 | Check Data field is mapped, not empty |

---

## Prevention

**Before running automation:**
1. Check Module 11 Data field has mapping pill visible
2. Verify File Name field shows blog title mapping
3. For Pinterest: verify Folder ID references Module 25
4. Check Imagen negative prompt includes hex code blockers

**After running automation (test with 1 row):**
1. Check Drive file is not 0 bytes
2. Click file to verify image displays
3. For Pinterest: verify image is INSIDE subfolder
4. Check file name matches blog title

---

## Session Notes

**Fixed:** December 27, 2024
**Automations Affected:**
- Blog Generator - NEW Workflow Sheet v1
- Pinterest Pin Generator - NEW Workflow Sheet v1

**Time to Diagnose:** ~45 minutes
**Time to Fix:** ~10 minutes once issue identified

**Key Insight:** Module 11 requires explicit Data field mapping. The module can create file metadata (name, folder, permissions) without actually having file content, resulting in empty files that look correct but have no data.

---

**Created:** December 27, 2024
**For:** HappyPawsCo Blog & Pinterest Automations
**Status:** Issues resolved, both automations working
