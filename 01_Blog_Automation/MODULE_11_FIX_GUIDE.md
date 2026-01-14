# Module 11 Fix Guide - Blog Automation
**Date:** December 27, 2024
**Issue:** Images not uploading to Drive (0-byte empty files)
**Cause:** Data field not mapped to Module 18 image output

---

## Step-by-Step Fix

### 1. Open Module 11 (Google Drive - Upload a File)

### 2. Configure These Fields:

**Drive** (select your Google Drive account)

**Folder ID**
- **Option A:** Leave BLANK (uploads to root)
- **Option B:** Paste your Drive folder ID (like `0APKOZKAGbus9Uk9PVA`)
- **DO NOT** put any sheet mappings here

**File Name**
```
{{20.Blog_Title (A)}}.jpg
```
(This names the file after your blog title)

**File Section**
- Click the **"Map"** radio button (NOT "Google Drive - Download a File")
- This reveals the Data field below

**Data** (THIS IS WHERE THE IMAGE GOES)
```
{{18.Generated Images[].Image Data}}
```
(This is the 422KB image buffer from Module 18)

---

## What Each Field Does

| Field | Purpose | Correct Value |
|-------|---------|---------------|
| **Folder ID** | Where to save file | Blank or folder ID string |
| **File Name** | What to name the file | `{{20.Blog_Title (A)}}.jpg` |
| **Data** | The actual file content | `{{18.Generated Images[].Image Data}}` |

---

## Common Mistakes

❌ **WRONG:** Putting `{{20.Image_URL (G)}}` in Folder ID
- Image_URL is a sheet column that gets populated AFTER upload
- You can't use it as input to the upload

❌ **WRONG:** Using "Google Drive - Download a File" mode
- This tries to download an existing file
- You need "Map" mode to upload new data

✅ **CORRECT:** Map image buffer from Module 18 to Data field
- Module 18 generates the image
- Module 11 uploads that image buffer to Drive
- Module 13 writes the Drive link to sheet column G

---

## Visual Flow

```
Module 18 (Imagen)
    ↓ Generates 422KB JPEG buffer
    ↓ Outputs: Generated Images[].Image Data
    ↓
Module 11 (Drive Upload)
    ↓ Receives: {{18.Generated Images[].Image Data}} in Data field
    ↓ Creates: JPEG file in Drive
    ↓ Outputs: webViewLink (Drive URL)
    ↓
Module 13 (Update Sheet)
    ↓ Writes: =HYPERLINK("{{11.webViewLink}}"; "View Image")
    ↓ To column G (Image_URL)
```

---

## After Fixing

**Test with one blog:**
1. Set one row to SCHEDULED
2. Run automation
3. Check Drive - should see JPEG file (not 0-byte "Untitled")
4. Check sheet column G - link should work
5. Status should change to AWAITING_REVIEW

**Expected Module 11 Output:**
```
Size: ~400000 bytes (not 0)
Name: [Your Blog Title].jpg (not "Untitled")
Mime Type: image/jpeg (not application/octet-stream)
```

---

**Created:** December 27, 2024
**Module:** Blog Automation Module 11
**Fix Time:** ~2 minutes once you find the Data field
