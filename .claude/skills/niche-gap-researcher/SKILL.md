---
name: niche-gap-researcher
description: Identifies underserved market opportunities in your niche through competitor analysis, social listening, and trend research. Outputs prioritized blog topics and product opportunities with demand validation.
---

# Niche Gap Researcher

This skill helps you discover untapped opportunities in your market by analyzing what customers need but aren't getting. It sits at the top of your content and product strategy funnel, feeding actionable insights to your other workflows.

## When to Use This Skill

- Planning your content calendar for the quarter
- Looking for new blog topics with SEO potential
- Identifying product opportunities for your store
- Understanding what competitors are missing
- Finding high-demand, low-competition topics
- Validating market demand before creating content or stocking products
- Refreshing your strategy with fresh market insights

## What This Skill Does

1. **Competitor Analysis**: Examines what others in your niche are writing about and selling
2. **Social Listening**: Monitors Reddit, forums, and social media for customer pain points
3. **Trend Research**: Identifies search trends and emerging topics
4. **Gap Identification**: Finds the "white space" - demand with limited supply
5. **Opportunity Prioritization**: Ranks opportunities by potential impact
6. **Actionable Output**: Delivers specific blog topics and product ideas with evidence

## How to Use

### Basic Usage

```
/niche-gap-researcher
```

The skill will ask you clarifying questions, then conduct comprehensive research.

### With Specific Parameters

```
Research gaps in pet travel accessories, focusing on cat-specific products
```

```
Find underserved topics in the luxury pet travel market
```

```
Identify blog opportunities around budget-friendly pet travel solutions
```

## Instructions

When a user invokes this skill, follow this systematic research process:

### 0. Check Existing Inventory (For Product Research Only)

**CRITICAL:** Before researching product opportunities, ALWAYS check what products HappyPawsCo already stocks to avoid recommending duplicates.

**When to do this:**
- Any time the research includes product opportunities/gaps
- Skip this step for content/blog-only research

**Actions:**
1. Access Google Drive using the google-workspace MCP server
2. Read the spreadsheet: "HappyPawsCo Product Data 11.01.26"
3. Extract all product names, categories, and types currently in inventory
4. Create a list of products to EXCLUDE from recommendations

**How to access:**
```
Use mcp__google-workspace__listGoogleSheets to find the sheet
Then use mcp__google-workspace__readSpreadsheet with the sheet ID
Read all product data to understand current inventory
```

**Output Format:**
```markdown
## Current Inventory Check

**Products Already Stocked:**
- [Category 1]: [Product name 1], [Product name 2]
- [Category 2]: [Product name 3], [Product name 4]
- [etc.]

**Total Products in Inventory:** [X]

**Categories Covered:**
- [Category 1]
- [Category 2]
- [etc.]

**Note:** These products will be EXCLUDED from opportunity recommendations.
```

**If Google Sheet is not accessible:**
- Note this in the report
- Proceed with research but flag products that may overlap
- Recommend user manually checks against inventory

---

### 1. Understand the Research Scope

Ask clarifying questions to focus the research:

- What niche/industry are we researching? (e.g., "pet travel accessories")
- Any specific angle? (e.g., "cat-specific", "luxury", "budget", "UK market")
- Competitor URLs to analyze? (optional)
- Product focus, content focus, or both?
- Geographic market? (UK, US, EU, etc.)
- Any topics/products to avoid or exclude?

**Example Interaction**:
```
I'm researching: Pet travel accessories
Specific angle: Cat-specific products and content
Focus: Both blog topics and product opportunities
Market: UK primarily, but global insights welcome
Competitors to analyze: [any provided URLs]
```

### 2. Competitor Content Analysis

Search for and analyze top competitors in the niche:

**Actions**:
- Search for "[niche] blog" and "[niche] guide"
- Identify top 5-10 competitor blogs/websites
- Use WebFetch to read their recent content
- Catalog what topics they're covering
- Note what they're NOT covering
- Identify content gaps and weak coverage

