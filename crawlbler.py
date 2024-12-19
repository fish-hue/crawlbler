import requests
from bs4 import BeautifulSoup
import validators

def validate_url(url):
    """Validate the given URL."""
    if not validators.url(url):
        raise ValueError("Invalid URL. Please enter a valid URL.")

def extract_scripts(soup):
    """Extract and print script sources."""
    scripts = soup.find_all('script')
    for script in scripts:
        if script.has_attr('src'):
            print("Script found:", script['src'])

def extract_forms(soup):
    """Extract and print form details."""
    forms = soup.find_all('form')
    for form in forms:
        print("Form found:")
        print("Action URL:", form.get('action', 'N/A'))
        print("Method:", form.get('method', 'N/A'))
        fields = form.find_all('input')
        for field in fields:
            print("Field name:", field.get('name', 'N/A'))
            print("Field type:", field.get('type', 'N/A'))
            print("Field value:", field.get('value', 'N/A'))

def extract_metadata(soup):
    """Extract and print metadata details."""
    generator = soup.find('meta', {'name': 'generator'})
    if generator:
        print("Generator found:", generator.get('content', 'N/A'))

def extract_headers(response):
    """Extract and print HTTP headers."""
    server_header = response.headers.get('Server')
    if server_header:
        print("Server header found:", server_header)
    x_powered_by = response.headers.get('X-Powered-By')
    if x_powered_by:
        print("X-Powered-By header found:", x_powered_by)

def extract_cookies(response):
    """Extract and print cookies."""
    cookies = response.cookies
    if cookies:
        print("Cookies found:")
        for cookie in cookies:
            print(f"  {cookie.name} = {cookie.value}")

def extract_social_links(soup, social_media_urls):
    """Extract and print social media links."""
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            for url in social_media_urls:
                if url in href:
                    print("Social media link found:", href)

# Main script
if __name__ == "__main__":
    url = input("Enter the URL to crawl: ")
    try:
        validate_url(url)
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information
        print("\n--- Scripts ---")
        extract_scripts(soup)

        print("\n--- Forms ---")
        extract_forms(soup)

        print("\n--- Metadata ---")
        extract_metadata(soup)

        print("\n--- HTTP Headers ---")
        extract_headers(response)

        print("\n--- Cookies ---")
        extract_cookies(response)

        print("\n--- Social Media Links ---")
        social_media_urls = ['facebook.com', 'twitter.com', 'instagram.com']
        extract_social_links(soup, social_media_urls)

    except Exception as e:
        print(f"An error occurred: {e}")
