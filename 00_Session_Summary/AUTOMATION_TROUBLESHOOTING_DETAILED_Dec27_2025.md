# Complete Automation Troubleshooting Guide
**Date:** December 27, 2024
**Issue:** Blog & Pinterest automations creating empty image files
**Status:** ✅ RESOLVED
**Time to Fix:** 10 minutes once you know what to look for

---

## When to Use This Guide

**Use this guide if you see these symptoms:**

1. **Blog automation runs successfully** BUT:
   - ✅ Blog text appears in Column F
   - ✅ Status changes from SCHEDULED → AWAITING_REVIEW
   - ✅ "View Image" link appears in Column G
   - ❌ When you click the link, you see "No preview available" or blank/white box
   - ❌ File in Drive shows 0 bytes or is named "Untitled"

2. **Pinterest automation runs successfully** BUT:
   - ✅ Subfolders created with blog titles
   - ✅ Pinterest_Pins sheet updated with Drive links
   - ❌ Subfolders are empty (no images inside)
   - OR
   - ❌ Images appear in parent folder instead of subfolders
   - OR
   - ❌ Text/hex codes appearing on generated images

---

## The Problems & What Was Happening

### Problem 1: Blog Images = Empty Files (0 bytes)

**What you see:**
- Drive link works, but shows "No preview available"
- File is named "Untitled"
- File size is 0 bytes
- Mime type shows as "application/octet-stream" instead of "image/jpeg"

**What's actually happening:**
- Module 18 (Google Vertex AI - Imagen) IS generating the image ✅
- The image is a 422KB JPEG buffer sitting in Module 18's output ✅
- Module 11 (Google Drive - Upload a File) IS creating a file in Drive ✅
- BUT Module 11 is creating an empty container with metadata only ❌
- The image data from Module 18 never makes it to Module 11 ❌

**Why this happens:**
- Module 11 has a field called "Data" that needs to contain the actual file contents
- This field was empty (not mapped to Module 18's output)
- Without data, Module 11 creates file structure but no content
- It's like making an empty box with a label but nothing inside

---

### Problem 2: Pinterest Images in Wrong Location

**What you see:**
- Blog-specific subfolders exist (e.g., "Winter Car Safety" folder)
- But when you open them, they're empty
- Images are sitting loose in the parent "HappyPawsCo_Pinterest" folder instead

**What's actually happening:**
- Module 25 creates blog-specific subfolder ✅
- Module 21 generates the Pinterest images ✅
- Module 11 uploads the images to Drive ✅
- BUT Module 11 is uploading to a static parent folder ID ❌
- The subfolder and images exist in same parent, but not connected ❌

**Why this happens:**
- Module 11's "Folder ID" was set to a static folder ID string
- Should reference Module 25's created folder ID dynamically
- Images go where Module 11 tells them, not where Module 25 creates folders

---

### Problem 3: Text Appearing in Pinterest Images

**What you see:**
- Beautiful dog image generated ✅
- BUT text overlay appears like: "CLEAN WOPT #EEECE6 #ISOFFBD #E0CFBD" ❌

**What's actually happening:**
- Module 19 creates the prompt that describes the image
- Prompt includes brand colors like: "#937F71 taupe, #EEECE6 cream"
- Imagen AI sees these hex codes and thinks "oh, I should render text with those codes"
- Even though negative prompt says "no text", the hex codes trigger text rendering

**Why this happens:**
- AI doesn't understand "#EEECE6" means "use this color"
- It sees "#" and alphanumeric characters and renders them as visible text
- Hex codes should never appear in visual prompts sent to image generators

---

## Step-by-Step Fixes

### FIX 1: Blog Automation - Map Image Data to Module 11

**Problem:** Empty image files
**Fix Location:** Module 11 (Google Drive - Upload a File)
**Time:** 3 minutes

#### Step-by-Step Instructions:

1. **Open Make.com** in your browser
2. **Navigate to your Blog automation:**
   - Go to Scenarios
   - Find: "Blog Generator - NEW Workflow Sheet v1"
   - Click on it to open

3. **Locate Module 11:**
   - Scroll through the automation flow
   - Find the module labeled "Google Drive - Upload a File"
   - It should be orange/yellow Drive icon
   - Module number shows as "11" in the flow

4. **Click on Module 11** to open its settings panel

5. **Check the "File" section:**
   - You'll see two radio button options:
     - ○ Google Drive - Download a File
     - ○ Map
   - If "Google Drive - Download a File" is selected, this is the problem!

6. **Click the "Map" radio button**
   - This switches the module to upload mode
   - New fields will appear below

7. **Locate the "Data" field:**
   - Scroll down in the Module 11 settings panel
   - Look for a field labeled "Data" with a red asterisk (*)
   - The red asterisk means it's a required field
   - This field should currently be empty (that's the problem!)

8. **Map the image data:**
   - Click inside the empty "Data" field
   - A right-side panel should appear showing available data from previous modules
   - Scroll up in this right panel to find "Module 18: Google Vertex AI (Gemini) - Generate an Image"
   - Click to expand Module 18 if it's collapsed
   - Look for "Generated Images[]" and expand it
   - You'll see several fields including:
     - Image Data
     - Mime Type
     - Content Type
   - Click on **"Image Data"** specifically (not Mime Type, not Content Type)

9. **Verify the mapping:**
   - The Data field should now show a blue/purple pill that says:
     ```
     {{18. Generated Images[].Image Data}}
     ```
   - The "18." refers to Module 18
   - The "[]" means it's an array
   - "Image Data" is the actual image buffer

10. **Set the File Name (if not already set):**
    - Scroll up to find the "File Name" field
    - Should contain: `{{20.Blog_Title (B)}}.jpg`
    - If empty, click inside and map:
      - Find Module 20 (Google Sheets - Search Rows)
      - Select "Blog_Title (B)"
      - Manually add `.jpg` to the end
    - Final result: `{{20.Blog_Title (B)}}.jpg`

11. **Check Folder ID:**
    - Should show your Drive folder ID
    - Should be a long string like: `1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4`
    - This can stay as a static ID (doesn't need to be dynamic for blog)

12. **Save the module:**
    - Click "OK" button at bottom of Module 11 panel
    - Then click "Save" button at bottom of entire automation

13. **Test with ONE row:**
    - Go to your Blog_Calendar sheet
    - Find ONE row with content
    - Set Column E (Status) to: `SCHEDULED`
    - Wait for automation to run OR trigger manually
    - Check the results

14. **Expected results after fix:**
    - ✅ Module 18 output shows: Image Data buffer ~422KB
    - ✅ Module 11 input shows: DataBuffer, codepage: binary
    - ✅ Module 11 output shows: Size: ~400000+ bytes (NOT 0)
    - ✅ Module 11 output shows: Name: [Your Blog Title].jpg (NOT "Untitled")
    - ✅ Module 11 output shows: Mime Type: image/jpeg (NOT application/octet-stream)
    - ✅ Drive file is clickable and shows dog image
    - ✅ File size in Drive shows ~400KB

---

### FIX 2: Pinterest Automation - Dynamic Folder Reference

**Problem:** Images uploading to parent folder instead of subfolders
**Fix Location:** Module 11 (Google Drive - Upload a File)
**Time:** 2 minutes

#### Step-by-Step Instructions:

1. **Open Make.com** and navigate to Pinterest automation:
   - Scenarios → "Pinterest Pin Generator - NEW Workflow Sheet v1"

2. **Locate Module 11** (Google Drive - Upload a File)
   - Orange/yellow Drive icon in the flow

3. **Click on Module 11** to open settings

4. **Find the "Folder ID" field:**
   - Near the top of the settings panel
   - Currently shows a static string like: `1phsPsEpGjubKaQ4T3-cnuol3lNGKFs80`

5. **Clear the static Folder ID:**
   - Click inside the Folder ID field
   - Delete the entire static string
   - Field should now be empty

6. **Map to Module 25's folder:**
   - With Folder ID field active (cursor blinking inside)
   - Right panel should show available modules
   - Scroll to find "Module 25: Google Drive - Create a Folder"
   - Expand Module 25
   - Look for "Folder ID" (NOT "Name", NOT "Web View Link")
   - Click on **"Folder ID"**

7. **Verify the mapping:**
   - Folder ID field should now show:
     ```
     {{25.Folder ID}}
     ```
   - This means: "Upload to whatever folder Module 25 just created"
   - This is dynamic - changes for each blog title

8. **Verify File Name is correct:**
   - Should show: `{{20.Blog_Title (A)}}_Pin_{{24.Bundle order position}}`
   - This creates names like: "Winter Car Safety_Pin_1"
   - Leave as-is if correct

9. **Verify Data field is mapped:**
   - Scroll to Data field
   - Should show: `{{21.Generated Images[].Image Data}}`
   - If empty, follow steps from Fix 1 but use Module 21 instead of Module 18

10. **Save the changes:**
    - Click OK to close Module 11
    - Click Save to save automation

11. **Test with ONE blog title:**
    - Set one row in Pinterest_Pins sheet to SCHEDULED
    - Run automation
    - Check Drive

12. **Expected results:**
    - ✅ Subfolder created with blog title name
    - ✅ Images appear INSIDE the subfolder (not in parent)
    - ✅ File names show: [Blog Title]_Pin_1, _Pin_2, _Pin_3
    - ✅ Each image is 1.3-1.5MB and viewable

---

### FIX 3: Pinterest Images - Remove Hex Codes from Prompts

**Problem:** Text/hex codes appearing in generated images
**Fix Location:** Module 19 (Gemini) prompt + Module 21 (Imagen) negative prompt
**Time:** 5 minutes

#### Part A: Fix Module 19 Prompt Template

1. **Open Pinterest automation** in Make.com

2. **Find Module 19:**
   - Look for "Google Vertex AI (Gemini) - Create a Chat Prompt (Gemini)"
   - Should be a blue/purple AI icon

3. **Click on Module 19** to open settings

4. **Find the Messages section:**
   - Look for "Messages" field
   - Should contain a long prompt template
   - This is the template that creates Pinterest image descriptions

5. **Search for the color palette section:**
   - Use Cmd+F (Mac) or Ctrl+F (Windows) to search in the prompt
   - Search for: "#937F71" or "warm earth tone palette"
   - You should find text like:
     ```
     warm earth tone palette (#937F71 taupe, #EEECE6 cream, #E0CFBD beige)
     ```

6. **Replace with descriptive text only:**
   - **OLD TEXT:**
     ```
     warm earth tone palette (#937F71 taupe, #EEECE6 cream, #E0CFBD beige)
     ```

   - **NEW TEXT:**
     ```
     warm earth tone palette with soft taupe, warm cream, and gentle beige tones
     ```

7. **Check for any other hex codes:**
   - Search the entire prompt for "#"
   - Remove ANY hex color codes
   - Replace with color names only (taupe, cream, beige, etc.)

8. **Save Module 19:**
   - Click OK to close module

#### Part B: Update Module 21 Negative Prompt

1. **Find Module 21** in the flow:
   - "Google Vertex AI (Gemini) - Generate an Image"
   - Blue/purple AI icon, after Module 19

2. **Click on Module 21** to open settings

3. **Find the "Negative Prompt" field:**
   - Should be in the middle section of settings
   - Currently contains a long list of things to avoid

4. **Locate the end of the negative prompt:**
   - Current ending should be something like:
     ```
     ...any readable characters, alphabet letters"
     ```

5. **Add hex code blockers:**
   - Place cursor at the end of the negative prompt
   - BEFORE the closing quote mark
   - Add this text:
     ```
     , hex codes, color codes, hashtags, #
     ```

6. **Final negative prompt should end with:**
   ```
   ...any readable characters, alphabet letters, hex codes, color codes, hashtags, #"
   ```

7. **Save Module 21:**
   - Click OK to close module

8. **Save entire automation:**
   - Click Save button

9. **Test with one Pinterest pin:**
   - Set one row to SCHEDULED
   - Run automation
   - Check generated images

10. **Expected results:**
    - ✅ No text overlays on images
    - ✅ No hex codes visible
    - ✅ No hashtags or symbols
    - ✅ Clean, professional dog images with warm color tones
    - ✅ Product (harness) visible and clear

---

## How to Diagnose Which Problem You Have

When images aren't generating, follow this diagnostic flow:

### Step 1: Check if Images Are Being Generated

**What to check:**
1. Run automation with ONE test row
2. Go to Make.com → Execution History
3. Click on the most recent execution
4. Find Module 18 (for blog) or Module 21 (for Pinterest)
5. Click on the module in the execution flow
6. Look at the OUTPUT section

**What you should see:**
```
Generated Images[]
  1Collection
    Image DataBuffer, codepage: binary
    ff d8 ff e0 00 10 4a 46... [long string of characters]
    End of data sample, buffer was originally 422471 bytes long.
    SHA1: 670c0dffd66b6c583c4f5fe7bf55df84ac22cd11
    Mime Type: image/jpeg
```

**Diagnosis:**
- ✅ If you see this with size > 400KB → Images ARE generating, problem is in upload
- ❌ If you see empty or error → Images NOT generating, problem is in Imagen module settings
- 🔧 If images not generating, check:
  - Gemini prompt in Module 19 (Pinterest) or Module 18 (Blog)
  - Imagen API connection is active
  - GCP project has Imagen API enabled

---

### Step 2: Check if Module 11 Is Receiving Data

**What to check:**
1. Same execution history view
2. Find Module 11 (Google Drive - Upload a File)
3. Click on it
4. Look at the INPUT section (not output)

**What you should see:**
```
Bundle 1Collection
  DataBuffer, codepage: binary
  [image data buffer shown]
  File Name: Winter Car Safety Tips.jpg
  Folder ID: 1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4
```

**Diagnosis:**
- ✅ If Input shows "DataBuffer" → Module 11 is receiving data correctly
- ❌ If Input shows "Bundle 1: empty" → Module 11 not receiving data
- 🔧 If empty, go to **FIX 1** - Data field not mapped

---

### Step 3: Check Module 11 Output

**What to check:**
1. Same execution, Module 11
2. Look at OUTPUT section

**What you should see:**
```
Bundle 1Collection
  Name: Winter Car Safety Tips.jpg
  Mime Type: image/jpeg
  Size: 422471
  Quota Bytes Used: 422471
  Web View Link: https://drive.google.com/file/d/xxx/view
```

**Diagnosis:**
- ✅ Size > 400000 = Image uploaded successfully
- ✅ Mime Type: image/jpeg = Correct file type
- ✅ Name = blog title = File naming working
- ❌ Size: 0 = Empty file uploaded
- ❌ Mime Type: application/octet-stream = Wrong file type
- ❌ Name: Untitled = File naming not working
- 🔧 If any ❌, check Module 11 configuration against FIX 1

---

### Step 4: Check Drive Location (Pinterest Only)

**What to check:**
1. Open Google Drive
2. Navigate to HappyPawsCo_Pinterest folder
3. Look for blog-title subfolders (e.g., "Winter Car Safety")

**What you should see:**
- ✅ Subfolders exist with blog title names
- ✅ Each subfolder contains 3 image files
- ✅ Images named: [Blog Title]_Pin_1, _Pin_2, _Pin_3
- ✅ Each image 1.3-1.5MB

**Diagnosis:**
- ❌ Subfolders empty, images in parent = Wrong folder mapping
- 🔧 Go to **FIX 2** - Update Folder ID to dynamic reference
- ❌ Text appearing on images = Hex code issue
- 🔧 Go to **FIX 3** - Remove hex codes from prompts

---

## Prevention Checklist

**Before running automation each time:**

□ Open Module 11 and verify Data field shows mapping pill (not empty)
□ Verify File Name field shows blog title mapping
□ For Pinterest: verify Folder ID shows `{{25.Folder ID}}` (not static ID)
□ Check one recent execution history to confirm last run worked

**After making ANY changes to automation:**

□ Test with exactly ONE row set to SCHEDULED
□ Check execution history for that specific run
□ Verify Module 18/21 output shows image buffer
□ Verify Module 11 input shows DataBuffer
□ Verify Module 11 output shows size > 400000
□ Check Drive file actually displays image
□ For Pinterest: check image is INSIDE subfolder

**Monthly maintenance:**

□ Review execution history for any failed runs
□ Check Drive storage space (large image files add up)
□ Test one blog and one Pinterest pin to verify both working
□ Review this troubleshooting doc before making changes

---

## Quick Reference Table

| Symptom | Location | Issue | Fix |
|---------|----------|-------|-----|
| Empty images (0 bytes) | Module 11 | Data field not mapped | Map to `{{18.Generated Images[].Image Data}}` (blog) or `{{21.Generated Images[].Image Data}}` (Pinterest) |
| File named "Untitled" | Module 11 | File Name not mapped | Map to `{{20.Blog_Title}}.jpg` |
| Images in wrong folder | Module 11 | Static folder ID | Change to `{{25.Folder ID}}` (Pinterest only) |
| Text on images | Module 19 + 21 | Hex codes in prompt | Remove hex codes, add to negative prompt |
| "No preview available" | Module 11 | Data field empty | Same as empty images fix |
| Wrong mime type | Module 11 | Data field empty or wrong mapping | Verify mapping to Image Data (not Mime Type field) |

---

## Contact Information for Future Reference

**Automation Names:**
- Blog: "Blog Generator - NEW Workflow Sheet v1"
- Pinterest: "Pinterest Pin Generator - NEW Workflow Sheet v1"

**Key Module Numbers:**
- **Blog:** Module 18 = Imagen, Module 11 = Upload, Module 20 = Sheet Search
- **Pinterest:** Module 21 = Imagen, Module 19 = Gemini, Module 25 = Create Folder, Module 11 = Upload

**Google Drive Folders:**
- Blog Images: Folder ID `1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4`
- Pinterest Parent: Folder ID `1phsPsEpGjubKaQ4T3-cnuol3lNGKFs80`
- Pinterest Subfolders: Created dynamically by Module 25

**Google Sheets:**
- Blog: "Blog_Calendar" sheet
- Pinterest: "Pinterest_Pins" sheet

---

## Additional Notes

**Why these problems are common:**
- Module 11's Data field is not obvious - it only appears when "Map" mode is selected
- Make.com doesn't show an error if Data field is empty - it just creates an empty file
- Dynamic folder references (Module 25) aren't intuitive - easy to use static IDs instead
- Hex codes LOOK like instructions but render as text - counterintuitive behavior

**This happened because:**
- User cleared old blog topics and added new ones
- This likely required updating/recreating some modules
- During updates, mappings can be lost or reset to defaults
- Make.com doesn't always preserve mappings when modules are edited

**Future-proofing:**
- Before making ANY changes to automation, screenshot the working module settings
- Store screenshots in: `/HappyPawsCo - Working Make.com Automations/Screenshots/`
- Document what you changed and when
- Always test with ONE row after changes

---

**Created:** December 27, 2024
**Last Updated:** December 27, 2024
**Next Review:** When automation breaks again (hopefully never!)
**Status:** Both automations working perfectly as of Dec 27, 2024 6:30 PM GMT
