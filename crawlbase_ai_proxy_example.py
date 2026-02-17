"""
Crawlbase Smart AI Proxy Example
Simple script to scrape Amazon.com using Crawlbase Smart AI Proxy
"""

import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings (since we're using verify=False)
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# ============================================================================
# Configuration
# ============================================================================

# Your Crawlbase access token (replace with your actual token)
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Target URL to scrape
target_url = "https://www.amazon.com/"

# ============================================================================
# Setup Proxy Configuration
# ============================================================================

# Smart AI Proxy URL with token embedded
# Format: http://TOKEN:@host:port or https://TOKEN:@host:port
proxy_url = f"http://{ACCESS_TOKEN}:@smartproxy.crawlbase.com:8012"
# HTTPS alternative: f"https://{ACCESS_TOKEN}:@smartproxy.crawlbase.com:8013"

# Configure proxy settings for both HTTP and HTTPS requests
proxies = {
    "http": proxy_url,
    "https": proxy_url
}

# ============================================================================
# Make the Request
# ============================================================================

print("=" * 60)
print("Crawlbase Smart AI Proxy - Amazon.com Scraping Example")
print("=" * 60)
print()

print(f"Sending request to {target_url} via Crawlbase Smart AI Proxy...")

try:
    # Make the request through the proxy
    # verify=False disables SSL verification (required for Smart AI Proxy)
    response = requests.get(
        url=target_url,
        proxies=proxies,
        verify=False,
        timeout=30
    )
    response.raise_for_status()  # Raise an exception for bad status codes
    
    # Display results
    print(f"✓ Success! Status code: {response.status_code}")
    print(f"✓ Response length: {len(response.text)} characters")
    print(f"✓ Content preview:\n{response.text[:500]}...")
        
except requests.exceptions.RequestException as e:
    print(f"✗ Error occurred: {e}")

print("\n" + "=" * 60)
print("Note: Replace 'YOUR_ACCESS_TOKEN' with your actual token")
print("Get your token at: https://crawlbase.com/dashboard")
print("=" * 60)
