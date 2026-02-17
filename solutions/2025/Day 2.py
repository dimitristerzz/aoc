from dtutils import getInput

response = getInput("https://adventofcode.com/2025/day/2/input")

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