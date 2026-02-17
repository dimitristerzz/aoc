from dtutils import getInput

response = getInput("https://adventofcode.com/2024/day/1/input")

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