**Output Format**:
```markdown
## Competitor Content Landscape

### Top Competitors Analyzed
1. [Competitor Name] - [URL]
   - Main topics: [list]
   - Publishing frequency: [estimate]
   - Content gaps: [observations]

2. [Competitor Name] - [URL]
   - Main topics: [list]
   - Content gaps: [observations]

### Common Topics (Saturated)
- Topic 1 (covered by 8/10 competitors)
- Topic 2 (covered by 7/10 competitors)
- Topic 3 (covered by 6/10 competitors)

### Underserved Topics (Opportunity)
- Topic A (only 1-2 competitors covering)
- Topic B (mentioned briefly, no deep content)
- Topic C (not addressed at all)
```

### 3. Social Listening & Customer Pain Points

Research what real customers are asking about and struggling with:

**Sources to Check**:
- Reddit: r/dogs, r/cats, r/pets, travel subreddits
- Pet forums and communities
- Social media discussions
- Review sites (Amazon, product reviews)
- Q&A sites (Quora, niche forums)

**Search Queries**:
```
"pet travel" site:reddit.com
"cat carrier" problems site:reddit.com
"dog car anxiety" site:reddit.com
"airline pet policy" confusion site:reddit.com
```

**Output Format**:
```markdown
## Customer Pain Points & Discussions

### Frequently Asked Questions (High Volume)
1. "How do I get my cat comfortable in a carrier?"
   - Mentioned in: 15+ Reddit threads, pet forums
   - Current content: Limited practical guides
   - Opportunity: Step-by-step desensitization guide

2. "Best litter box for RV travel?"
   - Mentioned in: 10+ discussions
   - Current solutions: Minimal product options
   - Opportunity: Product review + recommendation content

### Emerging Concerns
- [New trend or concern spotted]
- [Evidence: where discussed, frequency]
- [Current coverage: gap analysis]

### Frustrations & Complaints
- "Can't find X that does Y"
- "Why doesn't anyone make Z?"
- [Product/content gap indicated]
```

### 4. Search Trend Analysis

Research what people are actively searching for:

**Actions**:
- Use WebSearch to find keyword research data
- Look for "[niche] keywords 2026"
- Check Google Trends insights
- Identify seasonal patterns
- Find rising search queries

**Output Format**:
```markdown
## Search Trend Insights

### High-Volume, Low-Competition Keywords
1. "cat travel carrier anxiety"
   - Search volume: Medium-High
   - Competition: Low
   - Opportunity: High-value content

2. "dog car seat legal UK"
   - Search volume: Medium
   - Competition: Low
   - Opportunity: Definitive guide

### Rising Trends (Growing Interest)
- Topic: [trend name]
- Growth: [data/evidence]
- Current coverage: [gap analysis]

### Seasonal Opportunities
- Summer: [topics that spike]
- Winter: [topics that spike]
- Holiday: [topics that spike]
```

### 5. Product Gap Analysis

Identify product opportunities in the market:

**Actions**:
- Search for competitor stores/products
- Analyze Amazon categories
- Check niche marketplaces
- Identify customer requests from step 3
- Cross-reference demand signals

**Output Format**:
```markdown
## Product Opportunity Analysis

### High-Demand Product Gaps

1. **Portable RV Litter Box**
   - Demand signals:
     * 12+ forum discussions asking for this
     * Amazon reviews requesting "travel-sized" options
     * Reddit thread with 50+ upvotes
   - Competition: Only 2 generic options available
   - Opportunity: Specific RV/caravan-focused design
   - Market validation: STRONG

2. **Airline-Compliant Carrier Size Guide**
   - Not a physical product, but content opportunity
   - Could lead to product: Custom sizing tool/calculator
   - Demand: Frequently asked question
   - Competition: Generic guides only

### Product Categories to Explore
- Category 1: [description]
  * Current offerings: [analysis]
  * Gap: [what's missing]
  * Opportunity: [specific product ideas]
```

### 6. Synthesize & Prioritize Opportunities

Combine all research into actionable recommendations:

**Prioritization Criteria**:
- **NOT already in inventory** (Step 0 check - exclude existing products)
- Demand strength (how many signals?)
- Competition level (low = good opportunity)
- Alignment with brand (HappyPawsCo values)
- SEO potential (search volume, keyword difficulty)
- Product feasibility (can it be sourced?)
- Content depth (can we create valuable content?)

**Output Format**:
```markdown
## Priority Opportunities Report

Generated: [Date]
Niche: [Niche researched]
Focus: [Specific angle]

---

### 🔥 TOP 5 BLOG OPPORTUNITIES

#### 1. [Blog Topic Title]
**Priority: HIGH**

- **Gap Identified**: [What's missing in current content]
- **Demand Signals**:
  * [Evidence 1]
  * [Evidence 2]
  * [Evidence 3]
- **Competition**: LOW (only X competitors covering)
- **SEO Potential**: [Keyword data if available]
- **Why This Matters**: [Explanation]
- **Recommended Angle**: [Specific approach]
- **Next Step**: Create with /content-research-writer

#### 2. [Blog Topic Title]
**Priority: HIGH**
[Same format...]

#### 3-5. [Additional topics]
[Same format...]

---

### 🛒 TOP 5 PRODUCT OPPORTUNITIES

#### 1. [Product Name/Category]
**Priority: HIGH**

- **Gap Identified**: [What customers want but can't find]
- **Demand Signals**:
  * [Evidence 1: Reddit discussions]
  * [Evidence 2: Review requests]
  * [Evidence 3: Search volume]
- **Competition Analysis**: [Current market offerings]
- **Market Validation**: STRONG/MEDIUM/WEAK
- **Considerations**: [Sourcing, pricing, differentiation]
- **Content Tie-In**: [Related blog opportunity]
- **Next Step**: Research suppliers/manufacturers

#### 2-5. [Additional products]
[Same format...]

---

### 📊 MARKET INSIGHTS

#### What's Saturated (Avoid)
- Topic 1: [Why it's crowded]
- Topic 2: [Why it's crowded]

#### Emerging Trends (Watch)
- Trend 1: [Description, timeline]
- Trend 2: [Description, timeline]

#### Seasonal Opportunities
- Q2 2026: [Specific opportunities]
- Q3 2026: [Summer travel focus]
- Q4 2026: [Holiday travel]

---

### 🎯 RECOMMENDED ACTION PLAN

**This Month**:
1. Create blog: [Top priority topic]
2. Research product: [Top priority product]
3. Monitor: [Emerging trend]

**Next Quarter**:
1. Content series: [Theme]
2. Product launch: [Category]
3. Expand into: [Opportunity area]

---

### 📝 RESEARCH NOTES

#### Competitors Analyzed
- [Competitor 1]: [URL]
- [Competitor 2]: [URL]
- [List all analyzed]

#### Sources Referenced
- Reddit: [Specific subreddits]
- Forums: [Which ones]
- Trends: [Data sources]
- Products: [Marketplaces checked]

#### Research Limitations
- [Any gaps in research]
- [Areas needing deeper investigation]
- [Assumptions made]
```

## Research Best Practices

### For Competitor Analysis
- Check publish dates (focus on recent 6-12 months)
- Look at engagement (comments, shares if visible)
- Note content depth (surface-level vs comprehensive)
- Identify their blind spots

### For Social Listening
- Focus on genuine problems, not promotional posts
- Look for repeated patterns (not one-off complaints)
- Note the language customers use (for SEO)
- Identify emotional pain points

### For Trend Research
- Verify trends with multiple sources
- Distinguish fads from lasting trends
- Consider seasonal vs evergreen
- Check geographic relevance

### For Product Analysis
- Check Amazon reviews for "wish it had X" comments
- Look for DIY solutions (signals unmet need)
- Analyze price points and positioning
- Consider sourcing feasibility

## Integration with Other Skills

This skill feeds directly into:

### Content Pipeline
```
/niche-gap-researcher
  → Identifies blog topics
  → /content-research-writer [topic]
  → /blog-quality-checker
  → Publish
```

### Product Pipeline
```
/niche-gap-researcher
  → Identifies product opportunities
  → Research suppliers
  → /product-copy-writer
  → List on Shopify
```

