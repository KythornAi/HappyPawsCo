#!/usr/bin/env python3
"""
Product Copy Improvement Script
Processes Shopify product CSV and improves copy using HappyPawsCo brand voice
"""

import csv
import re
import json
from pathlib import Path

# Preservation rules
PRESERVE_PATTERNS = [
    r'<p><strong>Reassurance:.*?</p>',
    r'<p><strong>Safety note:.*?</p>',
    r'<p><strong>Note:.*?</p>',
    r'<p><strong>Hygiene notice:.*?</p>',
    r'<p><strong>Pairs well with:.*?</p>',
    r'<p>Prefer.*?</p>',
    r'<p><strong>Need a different size\?.*?</p>',
    r'<p>Also available in.*?</p>',
]

# Social proof variations (conversational)
SOCIAL_PROOF_VARIATIONS = [
    "Speaking with other dog owners at the park, this keeps coming up",
    "Friends with dogs mention this one a lot",
    "I've read so many reviews where people say",
    "Other pet owners I've chatted with say this helps with",
    "Family members using this have found",
    "Reviews talk about how this solved",
]

def extract_preserved_elements(html_body):
    """Extract elements that must be preserved exactly"""
    preserved = {}

    for i, pattern in enumerate(PRESERVE_PATTERNS):
        matches = re.findall(pattern, html_body, re.DOTALL | re.IGNORECASE)
        if matches:
            preserved[f'preserve_{i}'] = matches

    return preserved

def identify_product_type(title, body):
    """Identify product type to apply correct persona/framing"""
    title_lower = title.lower()
    body_lower = body.lower()

    if 'crash-tested' in body_lower or 'car harness' in title_lower:
        return 'crash_tested_harness'
    elif 'harness' in title_lower and 'reflective' in body_lower:
        return 'reflective_harness'
    elif 'booster seat' in title_lower:
        return 'booster_seat'
    elif 'lick mat' in title_lower or 'slow feeder' in title_lower:
        return 'small_item_can_claim_use'
    elif 'carrier' in title_lower and 'hard shell' in body_lower:
        return 'carrier_can_claim_use'
    else:
        return 'general'

def improve_opening_paragraph(product_type, current_opening):
    """Generate improved opening based on product type"""
    # This is a simplified version - full implementation would use
    # the approved patterns from FINAL_PRODUCT_COPY_EXAMPLES.md

    # For now, return placeholder showing the approach
    return f"<!-- IMPROVED OPENING FOR {product_type} -->\n{current_opening}"

def process_product_row(row):
    """Process a single product row"""
    body_html = row['Body (HTML)']
    title = row['Title']

    if not body_html or body_html.strip() == '':
        return row  # Skip empty products

    # Extract preserved elements
    preserved = extract_preserved_elements(body_html)

    # Identify product type
    product_type = identify_product_type(title, body_html)

    # Store original for logging
    original_body = body_html

    # Improve copy (placeholder - full implementation needed)
    # improved_body = improve_copy(body_html, product_type, preserved)

    # For now, just flag products for manual review
    row['_needs_copy_improvement'] = 'yes'
    row['_product_type'] = product_type
    row['_preserved_elements_count'] = len(preserved)

    return row

def main():
    """Main processing function"""
    csv_path = Path('/Volumes/Home Ext/Home Ext/Desktop/Claude/07_Shopify_Store_Improvements/products_export_1.csv')
    output_path = csv_path.parent / 'products_export_improved.csv'
    log_path = csv_path.parent / 'product_processing_log.json'

    print(f"Reading products from: {csv_path}")

    products_processed = []
    processing_log = {
        'total_products': 0,
        'products_with_body': 0,
        'product_types': {},
        'preserved_elements_found': 0,
    }

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['_needs_copy_improvement', '_product_type', '_preserved_elements_count']

        for row in reader:
            processing_log['total_products'] += 1

            if row['Body (HTML)'] and row['Body (HTML)'].strip():
                processing_log['products_with_body'] += 1
                processed_row = process_product_row(row)

                product_type = processed_row.get('_product_type', 'unknown')
                processing_log['product_types'][product_type] = processing_log['product_types'].get(product_type, 0) + 1

                preserved_count = int(processed_row.get('_preserved_elements_count', 0))
                processing_log['preserved_elements_found'] += preserved_count

                products_processed.append(processed_row)
            else:
                products_processed.append(row)

    # Write output CSV
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products_processed)

    # Write log
    with open(log_path, 'w') as f:
        json.dump(processing_log, f, indent=2)

    print(f"\\nProcessing complete:")
    print(f"  Total products: {processing_log['total_products']}")
    print(f"  Products with body content: {processing_log['products_with_body']}")
    print(f"  Preserved elements found: {processing_log['preserved_elements_found']}")
    print(f"\\nProduct types:")
    for ptype, count in processing_log['product_types'].items():
        print(f"  {ptype}: {count}")
    print(f"\\nOutput written to: {output_path}")
    print(f"Log written to: {log_path}")

if __name__ == '__main__':
    main()
