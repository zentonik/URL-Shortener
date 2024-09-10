import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

url = input("Enter the URL to shorten: ")
print("Shortened URL:", shorten_url(url))
