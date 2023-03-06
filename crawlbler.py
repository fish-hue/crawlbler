import requests
from bs4 import BeautifulSoup

# Prompt the user to enter the URL to crawl
url = input("Enter the URL to crawl: ")

# Send a GET request to the URL and store the response
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find all script tags in the HTML and extract the src attribute (if it exists)
scripts = soup.find_all('script')
for script in scripts:
    if script.has_attr('src'):
        print("Script found:", script['src'])

# Find the meta generator tag in the HTML and extract the content attribute
generator = soup.find('meta', {'name': 'generator'})
if generator:
    print("Generator found:", generator['content'])

# Check the server header of the response to find the web server and version
server_header = response.headers.get('Server')
if server_header:
    print("Server header found:", server_header)

# Check the X-Powered-By header of the response to find the server-side language and version
x_powered_by_header = response.headers.get('X-Powered-By')
if x_powered_by_header:
    print("X-Powered-By header found:", x_powered_by_header)

# Check for cookies that were set by the website
cookies = response.cookies
if cookies:
    print("Cookies found:", cookies)

# Find all forms on the page and extract information about each one
forms = soup.find_all('form')
for form in forms:
    print("Form found:")
    print("Action URL:", form.get('action'))
    print("Method:", form.get('method'))

    # Find all form fields in the form and extract information about each one
    fields = form.find_all('input')
    for field in fields:
        print("Field name:", field.get('name'))
        print("Field type:", field.get('type'))
        print("Field value:", field.get('value'))

# Check for links to social media accounts
social_media_urls = ['facebook.com', 'twitter.com', 'instagram.com']
links = soup.find_all('a')
for link in links:
    for url in social_media_urls:
        if url in link.get('href'):
            print("Social media link found:", link.get('href'))
