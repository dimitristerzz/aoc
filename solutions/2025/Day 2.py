import requests

SESSION_COOKIE = "53616c7465645f5f5d4b262b6473136e17634719c6129df046cd548d781b5b4523d9326759da7574a67d8dc5176ec4d122d9420f3e04c5a92b9e00ca2670dd58"

url = "https://adventofcode.com/2025/day/2/input"

headers = {
    "Cookie": f"session={SESSION_COOKIE}",
}

response = requests.get(url, headers=headers).text

ranges = []

for id in response.split(","):
    start, end = id.split("-")
    ranges.append((int(start), int(end)))

ranges.sort()
invalid_ids = 0

def check_validation(id: str):
    if len(id) % 2 == 0:
        mid = len(id) // 2
        if id[:mid] == id[mid:]:
            return True
        else:
            return False
    else:
        return False

for start, end in ranges:
    for id in range(start, end + 1):
        if check_validation(str(id)) == True:
            invalid_ids = invalid_ids + id

print(invalid_ids)