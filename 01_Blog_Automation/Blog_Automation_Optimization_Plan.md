# Blog Automation Optimization Plan
## Fixing Robotic AI Tone - Creating Warm, Empathetic Pet Owner Voice

---

## **CURRENT ISSUE ANALYSIS**
Your blog sounds robotic because:
- Generic AI structure and language patterns
- Lack of personal anecdotes and experiences
- Clinical, informational tone vs conversational
- Missing emotional connection with pet parent struggles
- No "fellow pet owner" credibility markers

---

## **TARGET VOICE: Warm, Empathetic Smart Friend**

### **Voice Characteristics:**
- **Personal:** "I've been there" moments and shared experiences
- **Empathetic:** Acknowledges pet parent struggles and emotions
- **Knowledgeable:** Well-researched but not preachy
- **Conversational:** Natural flow, contractions, casual language
- **Relatable:** Uses common pet parent scenarios and frustrations

### **Example Transformation:**

**BEFORE (Robotic AI):**
"Dog car safety is essential for protecting your pet during travel. Proper restraints reduce injury risk by 87% according to studies."

**AFTER (Warm Pet Owner Friend):**
"I still remember the first time my Cocker Spaniel went flying across the back seat during a sudden stop - my heart nearly stopped! That's when I learned the hard way that 'they'll be fine' isn't actually a safety strategy."

---

## **MODULE CHANGES REQUIRED**

### **1. ADD: Brand Voice Injection Module**
**New Module Position:** Between Google Sheets and Claude
**Module Type:** Text Preprocessor
**Purpose:** Inject personal context and voice guidelines

```json
{
    "id": "voice_context_injector",
    "module": "util:TextAggregator",
    "mapper": {
        "text": "{{20.`1`}}\n\nPERSONAL CONTEXT:\n- Write as a UK pet owner who's learned through experience\n- Include relatable 'I've been there' moments\n- Use warm, conversational tone like talking to a friend\n- Share common pet parent struggles and solutions\n- Reference your own pets naturally (don't overdo it)\n- Use contractions and natural speech patterns"
    }
}
```

### **2. MODIFY: Claude Blog Writing Module**
**Current Module ID:** 13 (anthropic-claude:createAMessage)
**Changes Required:**

#### **A. Enhanced System Prompt:**
```
You are a warm, empathetic UK pet owner writing for fellow pet parents. You've experienced the same struggles, learned through trial and error, and want to share genuine insights that help other pet families.

VOICE GUIDELINES:
- Write like you're chatting with a friend over coffee about pet challenges
- Include personal anecdotes and "I've been there" moments
- Acknowledge the emotional side of pet parenting
- Use conversational language with contractions (I'm, you're, we'll)
- Reference common pet parent experiences and frustrations
- Balance expertise with humility ("What I've learned...")

CONTENT STRUCTURE:
- Start with relatable scenario or personal experience
- Share practical insights gained through experience
- Include emotional validation for pet parent concerns
- End with encouragement and actionable next steps

AVOID:
- Clinical, academic tone
- Generic advice without personal context
- Overwhelming information dumps
- Preaching or lecturing tone
```

#### **B. Add Personal Context Variables:**
```json
"mapper": {
    "model": "claude-3-5-sonnet-20241022",
    "messages": [
        {
            "role": "system",
            "content": "[Enhanced system prompt above]"
        },
        {
            "role": "user", 
            "content": "Blog Topic: {{voice_context_injector.text}}\n\nWrite a 800-1000 word blog post that sounds like a knowledgeable pet owner friend sharing hard-won insights. Include at least one personal anecdote or relatable experience. Focus on practical help with emotional understanding."
        }
    ],
    "temperature": "0.8",
    "max_tokens": "2500"
}
```

### **3. ADD: Voice Validation Module**
**New Module Position:** After Claude writing, before image generation
**Module Type:** Anthropic Claude validation
**Purpose:** Check for robotic language and suggest improvements

```json
{
    "id": "voice_validator",
    "module": "anthropic-claude:createAMessage",
    "mapper": {
        "model": "claude-3-haiku-20240307",
        "messages": [
            {
                "role": "user",
                "content": "Analyze this blog post for robotic AI language:\n\n{{13.textResponse}}\n\nCheck for:\n1. Personal anecdotes or experiences\n2. Conversational tone with contractions\n3. Emotional validation for pet parents\n4. 'Fellow pet owner' credibility\n5. Natural flow vs clinical structure\n\nReturn JSON: {\"passes_voice_check\": true/false, \"issues\": [\"list of problems\"], \"suggestions\": [\"specific improvements\"]}"
            }
        ],
        "temperature": "0.3"
    }
}
```

### **4. ADD: Conditional Rewrite Module**
**Module Type:** Router/Filter
**Purpose:** Rewrite if voice validation fails

```json
{
    "id": "conditional_rewriter", 
    "module": "builtin:BasicRouter",
    "mapper": {
        "conditions": [
            {
                "label": "Voice Check Failed",
                "condition": "{{voice_validator.textResponse.passes_voice_check}} = false",
                "target": "rewrite_module"
            },
            {
                "label": "Voice Check Passed", 
                "condition": "{{voice_validator.textResponse.passes_voice_check}} = true",
                "target": "continue_to_images"
            }
        ]
    }
}
```

---

## **IMPLEMENTATION PRIORITY**

### **Phase 1: Quick Voice Fix (This Week)**
1. **Modify Claude system prompt** with personal, conversational guidelines
2. **Increase temperature** to 0.8 for more natural variation
3. **Add personal context injection** before blog writing

### **Phase 2: Voice Validation (Next Week)**
4. **Add voice checking module** to catch robotic language
5. **Implement conditional rewrite** for failed voice checks
6. **Test with 3-5 blog topics** to refine prompts

### **Phase 3: Advanced Personalization (Week 3)**
7. **Add pet owner persona details** (breeds owned, experience level)
8. **Create experience database** for consistent anecdotes
9. **Implement emotional tone matching** to blog topics

---

## **SPECIFIC PROMPT IMPROVEMENTS**

### **Current Problem Areas to Address:**

**1. Opening Lines:**
- **Instead of:** "When it comes to dog car safety..."
- **Use:** "The first time I had to slam on the brakes with my dog loose in the car, I knew I'd been kidding myself about safety..."

**2. Advice Delivery:**
- **Instead of:** "Research shows that proper restraints..."
- **Use:** "After trying three different harnesses (and one spectacular failure), here's what I've learned..."

**3. Conclusion Tone:**
- **Instead of:** "Following these guidelines will ensure..."
- **Use:** "Trust me, your future self will thank you when that unexpected pothole doesn't send your furry co-pilot flying..."

---

## **SUCCESS METRICS**

### **Voice Quality Checklist:**
- [ ] Includes at least one personal experience or anecdote
- [ ] Uses contractions naturally (I'm, you're, we'll, don't)
- [ ] Acknowledges emotional aspects of pet parenting
- [ ] Sounds like advice from an experienced friend
- [ ] Avoids clinical or academic language
- [ ] Includes relatable pet parent scenarios
- [ ] Balances expertise with humility

### **Reader Engagement Indicators:**
- Comments saying "This is so relatable!"
- Social shares with personal stories added
- Questions asking for more personal experiences
- Reduced bounce rate on blog posts

---

**Ready to implement Phase 1 changes to the Claude module?**