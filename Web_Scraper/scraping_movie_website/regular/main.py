from bs4 import BeautifulSoup
import requests
import xml

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")

all_anchor_tags = soup.find_all(name="h3")

#print(all_anchor_tags)
a = []
for tag in all_anchor_tags:
    a.append(tag.getText())


f1 = open("top_movie.txt", mode="w")
data = a[::-1]
for da in data:

    f1.write(f"{da}\n")
f1.close()
