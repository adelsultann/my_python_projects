from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

# here we got all the content in the website
soup = BeautifulSoup(contents, "html.parser")

# we can print any html tag by passing the tag after the soup
# print(soup.ul)
# to get the title without the html tag
# print(soup.title.string)

# to priny yhr info in pretty way
# print(soup.prettify())

# to get all the a tags
# result is a list contain all the tags
all_anchor_tags = soup.find_all(name="a")

# print(all_anchor_tags)

# to get only the text of the a tags
# for tag in all_anchor_tags:
#     print(tag.getText())
#     # to print only the herf
#     print(tag.get("href"))


# search by id

# heading = soup.find(name="h1", id="name")
# print(heading)

# search by class

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.text)

# select like Css
company_url = soup.select_one(selector="p a")
company_by_id = soup.select_one(selector="#name")
# select by class
company_by_class = soup.select_one(selector=".heading")

print(company_url)
print(company_by_id)
print(company_by_class)