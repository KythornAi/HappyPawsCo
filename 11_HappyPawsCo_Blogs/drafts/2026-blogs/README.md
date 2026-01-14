# Draft Blogs - 2026

Raw blogs waiting to be polished by the Blog Publisher Agent.

## What Goes Here
- Older blogs from Make.com experiments (early 2025)
- New blogs from current Make.com automation
- The 5 existing blogs on the pre-launch site
- Any blog content needing polish

## Folder Structure

Each blog gets its own folder named with the blog slug (kebab-case):

```
drafts/2026-blogs/
└── blog-title-slug/
    ├── draft.md              # Required: Raw blog content
    ├── image-prompts.md      # Optional: If already generated
    └── images/               # Optional: If images already exist
```

## Next Step

Once a blog is ready:
1. Run Blog Publisher Agent on `draft.md`
2. Run Image Prompter Agent if needed
3. Save outputs to `polished/2026-blogs/[blog-slug]/`
