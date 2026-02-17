"""
Crawlbase Smart AI Proxy - Advanced Examples with Custom Parameters
Demonstrates various Crawling API parameters for different use cases
Full documentation: https://crawlbase.com/docs/smart-proxy/parameters/
"""

import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# ============================================================================
# Configuration
# ============================================================================

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
target_url = "https://www.amazon.com/"

# ============================================================================
# Setup Proxy Configuration
# ============================================================================

# Smart AI Proxy URL with token embedded
proxy_url = f"http://{ACCESS_TOKEN}:@smartproxy.crawlbase.com:8012"

proxies = {
    "http": proxy_url,
    "https": proxy_url
}

# ============================================================================
# Example 1: JavaScript Rendering
# ============================================================================

print("Example 1: JavaScript rendering for dynamic content")
print("-" * 60)

headers = {
    "CrawlbaseAPI-Parameters": "javascript=true"
}

try:
    response = requests.get(
        url=target_url,
        proxies=proxies,
        headers=headers,
        verify=False,
        timeout=30
    )
    response.raise_for_status()
    
    print(f"✓ Success! Response length: {len(response.text)} characters")
except requests.exceptions.RequestException as e:
    print(f"✗ Error: {e}")

print()

# ============================================================================
# Example 2: Geo-Targeted Scraping
# ============================================================================

print("Example 2: Geo-targeted request from specific country")
print("-" * 60)

headers = {
    "CrawlbaseAPI-Parameters": "country=US"
}

try:
    response = requests.get(
        url="https://www.amazon.com/",
        proxies=proxies,
        headers=headers,
        verify=False,
        timeout=30
    )
    response.raise_for_status()
    
    print(f"✓ Success! Scraped from US location")
except requests.exceptions.RequestException as e:
    print(f"✗ Error: {e}")

print()

# ============================================================================
# Example 3: Mobile Device Emulation
# ============================================================================

print("Example 3: Mobile device emulation")
print("-" * 60)

headers = {
    "CrawlbaseAPI-Parameters": "device=mobile"
}

try:
    response = requests.get(
        url=target_url,
        proxies=proxies,
        headers=headers,
        verify=False,
        timeout=30
    )
    response.raise_for_status()
    
    print(f"✓ Success! Mobile version scraped")
except requests.exceptions.RequestException as e:
    print(f"✗ Error: {e}")

print()

# ============================================================================
# Example 4: Get Headers and Cookies
# ============================================================================

print("Example 4: Retrieve response headers and cookies")
print("-" * 60)

headers = {
    "CrawlbaseAPI-Parameters": "get_headers=true&get_cookies=true"
}

try:
    response = requests.get(
        url=target_url,
        proxies=proxies,
        headers=headers,
        verify=False,
        timeout=30
    )
    response.raise_for_status()
    
    print(f"✓ Success! Headers retrieved: {len(response.headers)} headers")
except requests.exceptions.RequestException as e:
    print(f"✗ Error: {e}")

print()

# ============================================================================
# Example 5: Combined Parameters
# ============================================================================

print("Example 5: Multiple parameters combined")
print("-" * 60)

# Combine multiple parameters for advanced scraping
headers = {
    "CrawlbaseAPI-Parameters": "javascript=true&country=US&device=mobile&store=true"
}

try:
    response = requests.get(
        url=target_url,
        proxies=proxies,
        headers=headers,
        verify=False,
        timeout=30
    )
    response.raise_for_status()
    
    print(f"✓ Success! JS rendering + US geo + Mobile + Cloud storage")
    print(f"✓ Response length: {len(response.text)} characters")
except requests.exceptions.RequestException as e:
    print(f"✗ Error: {e}")

print()
print("=" * 60)
print("All examples completed!")
print("For more parameters, visit:")
print("https://crawlbase.com/docs/smart-proxy/parameters/")
print("=" * 60)
