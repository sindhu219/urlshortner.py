import http.client
import urllib.parse

def shorten_url(url):
    api_url = 'tinyurl.com'
    params = urllib.parse.urlencode({'url': url})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(api_url)
    conn.request("POST", "/api-create.php", params, headers)
    response = conn.getresponse()
    if response.status == 200:
        shortened_url = response.read().decode('utf-8')
        return shortened_url
    else:
        print("Error occurred while shortening URL.")
        return None

# Example usage
long_url = "https://www.example.com/this/is/a/very/long/url"
short_url = shorten_url(long_url)
if short_url:
    print("Original URL:", long_url)
    print("Shortened URL:", short_url)
