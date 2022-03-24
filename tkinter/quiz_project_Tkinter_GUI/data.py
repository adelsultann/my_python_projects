


# the questions are taken from https://opentdb.com
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php",params=parameters)

response.raise_for_status()
data = response.json()
# after retrieve the data we got entities html code
question_data = data["results"]

print(question_data)


