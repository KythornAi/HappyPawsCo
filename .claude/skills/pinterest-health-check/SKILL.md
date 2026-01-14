---
name: pinterest-health-check
description: Quickly validate that Pinterest Pin Generator automation is correctly configured and working properly. Check Pinterest automation, review Make.com settings, troubleshoot pin generation, verify Pinterest workflows.
---
# Pinterest Automation Health Check Skill

## Purpose
Quickly validate that the HappyPawsCo Pinterest Pin Generator automation is correctly configured and hasn't been accidentally broken.

## When to Use
- Before running monthly Pinterest batch generation
- After making any changes to the automation
- If pins start having issues (text appearing, low quality, etc.)
- After Make.com updates or maintenance

## What This Skill Checks

### ✅ Critical Configuration Items

1. **Module 19 - Gemini Prompt Settings**
   - Temperature is 0.7 (NOT 0.9)
   - Blog_Title mapping format is correct
   - Special_Instructions mapping format is correct
   - Response format is application/json
   - Model is gemini-2.5-flash

2. **Module 13 - Google Sheets Update Settings**
   - Column C uses formatDate function (NOT a mapping)
   - Column D has HYPERLINK formula with Module 25 reference
   - Column E is literal text "NEEDS_REVIEW" (NOT a mapping)
   - Sheet name is "Pinterest_Pins"
   - Spreadsheet ID is correct

3. **Module 25 - Drive Folder Creation**
   - Folder name maps to Blog_Title
   - Parent folder ID is correct
   - Filter only runs on first iteration

4. **Module 20 - Sheet Filter**
   - Sheet name is "Pinterest_Pins"
   - Filter checks Column E equals "SCHEDULED"
   - Spreadsheet ID is correct

5. **Module 11 - File Upload**
   - Folder ID references Module 25
   - File name includes blog title and pin index
   - Data field references Imagen output

## Expected Configuration

### Module 19 Settings:
```
Temperature: 0.7
Model: gemini-2.5-flash
Blog Title: {{20.Blog_Title (A)}} or {{20.1}}
Special Instructions: {{20.Pin_Special_Instructions (B)}} or {{20.2}}
Response Format: application/json
```

### Module 13 Settings:
```
Spreadsheet ID: 1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE
Sheet Name: Pinterest_Pins
Column C: {{formatDate(now; "DD/MM/YYYY")}}
Column D: =HYPERLINK("{{25.Web View Link}}"; "View Folder")
Column E: NEEDS_REVIEW
```

### Module 25 Settings:
```
Folder Name: {{20.Blog_Title (A)}} or {{20.1}}
Parent Folder: 1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4
Filter: Bundle order position = 1
```

### Module 20 Settings:
```
Spreadsheet ID: 1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE
Sheet Name: Pinterest_Pins
Filter: Column E equals SCHEDULED
```

## Common Issues & Fixes

### Issue: Text Appearing in Images
**Check:**
- Module 19 temperature is 0.7 (NOT 0.9)
- Blog_Title mapping is correct format (not `{{20.`0`}}`)

**Fix:**
- Set temperature to 0.7
- Update mapping to `{{20.Blog_Title (A)}}`

### Issue: Generated_Date Not Populating
**Check:**
- Module 13 Column C is NOT mapped to `{{20.Generated_Date (C)}}`

**Fix:**
- Change to: `{{formatDate(now; "DD/MM/YYYY")}}`

### Issue: Status Not Changing
**Check:**
- Module 13 Column E is NOT mapped to `{{20.Pin_Status (E)}}`

**Fix:**
- Change to literal text: `NEEDS_REVIEW`

### Issue: Folder Not Created
**Check:**
- Module 25 filter is set (Bundle order position = 1)
- Parent folder ID is correct

**Fix:**
- Add filter to only run on first iteration
- Verify parent folder ID: 1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4

### Issue: No Rows Found
**Check:**
- Sheet tab name is "Pinterest_Pins"
- At least one row has Column E = "SCHEDULED"

**Fix:**
- Verify sheet tab name matches
- Add a test row with SCHEDULED status

## How to Run Health Check

When user asks to "check Pinterest automation" or "validate Pinterest setup":

1. **Ask user to provide:**
   - Screenshot of Module 19 settings (temperature, mappings)
   - Screenshot of Module 13 values section
   - Screenshot of Module 25 settings
   - OR access to the automation blueprint/scenario

2. **Verify each critical setting:**
   - Compare against expected configuration above
   - Flag any mismatches

3. **Report findings:**
   - ✅ What's correct
   - ⚠️ What needs attention
   - ❌ What's broken
   - 🔧 How to fix issues

4. **Provide fix instructions:**
   - Step-by-step for any issues found
   - Reference handover document for context

## Red Flags 🚩

These settings should NEVER be changed:

- ❌ Temperature > 0.7 (causes text generation)
- ❌ Column C mapped to sheet column (should be formatDate function)
- ❌ Column E mapped to sheet column (should be literal "NEEDS_REVIEW")
- ❌ Module 25 without filter (creates 3 folders instead of 1)
- ❌ Blog_Title in format `{{20.`0`}}` (broken mapping)

## Success Criteria

Automation is healthy when:
- ✅ All module settings match expected configuration
- ✅ No red flags detected
- ✅ Recent test run produced 3 usable pins
- ✅ No text appearing in images
- ✅ Folder structure organized correctly
- ✅ Sheet updates populating correctly

## Quick Test

To verify automation is working:
1. Add test row to Pinterest_Workflow sheet
2. Blog_Title: "Test Health Check"
3. Pin_Status: "SCHEDULED"
4. Run automation once
5. Check results:
   - ✅ 3 images generated
   - ✅ No text overlays
   - ✅ Folder created with blog title
   - ✅ Sheet updated with date, link, status

## Reference Documents

- **Handover Summary:** `/02_Pinterest_Automation/SESSION_HANDOVER_Dec26_2024.md`
- **Quick Start:** `/02_Pinterest_Automation/QUICK_START_New_Workflow.md`
- **Troubleshooting:** `/02_Pinterest_Automation/TROUBLESHOOTING_GUIDE.md`

## Version Info

- **Created:** December 26, 2024
- **Automation Version:** Pinterest Pin Generator - NEW Workflow Sheet v1
- **Last Known Working Config:** See SESSION_HANDOVER_Dec26_2024.md
- **Sheet ID:** 1xCcDKooyPShQx7pYuqzzs4CQ3Xlo6groSLXbQa82ekE
- **Parent Folder ID:** 1YwU4p-azYip_AZc2mXXOeKCXM6EXCMh4
