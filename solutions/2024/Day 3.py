import requests
import re

SESSION_COOKIE = "53616c7465645f5fd74bdb22c4af0e2bc8fff114a6ad5eff5a0e958455b0a1d04457be84407f3e7e84481554258eb684d71db896e2524ac9afd8e8edff4f7e01"

url = "https://adventofcode.com/2024/day/3/input"

headers = {
    "Cookie": f"session={SESSION_COOKIE}",
}

response = requests.get(url, headers=headers).text

# Part 1
#
# mul_functions = re.findall(r'mul\((\d+),(\d+)\)', response)

# total_sum = sum(int(x) * int(y) for x, y in mul_functions)

# print(total_sum)


# Part 2
#
mul_enabled = True

total_sum = 0

instructions = re.findall(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)', response)

for instruction in instructions:
    if instruction == 'do()' or instruction == "don't()":
        if instruction == 'do()':
            mul_enabled = True
            print("do() found, mul_enabled set to True")
        elif instruction == "don't()":
            mul_enabled = False
            print("don't() found, mul_enabled set to False")
    else:
        x, y = instruction
        if mul_enabled and x and y:
            print(f"Processing mul({x},{y})")
            total_sum += int(x) * int(y)

print("Total sum:", total_sum)