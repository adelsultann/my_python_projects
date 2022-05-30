import requests

# r = requests.get("https://xkcd.com/353/")

# if the result is 200 then it is successful connection
# print(r)

# The dir() function returns all properties and methods of the specified object,
# print(dir(r))

# to get the text of the page html
# print(r.text)


# ___________ dealing with img _______________________________

# r = requests.get("https://imgs.xkcd.com/comics/python.png")

# read the picture in bytes

# print(r.content)
# print(r.status_code) # to check if the connection is valid
# to save the picture

# with open("comic.png", "wb") as f:
#     f.write(r.content)

# to get information about the header
# print(r.headers)

# ___________ More

# get post

# payload = {"page":2, "count": 25}

# r = requests.get("http://httpbin.org/get", params=payload)

# to get the full url
# print(r.url)


# request Post to url

# payload = {"username":"adel", "pass": "testing"}

# r = requests.post("http://httpbin.org/post", data=payload)

# r_dic = r.json()

# to get specific value from the dictionary
# print(r_dic["form"])

# HTTP Auth requests


r = requests.get("http://httpbin.org/basic-auth/adel/4466", auth=("adel", "4466"))

print(r.text)
