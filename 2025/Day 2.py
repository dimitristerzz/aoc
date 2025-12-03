import requests

SESSION_COOKIE = "53616c7465645f5f5d4b262b6473136e17634719c6129df046cd548d781b5b4523d9326759da7574a67d8dc5176ec4d122d9420f3e04c5a92b9e00ca2670dd58"

url = "https://adventofcode.com/2025/day/2/input"

headers = {
    "Cookie": f"session={SESSION_COOKIE}",
}

response = requests.get(url, headers=headers).text

ids = response.split(",")
for id in ids:
    start, end = id.split("-")
    start = int(start)
    end = int(end)

    print("start:", start, "end:", end)


def check_validation(id):
    if id==1:
        return True
    else:
        return False