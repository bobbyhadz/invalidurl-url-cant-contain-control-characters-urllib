# Python InvalidURL: URL can't contain control characters

import urllib.request


url = 'http://www.pyt hon.org/'

url = url.replace(' ', '')

with urllib.request.urlopen(url) as f:
    print(f.read(300))