### Pinterest Strategy
```
/niche-gap-researcher
  → New content topics
  → /pinterest-pin-creator
  → Drive traffic to new content
```

## Examples

### Example 1: Pet Travel Accessories

**User**: `/niche-gap-researcher`

**Skill Response**:
"I'll help you discover underserved opportunities in your niche. Let me ask a few questions:

1. What niche are we researching?
2. Any specific angle (e.g., cat-specific, luxury, budget)?
3. Focus on blog content, products, or both?
4. Target market (UK, US, global)?
5. Any competitor URLs to analyze?"

**User**: "Pet travel accessories, cat-specific angle, both content and products, UK market"

**Skill Process**:
1. Searches for top pet travel blogs
2. Analyzes their content for cat coverage
3. Checks Reddit r/cats for travel discussions
4. Reviews Amazon UK pet travel products
5. Identifies gaps

**Output**: Detailed opportunity report showing:
- "Airline Carrier Rules by UK Airline" (high demand, low content)
- "Cat Travel Anxiety Solutions for Cars" (heavily discussed, weak content)
- Product: "UK-Compliant Car Restraint for Cats" (requested in reviews, limited options)

### Example 2: Luxury Pet Travel

**User**: "Find gaps in the luxury pet travel market"

**Skill Process**:
1. Analyzes luxury pet brands and boutiques
2. Checks high-end travel forums
3. Reviews premium product offerings
4. Identifies underserved luxury segments

**Output**: Report showing:
- "Private Jet Pet Etiquette" (wealthy pet owners asking, no guides)
- "Luxury Pet-Friendly Hotels in Europe" (scattered info, no comprehensive guide)
- Product: "Designer Car Hammock" (demand for high-end, most are budget)

### Example 3: Seasonal Research

**User**: "What pet travel opportunities exist for summer 2026?"

**Skill Process**:
1. Checks seasonal search trends
2. Analyzes last summer's discussions
3. Identifies emerging summer patterns
4. Predicts upcoming needs

**Output**: Report showing:
- "Keeping Pets Cool in Hot Cars" (summer spike, safety focused)
- "Beach Travel with Dogs UK" (seasonal high demand)
- Product: "Cooling Car Seat Covers" (requested in summer months)

## Pro Tips

1. **Run Quarterly**: Market gaps change, refresh your research every 3 months
2. **Track Competitors**: Note when competitors fill gaps you identified
3. **Validate Before Creating**: Use this research to prioritize, not to create everything
4. **Combine Opportunities**: Look for blog + product combos (cross-promotion)
5. **Document Research**: Save the full reports for future reference
6. **Act Fast**: Gaps don't stay open forever, prioritize and execute
7. **Update CLAUDE.md**: Add new insights to your project knowledge base

## Output File Structure

Save research reports in organized format:

```
00_Knowledge_Base/Market_Research/
├── 2026-Q1-Gap-Analysis.md
├── 2026-Q2-Gap-Analysis.md
├── Competitor_Tracking.md
└── Opportunity_Backlog.md
```

## Common Use Cases

- **Content Planning**: "What should I blog about next month?"
- **Product Expansion**: "What products should I add to my store?"
- **SEO Strategy**: "What keywords are underserved?"
- **Competitive Positioning**: "What are competitors missing?"
- **Trend Spotting**: "What's emerging in my niche?"
- **Validation**: "Is there demand for this idea?"

## Limitations & Considerations

- Research is a snapshot in time (markets change)
- High demand doesn't always mean profitability
- Consider your capacity (don't overcommit)
- Some gaps exist for good reasons (regulatory, complexity)
- Validate findings before major investments
- Use judgment alongside data

## Success Metrics

Track whether opportunities identified lead to:
- Blog traffic increases
- Product sales
- SEO ranking improvements
- Audience engagement
- Revenue growth

Review which predictions were accurate to improve future research.

---

**Remember**: This skill finds opportunities. Execution still requires your other skills (/content-research-writer, /product-copy-writer, etc.) and your strategic judgment. Not every gap is worth filling - choose wisely based on your brand and capacity.
