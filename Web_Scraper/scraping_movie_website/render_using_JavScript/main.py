from requests_html import HTMLSession
from bs4 import BeautifulSoup

# check out requests_html readme here https://github.com/psf/requests-html

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
session = HTMLSession()
webpage = session.get(URL)

# render html and find by selector
# also increase the default JavaScript timeout from 8sec to 20sec
webpage.html.render(timeout=20)
movies = webpage.html.find(selector="h3")

movies_list = []
for r in movies:
    movies_list.append(r.text)


f1 = open("top_movie.txt", mode="w")

# reverse order using for loop
# (start, end , step)
for n in range(len(movies_list) - 1, -1, -1):
    data = movies_list[n]
    f1.write(f"{data}\n")
f1.close()

