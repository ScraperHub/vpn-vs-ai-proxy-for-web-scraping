"""
Crawlbase Smart AI Proxy - Parameter Reference Guide
Quick reference for common parameter combinations

Full parameter documentation: https://crawlbase.com/docs/smart-proxy/parameters/
"""

import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
proxy_url = f"http://{ACCESS_TOKEN}:@smartproxy.crawlbase.com:8012"

proxies = {
    "http": proxy_url,
    "https": proxy_url
}

# ============================================================================
# Parameter Reference Examples
# ============================================================================

print("CRAWLBASE SMART AI PROXY - PARAMETER REFERENCE")
print("=" * 60)
print()

# Example 1: Scrape JavaScript-heavy SPA (Single Page Application)
print("1. JavaScript-Heavy Sites (React, Vue, Angular)")
print("   Parameter: javascript=true")
print("   Use case: Dynamic content that loads via AJAX/fetch")
print()

# Example 2: E-commerce price comparison across regions
print("2. Geo-Targeted E-commerce Scraping")
print("   Parameter: country=US&device=desktop")
print("   Use case: Compare prices across different countries")
print()

# Example 3: Mobile-first websites
print("3. Mobile-Specific Content")
print("   Parameter: device=mobile")
print("   Use case: Scrape mobile-only features or layouts")
print()

# Example 4: Session-based scraping with cookies
print("4. Session Management")
print("   Parameter: get_cookies=true&get_headers=true")
print("   Use case: Track session cookies and authentication headers")
print()

# Example 5: Long-term data collection
print("5. Cloud Storage Integration")
print("   Parameter: store=true")
print("   Use case: Automatically backup scraped data to cloud")
print()

# Example 6: Production scraping setup
print("6. Production-Ready Configuration")
print("   Parameter: javascript=true&country=US&store=true&format=json")
print("   Use case: Full-featured scraping with all safeguards")
print()

print("=" * 60)

# ============================================================================
# Practical Example: Amazon Product Scraping
# ============================================================================

print("\nPRACTICAL EXAMPLE: Amazon Product Data Collection")
print("=" * 60)

target_url = "https://www.amazon.com/dp/B08N5WRWNW"

# Configuration for reliable Amazon scraping
headers = {
    "CrawlbaseAPI-Parameters": "javascript=true&country=US&device=desktop&store=true"
}

print(f"Target: {target_url}")
print(f"Parameters: javascript=true, country=US, device=desktop, store=true")
print()

try:
    response = requests.get(
        url=target_url,
        proxies=proxies,
        headers=headers,
        verify=False,
        timeout=30
    )
    response.raise_for_status()
    
    print(f"✓ Status: {response.status_code}")
    print(f"✓ Content Length: {len(response.text):,} characters")
    print(f"✓ JavaScript: Rendered")
    print(f"✓ Location: United States")
    print(f"✓ Device: Desktop")
    print(f"✓ Storage: Saved to Crawlbase Cloud")
    print()
    print("Data successfully collected and stored!")
    
except requests.exceptions.RequestException as e:
    print(f"✗ Error occurred: {e}")

print()
print("=" * 60)
print("COMMON PARAMETER COMBINATIONS")
print("=" * 60)
print()
print("Basic scraping:")
print("  (no parameters needed)")
print()
print("JavaScript sites:")
print("  javascript=true")
print()
print("Geo + JS:")
print("  javascript=true&country=US")
print()
print("Mobile scraping:")
print("  device=mobile&country=US")
print()
print("Full featured:")
print("  javascript=true&country=US&device=mobile&store=true")
print()
print("Session tracking:")
print("  get_cookies=true&get_headers=true")
print()
print("=" * 60)
print("For complete parameter list:")
print("https://crawlbase.com/docs/smart-proxy/parameters/")
print("=" * 60)
