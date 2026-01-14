# Pinterest Automation - New Workflow Sheet Import Instructions

## File to Import
**`UPDATED_Pinterest_New_Workflow_v1.blueprint.json`**

---

## What Changed

### ✅ OLD Setup (No Longer Used):
- Pinterest_Pins tab in Blog sheet
- Images uploaded to single root folder
- No special instructions support
- Status updates to same input sheet

### ✅ NEW Setup (This Update):
- **Pinterest_Workflow** sheet (8 columns, separate from blog)
- Images organized in **subfolders per blog title**
- **Special Instructions** support (optional nudges)
- Clean separation: input triggers → output results

---

## Your New Pinterest_Workflow Sheet

**Spreadsheet ID:** `1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE`

### 8 Columns:
| Column | Name | You Fill | Auto-Filled |
|--------|------|----------|-------------|
| A | Blog_Title | ✅ Type blog title | |
| B | Pin_Special_Instructions | ✅ Optional nudges | |
| C | Generated_Date | | ✅ Timestamp |
| D | Drive_Folder_Link | | ✅ Click to see 3 images |
| E | Pin_Status | ✅ SCHEDULED to start | ✅ Changes to NEEDS_REVIEW |
| F | Canva_Done | ✅ Checkbox when done | |
| G | Posted_Date | ✅ When posted | |
| H | Notes | ✅ Your notes | |

---

## Import Steps

### Step 1: Backup Current Automation
1. Go to Make.com
2. Open your current Pinterest automation
3. Click **three dots** > **Export Blueprint**
4. Save as backup (just in case)

### Step 2: Import New Automation
1. Go to Make.com > **Scenarios**
2. Click **Create a new scenario**
3. Click **three dots menu** > **Import Blueprint**
4. Upload: `UPDATED_Pinterest_New_Workflow_v1.blueprint.json`
5. Wait for import to complete

### Step 3: Reconnect Your Accounts

⚠️ **IMPORTANT:** You'll need to remap 2 connections and 2 spreadsheet IDs.

#### Connection 1: Google Sheets (Module 20 - Filter Rows)
1. Click on **Module 20** (Google Sheets - Filter Rows)
2. Click **Choose a connection**
3. Select: **My Google connection (casadecashflow@gmail.com)**
4. **Spreadsheet ID:** Click dropdown and search for **"Pinterest_Workflow"**
   - OR manually paste: `1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE`
