# Content-Inventory Alignment Agent

**Version**: 1.0
**Created**: 2026-01-12
**Purpose**: Ensure blog content aligns with current product inventory

## What It Does

This agent scans your blog content and checks that:

- ✅ Products mentioned are ACTIVE (not discontinued)
- ✅ Product links are correct
- ✅ Product count stays within 3-per-blog guideline
- ✅ Product positioning matches Blog Usage Notes
- ✅ No missed opportunities for better product matches

## Quick Start

**Invoke with**: Use the Task tool and provide blog content

**Example commands**:
- "Check this blog for product alignment" [paste blog]
- "Scan my muddy paws blog for inventory issues"
- "Verify products in my cat care blog are still active"

## Scanning Modes

1. **Quick Scan**: Fast check for existence, status, count
2. **Deep Analysis**: Full positioning review + suggestions
3. **Batch Mode**: Scan multiple blogs at once

## Output

Generates clear, prioritized report with:
- 🚨 **CRITICAL**: Fix immediately (discontinued products, broken links)
- ⚠️ **IMPORTANT**: Review soon (positioning issues, count problems)
- 💡 **SUGGESTIONS**: Nice to have (optimization ideas)

## Brand Guidelines Enforced

- **Max 3 products per blog** (keeps it helpful, not salesy)
- **Positioning alignment** with product Blog Usage Notes
- **Safety context** for safety products
- **Correct URLs** from official product database

## Works With

- **Product Database Agent** (verifies all product data)
- **Blog Publisher Agent** (pre-publish checks)
- **Blog Quality Checker Skill** (comprehensive quality review)

## Current Settings

**Recommendation Mode**: Suggest (don't auto-update)
- You review recommendations
- You decide what to change
- Manual application for now
- *(Can switch to auto-update after testing)*

---

🐾 Your content watchdog - keeping blogs aligned with inventory!
