import requests

SESSION_COOKIE = "53616c7465645f5f02f05bfb338a98c493c554f579488c901f1430ff471d197ee00d6773a3c6cf5f4a0c66cf77c30cdba9588b4821923bf2108f25a981efabcd"

url = "https://adventofcode.com/2024/day/1/input"

headers = {
    "Cookie": f"session={SESSION_COOKIE}",
}

response = requests.get(url, headers=headers).text

def readColumnsFromResponse(response):
    column1 = []
    column2 = []
    lines = response.splitlines()
    for line in lines:
        numbers = line.split()
        if len(numbers) == 2:
            column1.append(int(numbers[0]))
            column2.append(int(numbers[1]))
    return column1, column2

column1, column2 = readColumnsFromResponse(response)

# Part 1
#
# column1.sort()
# column2.sort()
#
# sum_of_differences = sum(abs(a - b) for a, b in zip(column1, column2))
#
# print("Sum of differences:", sum_of_differences)


# Part 2

from collections import Counter

count_column2 = Counter(column2)

total_similarity_score = 0

for number in column1:
    total_similarity_score += number * count_column2.get(number, 0)

print("Total similarity score:", total_similarity_score)