5. **Sheet Name:** Select **"Pinterest_Workflow"** (should be Sheet1 if you haven't renamed it)
6. Verify filter shows: **Column E (Pin_Status) = SCHEDULED**
7. Click **OK**

#### Connection 2: Google Vertex AI (Module 19 - Gemini)
1. Click on **Module 19** (Gemini Multimodal Prompt)
2. Click **Choose a connection**
3. Select your existing Vertex AI connection
4. Verify:
   - Model: **gemini-2.5-flash**
   - Temperature: **0.7** (changed from 0.9 for less text overlay issues)
   - Response Type: **application/json**
5. Click **OK**

#### Connection 3: Google Drive (Module 27 - NEW - Create Folder)
1. Click on **Module 27** (Create a Folder)
2. Click **Choose a connection**
3. Select: **My Google connection (casadecashflow@gmail.com)**
4. **Folder Name:** Should show `{{20.1}}` (blog title from sheet)
5. **Parent Folder:** Should show folder ID `1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4`
   - ⚠️ **VERIFY THIS IS YOUR "Pinterest_Pins" FOLDER**
   - If not, click **Map** and select your Pinterest_Pins folder
6. Click **OK**

#### Connection 4: Google Drive (Module 11 - Upload Image)
1. Click on **Module 11** (Upload a File)
2. Connection should auto-reconnect
3. Verify **Folder ID** shows: `{{27.id}}` (uses folder created by Module 27)
4. Verify **Filename** shows: `{{20.1}}_Pin_{{24.__IMTINDEX__}}.jpg`
5. Click **OK**

#### Connection 5: Google Sheets (Module 13 - Update Row)
1. Click on **Module 13** (Google Sheets - Update Row)
2. Click **Choose a connection**
3. Select: **My Google connection (casadecashflow@gmail.com)**
4. **Spreadsheet ID:** Click dropdown and search for **"Pinterest_Workflow"**
   - OR manually paste: `1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE`
5. **Sheet Name:** Select **"Pinterest_Workflow"**
6. **Row Number:** Should show `{{20.__ROW_NUMBER__}}`
7. **Values:** Verify it shows:
   - Column C (3): `={{NOW()}}`
   - Column D (4): `=HYPERLINK("{{27.webViewLink}}"; "View Folder")`
   - Column E (5): `NEEDS_REVIEW`
8. Click **OK**

### Step 4: Save and Test

1. Click **Save** (bottom right)
2. Name it: **"Pinterest Pin Generator - New Workflow v1"**
3. Turn it **ON** (toggle in bottom left)

---

## Test Run

### Prepare Test Data:
1. Open your **Pinterest_Workflow** sheet
2. Add a test row:
   - **A (Blog_Title):** "Bringing Home a New Puppy Car Travel Guide"
   - **B (Pin_Special_Instructions):** "Show 8-week puppy in carrier, mention Rule 57"
   - **E (Pin_Status):** "SCHEDULED"

### Run Automation:
1. In Make.com, click **Run once**
2. Watch the modules execute
3. Check for errors

### Verify Results:
1. Check **Pinterest_Workflow** sheet:
   - Column C should have today's date
   - Column D should have "View Folder" link (click it!)
   - Column E should say "NEEDS_REVIEW"
2. Click the **Drive_Folder_Link**:
   - Should open a folder named "Bringing Home a New Puppy Car Travel Guide"
   - Should contain 3 images: Pin 1, Pin 2, Pin 3
3. Open the images - verify NO TEXT overlays appear in the images

---

## Module Flow Overview

Here's what happens when you run this automation:

```
1. Module 20 → Reads Pinterest_Workflow sheet where Status = SCHEDULED
2. Module 19 → Gemini generates 3 pin descriptions (JSON)
                Uses Blog_Title + Special_Instructions
3. Module 23 → Parses JSON
4. Module 24 → Iterator (loops 3 times for 3 pins)
   ├─ Module 27 → Creates Drive subfolder (only on first loop)
   ├─ Module 21 → Imagen generates image
   └─ Module 11 → Uploads image to subfolder
5. Module 13 → Updates Pinterest_Workflow sheet:
                - Generated_Date
                - Drive_Folder_Link
                - Status = NEEDS_REVIEW
```

---

## Troubleshooting

### Issue: "Spreadsheet not found"
**Fix:** Make sure you're selecting **Pinterest_Workflow** sheet ID `1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE` in both Module 20 and Module 13.

### Issue: "No rows returned"
**Fix:** Check your Pinterest_Workflow sheet has:
- At least one row with data
- Column E (Pin_Status) = "SCHEDULED"

### Issue: "Folder not created"
**Fix:**
- Check Module 27 parent folder ID is correct
- Verify you have permissions to create folders in Google Drive

### Issue: "Images not appearing in sheet"
**Fix:**
- Check Module 13 is writing to correct columns (C, D, E)
- Verify Module 27's webViewLink is being passed to Module 13

### Issue: "Text still appearing in images"
**Fix:**
- Temperature is now 0.7 (down from 0.9) - should reduce this
- If it persists, consider using ENHANCED_Pinterest_Prompt_v2.blueprint.json instead (has stronger text warnings)

---

## What's Different from ENHANCED_Pinterest_Prompt_v2.blueprint.json?

You have TWO Pinterest automation files now:

1. **UPDATED_Pinterest_New_Workflow_v1.blueprint.json** ⬅️ **START WITH THIS**
   - Uses your new 8-column Pinterest_Workflow sheet
   - Creates Drive subfolders per blog
   - Supports Special Instructions
   - Uses original Gemini prompt (proven to work)
   - Temperature: 0.7

2. **ENHANCED_Pinterest_Prompt_v2.blueprint.json**
   - MUCH longer Gemini prompt (15,541 chars vs ~4,200)
   - Stronger rules against text appearing
   - More visual cohesion rules
   - BUT: Still uses old Pinterest_Pins sheet structure

### Recommendation:
- Import **UPDATED_Pinterest_New_Workflow_v1.blueprint.json** FIRST
- Test it with 2-3 blog titles
- If text still appears in images, we can merge the ENHANCED prompt into this new workflow

---

## Your Workflow Going Forward

### Weekend Batch Work:
1. Type 8 blog titles into **Pinterest_Workflow** sheet (Column A)
2. Add special instructions if needed (Column B)
3. Set all to Status = "SCHEDULED" (Column E)
4. Run automation **ONCE**
5. Wait ~10-15 minutes for all pins to generate
6. Check Column D for Drive folder links
7. Download all images, add text overlays in Canva
8. Mark Column F (Canva_Done) as checked

### Throughout the Month:
- Post pins according to your schedule
- Update Column E (Pin_Status) to "POSTED"
- Add Column G (Posted_Date)
- Add Column H (Notes) if needed

---

## Need Help?

If you encounter issues:
1. Check the module that failed (Make.com shows errors)
2. Verify your sheet has correct column structure
3. Verify all spreadsheet IDs are `1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE`
4. Check Drive folder ID in Module 27 is your Pinterest_Pins parent folder

---

**Created:** December 26, 2024
**Automation Version:** v1 - New Workflow Sheet Integration
**Sheet ID:** 1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE
