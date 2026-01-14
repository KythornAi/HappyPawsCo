# CSS Header Jitter Fix
**Issue:** Header and announcement bar causing "jumping" effect on scroll
**Status:** Root cause identified - Fix ready to apply
**Date:** December 30, 2024

---

## Root Cause Identified

After analyzing your `base.css` file, I found **two issues** causing the jitter:

### Issue 1: Announcement Bar Animations
**Location:** Lines 2255-2288 in base.css

The announcement bar uses **translateX animations** that change the layout during transitions. While the `.announcement-bar__message` has a `min-height: 3.8rem`, the animations can cause micro-shifts.

```css
/* Current animation (causing jitter) */
.announcement-bar-slider--fade-in-next .announcement-bar__message {
  animation-name: translateAnnouncementSlideIn;
  animation-duration: var(--duration-announcement-bar);
}

@keyframes translateAnnouncementSlideIn {
  0% {
    opacity: 0;
    transform: translateX(var(--announcement-translate-from));
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}
```

### Issue 2: Sticky Header Without Fixed Height
**Location:** Lines 2317-2332 in base.css

The header uses `position: sticky` and references `var(--header-height)`, but this variable might not be consistently defined or the header height changes during scroll.

```css
/* Current sticky header */
.shopify-section-header-sticky {
  position: sticky;
  top: 0;
}

.shopify-section-header-hidden {
  top: calc(-1 * var(--header-height));
}
```

---

## The Fix

Add this CSS to your theme to eliminate jitter:

### Step 1: Fix Announcement Bar

**Add this CSS** (paste at the end of base.css or in your custom CSS section):

```css
/* ==== FIX: Announcement Bar Jitter ==== */

/* Force consistent height on announcement bar container */
.announcement-bar,
.announcement-bar-slider {
  min-height: 3.8rem;
  height: 3.8rem;
}

/* Ensure animations don't cause layout shifts */
.announcement-bar__message {
  will-change: opacity; /* Only animate opacity, not transform */
  backface-visibility: hidden;
  transform: translateZ(0); /* Force GPU acceleration */
}

/* Override translateX animations to use opacity only */
.announcement-bar-slider--fade-in-next .announcement-bar__message,
.announcement-bar-slider--fade-in-previous .announcement-bar__message {
  animation-name: fadeInAnnouncement !important; /* Override existing */
}

.announcement-bar-slider--fade-out-next .announcement-bar__message,
.announcement-bar-slider--fade-out-previous .announcement-bar__message {
  animation-name: fadeOutAnnouncement !important; /* Override existing */
}

/* New animations - opacity only, no transform */
@keyframes fadeInAnnouncement {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes fadeOutAnnouncement {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
```

### Step 2: Fix Sticky Header

**Add this CSS** (paste right after Step 1):

```css
/* ==== FIX: Sticky Header Jitter ==== */

/* Ensure header wrapper has consistent height */
.header-wrapper {
  min-height: 60px; /* Adjust this value to match your actual header height */
}

/* Improve sticky header performance */
.shopify-section-header-sticky {
  position: sticky;
  top: 0;
  will-change: transform;
  backface-visibility: hidden;
  transform: translateZ(0); /* Force GPU acceleration */
}

/* Smooth transition without layout shifts */
.section-header.animate {
  transition: transform 0.15s ease-out; /* Use transform instead of top */
}

.shopify-section-header-hidden {
  transform: translateY(calc(-1 * var(--header-height)));
  /* Instead of: top: calc(-1 * var(--header-height)); */
}

.shopify-section-header-hidden.menu-open {
  transform: translateY(0);
  /* Instead of: top: 0; */
}
```

---

## Complete CSS Fix (Copy & Paste This)

Here's the complete fix in one block - **paste this at the very end of your base.css file**:

```css
/* ========================================
   HEADER JITTER FIX - December 30, 2024
   ======================================== */

/* Fix 1: Announcement Bar Jitter */
.announcement-bar,
.announcement-bar-slider {
  min-height: 3.8rem;
  height: 3.8rem;
}

.announcement-bar__message {
  will-change: opacity;
  backface-visibility: hidden;
  transform: translateZ(0);
}

.announcement-bar-slider--fade-in-next .announcement-bar__message,
.announcement-bar-slider--fade-in-previous .announcement-bar__message {
  animation-name: fadeInAnnouncement !important;
}

.announcement-bar-slider--fade-out-next .announcement-bar__message,
.announcement-bar-slider--fade-out-previous .announcement-bar__message {
  animation-name: fadeOutAnnouncement !important;
}

@keyframes fadeInAnnouncement {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@keyframes fadeOutAnnouncement {
  0% { opacity: 1; }
  100% { opacity: 0; }
}

/* Fix 2: Sticky Header Jitter */
.header-wrapper {
  min-height: 60px; /* Adjust to your actual header height if needed */
}

.shopify-section-header-sticky {
  position: sticky;
  top: 0;
  will-change: transform;
  backface-visibility: hidden;
  transform: translateZ(0);
}

.section-header.animate {
  transition: transform 0.15s ease-out;
}

.shopify-section-header-hidden {
  transform: translateY(calc(-1 * var(--header-height)));
}

.shopify-section-header-hidden.menu-open {
  transform: translateY(0);
}

/* End of Header Jitter Fix */
```

---

## How to Apply This Fix

### Option A: Via Shopify Admin (Recommended)

1. **Go to:** Shopify Admin → Online Store → Themes
2. **Click:** Actions → Edit Code
3. **Find:** `assets/base.css` in the left sidebar
4. **Scroll to the very bottom** of the file
5. **Paste** the complete CSS fix above
6. **Click:** Save
7. **Test** your site (preview first!)

### Option B: Theme Customizer (If Available)

1. **Go to:** Shopify Admin → Online Store → Themes → Customize
2. **Look for:** Custom CSS section (usually in Theme Settings)
3. **Paste** the complete CSS fix
4. **Click:** Save
5. **Test** your site

---

## What This Fix Does

### Before Fix:
- ❌ Announcement bar uses `translateX` animations → causes layout shifts
- ❌ Header uses `top` property for hide/show → causes repaints
- ❌ No fixed heights → content jumps during animations
- ❌ No GPU acceleration → janky animations

### After Fix:
- ✅ Fixed heights on announcement bar → no layout shifts
- ✅ Opacity-only animations → smooth fades without movement
- ✅ `transform` instead of `top` → GPU-accelerated, no reflow
- ✅ `will-change` and `backface-visibility` → optimized rendering
- ✅ `translateZ(0)` → forces GPU acceleration

---

## Testing Checklist

After applying the fix, test:

- [ ] Scroll down the page - no jitter
- [ ] Scroll up the page - no jitter
- [ ] Announcement bar rotates (if you have multiple) - smooth fade
- [ ] Header stays in place during scroll
- [ ] Test on mobile device
- [ ] Test on tablet
- [ ] Test on desktop
- [ ] Check different pages (home, product, collection)
- [ ] No layout shifts (use Chrome DevTools Performance tab)

---

## Troubleshooting

### If jitter persists:

**Check 1: Header Height**
The `.header-wrapper { min-height: 60px; }` value might need adjustment.

**To find your actual header height:**
1. Open your site in Chrome
2. Right-click the header → Inspect
3. Look at the computed height
4. Update `min-height` to match that value

**Check 2: Announcement Bar**
If you have a different announcement bar setup, you may need to adjust:
```css
.announcement-bar {
  min-height: [your-value]rem;
  height: [your-value]rem;
}
```

**Check 3: Cache**
Clear your browser cache and Shopify cache:
- Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Or use incognito/private browsing

---

## Alternative Fix (If Above Doesn't Work)

If the main fix doesn't completely solve it, try this **more aggressive fix**:

```css
/* Disable all announcement bar animations */
.announcement-bar-slider--fade-in-next .announcement-bar__message,
.announcement-bar-slider--fade-in-previous .announcement-bar__message,
.announcement-bar-slider--fade-out-next .announcement-bar__message,
.announcement-bar-slider--fade-out-previous .announcement-bar__message {
  animation: none !important;
  transition: opacity 0.3s ease !important;
}

/* Instant visibility toggle instead of animation */
.announcement-bar-slider--fade-out-next .announcement-bar__message,
.announcement-bar-slider--fade-out-previous .announcement-bar__message {
  opacity: 0;
}

.announcement-bar-slider--fade-in-next .announcement-bar__message,
.announcement-bar-slider--fade-in-previous .announcement-bar__message {
  opacity: 1;
}
```

---

## Backup Plan

**Before applying**, make sure you have:
- ✅ Theme backup (duplicate your theme first)
- ✅ Can revert if needed
- ✅ Test in preview mode first

**To revert:**
Simply remove the CSS you added at the bottom of base.css

---

## Expected Results

**Scroll behavior:**
- Smooth scrolling with no jumps
- Header stays fixed in position
- Announcement bar transitions smoothly
- No content shifts or layout reflows

**Performance:**
- Faster rendering (GPU acceleration)
- Smoother animations
- Better mobile performance

---

## Next Steps

1. **Create theme backup** (Themes → Actions → Duplicate)
2. **Apply the fix** (paste CSS at end of base.css)
3. **Test in preview** (don't publish yet)
4. **Verify no jitter** (scroll test on all devices)
5. **Publish when confirmed working**

**Let me know once you've applied it and I can help troubleshoot if needed!**

---

**Last Updated:** December 30, 2024
