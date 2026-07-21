import hashlib

url = "https://google.com"
code = hashlib.md5(url.encode()).hexdigest()[:6]
print(code)
