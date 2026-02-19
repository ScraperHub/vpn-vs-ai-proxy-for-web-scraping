<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=crawling_api_banner" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2" 
       alt="crawling-api-cta" 
       style="max-width: 100%; border: 0;">
</a>

We invite you to explore our [blog](https://crawlbase.com/blog/difference-between-vpn-and-ai-proxy/?utm_source=github&utm_medium=referral&utm_campaign=scraperhub&ref=gh_scraperhub) for more details.

# Crawlbase Smart AI Proxy Examples

This folder contains Python examples demonstrating how to use [Crawlbase Smart AI Proxy](https://crawlbase.com/docs/smart-proxy/) to scrape websites like Amazon.com with various configurations.

## What is Crawlbase Smart AI Proxy?

The Smart AI Proxy is an intelligent rotating proxy that forwards your requests to the Crawling API with built-in features like:
- Automatic IP rotation
- Anti-blocking mechanisms
- CAPTCHA bypassing
- Browser fingerprint management

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get your Crawlbase access token:**
   - Sign up at [Crawlbase](https://crawlbase.com/)
   - Get your access token from the [dashboard](https://crawlbase.com/dashboard)

3. **Update the script:**
   - Open `crawlbase_ai_proxy_example.py`
   - Replace `YOUR_ACCESS_TOKEN` with your actual token

## Usage

Run the examples:
```bash
# Basic example
python crawlbase_ai_proxy_example.py

# Advanced parameter examples
python crawlbase_with_custom_params.py

# Parameter reference guide
python crawlbase_parameter_reference.py
```

## How It Works

The script makes HTTP requests through the Crawlbase Smart AI Proxy:

- **Proxy Endpoint (HTTPS):** `https://smartproxy.crawlbase.com:8013`
- **Proxy Endpoint (HTTP):** `http://smartproxy.crawlbase.com:8012`
- **Authentication:** Your access token is used as the proxy username

```python
proxies = {
    "http": "https://smartproxy.crawlbase.com:8013",
    "https": "https://smartproxy.crawlbase.com:8013"
}

proxy_auth = HTTPProxyAuth(ACCESS_TOKEN, "")

response = requests.get(
    "https://www.amazon.com/",
    proxies=proxies,
    auth=proxy_auth,
    verify=False  # Required for Smart AI Proxy
)
```

## Features Demonstrated

### 1. Basic Example (`crawlbase_ai_proxy_example.py`)
Simple request through the proxy with automatic IP rotation and anti-blocking.

### 2. Advanced Examples (`crawlbase_with_custom_params.py`)
Demonstrates various Crawling API parameters:

1. **JavaScript Rendering** - `javascript=true` for dynamic content (React, Vue, Angular)
2. **Geo-Targeting** - `country=US` to scrape from specific countries
3. **Device Emulation** - `device=mobile` for mobile-specific content
4. **Headers & Cookies** - `get_headers=true&get_cookies=true` to retrieve response metadata
5. **Combined Parameters** - Chain multiple parameters for advanced use cases

### 3. Parameter Reference Guide (`crawlbase_parameter_reference.py`)
Quick reference guide showing:
- Common parameter combinations
- Use case examples
- Practical Amazon scraping example
- Best practices for production scraping

**Available Parameters:**
- `javascript=true` - Enable JavaScript rendering
- `country=US|UK|DE|...` - Geo-locate requests (195+ countries)
- `device=mobile|desktop` - Emulate device type
- `store=true` - Store results in Crawlbase Cloud Storage
- `get_headers=true` - Retrieve response headers
- `get_cookies=true` - Get cookies from response
- `format=json|html` - Response format
- And many more...

## Important Notes

- SSL verification is disabled (`verify=False`) because the proxy needs to inspect and modify requests
- The proxy automatically handles IP rotation and anti-blocking
- Parameters are passed via the `CrawlbaseAPI-Parameters` header
- Multiple parameters can be combined with `&` (e.g., `javascript=true&country=US`)

## Documentation

- [Smart AI Proxy Documentation](https://crawlbase.com/docs/smart-proxy/)
- [Smart Proxy Parameters](https://crawlbase.com/docs/smart-proxy/parameters/)
- [Crawling API Parameters](https://crawlbase.com/docs/crawling-api/parameters/)
