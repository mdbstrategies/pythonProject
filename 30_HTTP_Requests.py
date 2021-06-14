import requests
r = requests.get("https://www.myparentslegacy.com")
var = r.status_code

var1 = r.headers

var2 = r.text


print(var)
print(var1)
print(var2)
