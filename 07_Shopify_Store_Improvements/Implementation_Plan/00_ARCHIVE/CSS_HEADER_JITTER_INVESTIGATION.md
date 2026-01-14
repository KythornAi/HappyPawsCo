# CSS Header Jitter Investigation Plan
**Issue:** Header and announcement bar causing "jumping" effect on scroll  
**Priority:** CRITICAL - Fix before launch  
**Date:** December 29, 2024

---

## Issue Description

**Symptom:**
- Header and announcement bar "jump" or "jitter" when scrolling
- Content below shifts unexpectedly
- Creates poor user experience

**Root Cause (Likely):**
- Announcement bar changing height during scroll
- CSS animations causing layout shifts
- Missing fixed heights or min-heights
- Transform properties not used (using margin/padding instead)

---

## What I'll Investigate

### 1. Announcement Bar CSS
- Current height settings
- Animation properties
- Scroll behavior
- Transform vs. margin/padding usage

### 2. Header CSS
- Fixed/sticky positioning
- Height calculations
- Z-index issues
- Scroll event handlers

### 3. Theme Structure
- Section templates
- Liquid code
- JavaScript files (if any)
- Asset files

---

## Investigation Process

### Step 1: Access Theme Files

**I'll look for:**
- `assets/theme.css` or similar
- `sections/announcement-bar.liquid`
- `sections/header.liquid`
- `layout/theme.liquid`

### Step 2: Identify Problem Code

**Looking for:**
```css
/* Problem patterns: */
- Height changes on scroll
- Margin/padding animations
- Missing min-height
- Transform not used
- Will-change not set
```

### Step 3: Provide Fix

**Likely solutions:**
```css
/* Fix 1: Fixed height */
.announcement-bar {
  min-height: 40px; /* or actual height */
  height: 40px;
}

/* Fix 2: Use transform */
.header {
  transform: translateY(0);
  will-change: transform;
}

/* Fix 3: Prevent collapse */
.section {
  min-height: [value];
}
```

---

## Expected Outcomes

### Scenario 1: Simple CSS Fix (80% likely)
- Issue: Missing min-height or height property
- Fix: Add fixed height to announcement bar
- Time: 15-30 minutes
- I can do: ✅ Yes

### Scenario 2: Animation Issue (15% likely)
- Issue: CSS animations causing layout shifts
- Fix: Use transform instead of margin/padding
- Time: 30-45 minutes
- I can do: ✅ Yes

### Scenario 3: JavaScript Issue (5% likely)
- Issue: JavaScript changing heights on scroll
- Fix: Modify JavaScript or add CSS overrides
- Time: 1-2 hours
- I can do: ⚠️ Maybe (depends on complexity)

---

## How I'll Access Files

### Option A: Direct Access (If You Grant Admin)
1. Navigate to: Themes → Edit Code
2. Read CSS and Liquid files
3. Identify issue
4. Provide fix code
5. Apply fix (with your approval)

### Option B: File Sharing
1. You export theme or copy CSS files
2. Share files with me
3. I analyze and provide fix
4. You paste code back into Shopify

---

## Fix Implementation

### Once I Identify the Issue:

**Step 1: I'll provide fix code**
```css
/* Example fix */
.announcement-bar {
  min-height: 40px;
  height: 40px;
  will-change: auto;
}

.header {
  position: sticky;
  top: 0;
  z-index: 100;
}
```

**Step 2: You approve**
- Review the fix
- Understand what it does
- Approve application

**Step 3: I apply (or you paste)**
- Apply fix to theme
- Test on preview
- Verify it works

**Step 4: Test**
- Test on desktop
- Test on mobile
- Test scroll behavior
- Verify no jitter

---

## Testing Checklist

After fix is applied:

- [ ] Scroll down page - no jitter
- [ ] Scroll up page - no jitter
- [ ] Test on mobile device
- [ ] Test on tablet
- [ ] Test on desktop
- [ ] Check announcement bar rotation
- [ ] Verify header stays in place
- [ ] No layout shifts

---

## Backup Safety

**Before making CSS changes:**
- ✅ Theme backup created (you'll do this)
- ✅ Can revert if needed
- ✅ Test in preview first
- ✅ Only publish when confirmed working

---

## Timeline

### Investigation Phase:
- **Access files:** 5 minutes
- **Identify issue:** 15-30 minutes
- **Create fix:** 15-30 minutes
- **Total:** 35-65 minutes

### Implementation Phase:
- **Apply fix:** 5 minutes
- **Test:** 10-15 minutes
- **Refine if needed:** 10-20 minutes
- **Total:** 25-40 minutes

### Grand Total: 1-2 hours

---

## Next Steps

**Once you've created backup:**

1. **Grant access or share files:**
   - Option A: Give me Shopify admin access
   - Option B: Share theme CSS files

2. **I'll investigate:**
   - Read theme files
   - Identify jitter cause
   - Provide fix code

3. **We'll test:**
   - Apply fix
   - Test scroll behavior
   - Verify it works

4. **Done:**
   - Jitter fixed
   - Ready for launch

---

**Ready to start investigation?** Create your theme backup first, then let me know when you're ready!

---

**Last Updated:** December 29, 2024

