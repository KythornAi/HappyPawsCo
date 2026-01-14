# Review Request Email Templates
**Purpose:** Post-purchase email sequence to collect authentic customer reviews
**Created:** December 30, 2024
**Status:** Ready to implement in email platform

---

## Why Review Requests Matter

**Benefits:**
- Builds social proof for future customers
- Increases conversion rates (products with reviews convert 270% higher)
- Improves SEO (fresh user-generated content)
- Provides valuable product feedback
- Builds customer relationships

**Best Practices:**
- Send at the right time (after they've had time to use the product)
- Keep it short and easy
- Don't beg or sound desperate
- Offer a simple, one-click review option
- Follow up once if no response (then stop)

---

## Email Sequence Overview

**3-Email Sequence:**

1. **Email 1: Order Confirmation & What to Expect** (sent immediately after purchase)
   - Sets the stage for future communication
   - Doesn't ask for a review yet

2. **Email 2: Review Request** (sent 14 days after delivery)
   - Primary review request
   - Simple, friendly, one-click option

3. **Email 3: Gentle Reminder** (sent 7 days after Email 2, only if no review left)
   - Softer follow-up
   - Last attempt, then stop

---

## Email 1: Order Confirmation & What to Expect

**Subject Line:**
```
Your HappyPawsCo order is on the way 🐾
```

**Alternative Subject Lines:**
```
Order confirmed: [Product Name] is heading your way
Thanks for your order - here's what happens next
```

**Email Body:**

```
Hi [First Name],

Thanks for your order! Your [Product Name] is on the way and should arrive within 3-5 working days.

**What happens next:**

✅ Your order has been confirmed
📦 We'll pack it today and hand it to our courier
🚚 You'll get a tracking link as soon as it's dispatched
📧 In a couple of weeks, we'll check in to see how you're getting on

**What's in your order:**

- [Product Name] (x[Quantity])
- [Product Name] (x[Quantity])

**Order number:** #[Order Number]
**Delivery address:** [Address]

If you need to change anything, just reply to this email and we'll sort it.

Thanks for supporting HappyPawsCo. We're a small UK team working to make life with dogs a little bit easier, and we're really glad you're here.

— The HappyPawsCo Team

P.S. If you have any questions while you're waiting, drop us a line at hello@happypawsco.co.uk
```

**Implementation Notes:**
- Use your Shopify automated order confirmation email
- Customize the default template with this copy
- Include order details (product names, quantities, tracking)
- Personalize with customer's first name

---

## Email 2: Review Request (Primary)

**Timing:** 14 days after delivery

**Subject Line:**
```
Quick question about your [Product Name]
```

**Alternative Subject Lines:**
```
How's the [Product Name] working out?
Mind if we ask how [Dog's Name] is getting on? (if you collect dog names at checkout)
Two weeks in - how's it going?
```

**Email Body:**

```
Hi [First Name],

It's been a couple of weeks since your [Product Name] arrived, so you've probably had a chance to try it out by now.

If you've got 30 seconds, we'd really appreciate it if you could leave a quick review. It helps other dog owners figure out if it's right for them, and it helps us keep improving what we do.

👉 **[Leave a Review Button]**

No essay required - just a few words about what worked (or didn't) is perfect.

Thanks for your time, and thanks for supporting a small UK pet business.

— The HappyPawsCo Team

P.S. If something's not working or doesn't fit, let us know. We've got a 30-day returns policy, and we're always happy to help.
```

**Button Text:**
```
Leave a Review
```

**Button Link:**
- Direct link to the product review page on your site
- Or use a review app like Judge.me, Loox, or Stamped.io that generates a direct review link

**Implementation Notes:**
- Send 14 days after delivery (not dispatch)
- Use Shopify email apps like Klaviyo, Omnisend, or Judge.me
- Personalize with product name
- Include a clear, clickable button (not just a text link)

---

## Email 3: Gentle Reminder (Follow-Up)

**Timing:** 7 days after Email 2 (21 days post-delivery), only if no review left

**Subject Line:**
```
We're still hoping to hear from you
```

**Alternative Subject Lines:**
```
Last chance to share your thoughts
One more try - could you spare 30 seconds?
Mind leaving a quick review?
```

**Email Body:**

```
Hi [First Name],

We sent an email last week asking if you'd mind leaving a review for your [Product Name]. We know life gets busy, so no stress if you haven't got around to it yet.

But if you've got half a minute today, we'd genuinely appreciate it. Your feedback helps other dog owners make the right choice, and it helps us figure out what's working (and what's not).

👉 **[Leave a Review Button]**

That's the last you'll hear from us about this - we promise we're not going to pester you every week!

Thanks for being a HappyPawsCo customer.

— The HappyPawsCo Team

P.S. If you had any issues with your order, we'd love to know. Drop us a line at hello@happypawsco.co.uk and we'll make it right.
```

**Button Text:**
```
Leave a Review
```

**Implementation Notes:**
- Only send if customer has NOT left a review after Email 2
- Use conditional logic in your email platform (e.g., Klaviyo, Omnisend)
- Stop after this email - don't send more reminders

---

## Optional: Photo Review Incentive Email

**Use this if you want to encourage customers to leave photo reviews**

**Timing:** Same as Email 2 (14 days after delivery)

**Subject Line:**
```
Show us [Dog's Name] in action? (And get 15% off your next order)
```

**Email Body:**

```
Hi [First Name],

It's been a couple of weeks since your [Product Name] arrived. We'd love to know how it's working out - and even better, we'd love to see [Dog's Name] using it!

If you leave a review with a photo, we'll send you a 15% discount code for your next order as a thank-you.

👉 **[Leave a Photo Review Button]**

Just snap a quick pic of your dog using the [Product Name], write a sentence or two about how it's going, and you're done. We'll email your discount code within 24 hours.

Thanks for being part of the HappyPawsCo community.

— The HappyPawsCo Team

P.S. Not happy with your order? Let us know and we'll sort it out - 30-day returns, no questions asked.
```

**Button Text:**
```
Leave a Photo Review & Get 15% Off
```

**Implementation Notes:**
- Only use this if you're offering an incentive
- Make sure it's clear: photo review = discount code
- Use a review platform that supports photo reviews (Judge.me, Loox, Stamped.io)
- Automate discount code delivery via your review app

---

## Plain-Text Alternative (For Better Deliverability)

Some email platforms perform better with plain-text emails. Here's a plain-text version of Email 2:

**Subject:** Quick question about your [Product Name]

**Body:**

```
Hi [First Name],

It's been a couple of weeks since your [Product Name] arrived, so you've probably had a chance to try it out by now.

If you've got 30 seconds, we'd really appreciate it if you could leave a quick review:

[Insert Review Link Here]

It helps other dog owners figure out if it's right for them, and it helps us keep improving what we do.

Thanks for your time, and thanks for supporting a small UK pet business.

— The HappyPawsCo Team

P.S. If something's not working or doesn't fit, let us know. We've got a 30-day returns policy, and we're always happy to help.
```

---

## Review Request on Product Packaging Insert

**Alternative/Supplement to Email: Physical Insert in Package**

If you want to include a physical card in the package asking for reviews, here's the copy:

---

### Insert Card (Front)

```
Thanks for your order!

We're a small UK team, and your support means the world.

If you've got 30 seconds, we'd love to know how this product worked out for you and [Dog's Name].
```

### Insert Card (Back)

```
Leave a review:
👉 happypawsco.co.uk/review

Or scan this QR code:
[QR Code linking to review page]

— The HappyPawsCo Team

P.S. Not happy? Email us at hello@happypawsco.co.uk and we'll make it right.
```

---

**Card Size:** Business card size (85mm x 55mm) or postcard size (A6: 148mm x 105mm)

**Printing:** Moo.com, Vistaprint, or local print shop

---

## Automation Setup (Shopify)

**Recommended Tools:**

1. **Judge.me** (Review app + automated emails)
   - Free plan available
   - Automated review requests
   - Photo reviews supported
   - Integrates with Shopify

2. **Klaviyo** (Email marketing platform)
   - Post-purchase flows
   - Conditional logic (only send if no review left)
   - Advanced personalization
   - 14-day timing from delivery date

3. **Loox** (Photo review app)
   - Visual reviews with photos
   - Automated review requests
   - Discount incentives for photo reviews

4. **Omnisend** (Email marketing platform)
   - Shopify integration
   - Automated workflows
   - Post-purchase sequences

---

## How to Set Up Automated Review Requests in Shopify

**Step-by-Step (Using Judge.me - Free Option):**

1. **Install Judge.me app from Shopify App Store**
   - Search "Judge.me Product Reviews"
   - Click "Add app"

2. **Enable Automated Review Requests**
   - Go to Judge.me dashboard
   - Settings → Email Settings
   - Turn on "Automated Review Request Emails"

3. **Set Timing**
   - Set delay: 14 days after order fulfillment
   - Enable reminder email: 7 days after first email

4. **Customize Email Template**
   - Go to Email Templates
   - Select "Review Request Email"
   - Paste the copy from Email 2 above
   - Customize with your branding

5. **Add Follow-Up Reminder**
   - Go to Reminder Email template
   - Paste the copy from Email 3 above
   - Set to only send if no review left

6. **Test the Flow**
   - Place a test order
   - Mark it as fulfilled
   - Check that emails send at the right time

---

**Step-by-Step (Using Klaviyo - Advanced Option):**

1. **Install Klaviyo from Shopify App Store**

2. **Create a Post-Purchase Flow**
   - Flows → Create Flow → "Post-Purchase"

3. **Set Trigger**
   - Trigger: "Fulfilled Order"

4. **Add Time Delay**
   - Add delay: 14 days after fulfillment

5. **Add Email 2 (Review Request)**
   - Add email action
   - Paste copy from Email 2
   - Design email with button linking to review page

6. **Add Conditional Split**
   - Add conditional split: "Has left review? Yes/No"
   - If yes: End flow
   - If no: Continue

7. **Add Time Delay**
   - Add delay: 7 days

8. **Add Email 3 (Reminder)**
   - Add email action
   - Paste copy from Email 3

9. **End Flow**

10. **Activate Flow**

---

## Email Design Tips

**Keep It Simple:**
- Single-column layout
- Clear call-to-action button (big, obvious)
- Minimal images (loads faster, better deliverability)
- Mobile-friendly (60%+ of people check email on phones)

**Personalization:**
- Use customer's first name
- Reference specific product they bought
- Include their dog's name if you collect it at checkout

**Branding:**
- Use your brand colors
- Include logo at the top
- Keep tone consistent with your brand voice (friendly, warm, helpful)

**Deliverability:**
- Avoid spam trigger words ("free," "click here," "limited time")
- Include physical address in footer (legal requirement)
- Add unsubscribe link (legal requirement)
- Use plain-text version for better inbox placement

---

## Timing Strategy

**Why 14 Days After Delivery?**

- Gives customer time to actually use the product
- Not too soon (they haven't tried it yet)
- Not too late (they've forgotten about it)

**Product-Specific Timing Adjustments:**

```
**Fast-Use Products (Poo Bags, Pet Wipes, Lick Mats):**
- Send review request 7-10 days after delivery
- They'll have used it by then

**Slow-Use Products (Car Harnesses, Travel Bowls, Carriers):**
- Send review request 21-30 days after delivery
- They might not use these daily, so give extra time

**Training Products (No-Pull Harnesses, Two-Point Leads):**
- Send review request 21 days after delivery
- Training takes time to see results
```

---

## What to Do with Negative Reviews

**If you get a negative review:**

1. **Respond Quickly (Within 24 Hours)**
   - Thank them for the feedback
   - Apologize for the issue
   - Offer a solution (refund, replacement, discount)

2. **Example Response:**

```
Hi [Name],

Thanks so much for taking the time to leave a review - even though it wasn't the experience we hoped you'd have.

I'm really sorry the [Product Name] didn't work out for [Dog's Name]. That's frustrating, and we'd love to make it right.

Would you like a full refund, or would you be open to trying a different size/product? We've got a 30-day returns policy, no questions asked.

Drop us a line at hello@happypawsco.co.uk and we'll sort it out today.

Thanks again for the honest feedback.

— [Your Name], HappyPawsCo Team
```

3. **Learn from It**
   - Track common complaints
   - Adjust product descriptions or photos if sizing/expectations are off
   - Improve products based on patterns

---

## Review Metrics to Track

**Key Metrics:**

- **Review Request Open Rate:** Aim for 20-30%
- **Review Request Click Rate:** Aim for 5-10%
- **Review Conversion Rate:** Aim for 3-5% (3-5% of customers leave a review)
- **Average Star Rating:** Aim for 4.5+ stars
- **Photo Review Rate:** Aim for 20-30% of reviews include photos (if incentivized)

**How to Improve:**

- Test different subject lines
- Test different timing (7 days vs. 14 days)
- Offer incentive for photo reviews (discount code)
- Make it easier (one-click review link)
- Follow up once (but only once)

---

## Legal & Compliance

**Important:**

- ✅ Never incentivize positive reviews (against most platform policies)
- ✅ You CAN incentivize reviews in general (e.g., "Leave a review, get 10% off")
- ✅ You CANNOT incentivize 5-star reviews specifically
- ✅ Include unsubscribe link in all emails (legal requirement under GDPR)
- ✅ Include your business address in email footer (legal requirement)
- ✅ Don't delete negative reviews (unless they violate platform policies)

---

## Quick Start Checklist

**To implement review request emails:**

- [ ] Choose a review platform (Judge.me, Loox, Stamped.io, or Klaviyo)
- [ ] Install the app in Shopify
- [ ] Set up automated review request emails (Email 2 - 14 days post-delivery)
- [ ] Set up reminder email (Email 3 - 7 days after Email 2, only if no review)
- [ ] Customize email templates with the copy above
- [ ] Add your branding (logo, colors, tone)
- [ ] Test the flow with a test order
- [ ] Turn on automation
- [ ] Monitor open rates, click rates, and review conversion rates
- [ ] Respond to reviews (especially negative ones) within 24 hours

**Optional:**
- [ ] Create packaging insert card with review request + QR code
- [ ] Offer photo review incentive (15% off next order)
- [ ] Set up product-specific timing (7 days for poo bags, 21 days for harnesses)

---

## Expected Results

**After 30 Days:**
- 3-5% of customers leave a review (industry average)
- 20-30% of reviews include photos (if incentivized)
- Improved conversion rates on products with reviews

**After 90 Days:**
- 10-20 reviews per product (depending on sales volume)
- Social proof established
- Trust signals in place for new visitors

**After 6 Months:**
- 50+ reviews across top products
- Conversion rate increase of 10-25% (compared to no reviews)
- Improved SEO from user-generated content

---

**Status:** Ready to implement
**Time to set up:** 1-2 hours (depending on platform choice)

---

**Last Updated:** December 30, 2024
