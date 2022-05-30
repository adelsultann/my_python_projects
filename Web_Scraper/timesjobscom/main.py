import time

from bs4 import BeautifulSoup
import requests

# user inout _____________________________________________
print("Put some skill that your not familiar with")
unfamiliar_skill = input(">")
print(f"filtering out {unfamiliar_skill}")


# _____________________________________________


def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    r = requests.get(url)
    header = headers = {"User-Agent": "Defined"}

    page = requests.get(url, headers=header)

    soup = BeautifulSoup(page.content, "html5lib")
    # job = soup.find("li", class_="clearfix job-bx wht-shd-bx")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    # enumerate to loop with the index number
    for index,job in enumerate(jobs):
        # inside the span is another span so we add it at the end

        published_data = job.find("span", class_="sim-posted").span.text
        # print(published_data)

        if "few" in published_data:
            # job.find get access to the job variable and find something inside it
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")

            # print(company_name)
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]

            if unfamiliar_skill not in skills:
                # with open(f"Post/{index}.txt","w") as f:
                #     f.write(f"Company Name: {company_name.strip()}\n")
                #     f.write(f"Required skills {skills.strip()}\n")
                #     f.write(f"More Info: {more_info}")
                #     print("")
                # print(f"file saved: {index}")

                print(f"Company Name: {company_name.strip()}")
                print(f"Required skills {skills.strip()}")
                print(f"More Info: {more_info}")
                print("")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Wating for {time_wait} minutes")
        time.sleep(time_wait * 60)
