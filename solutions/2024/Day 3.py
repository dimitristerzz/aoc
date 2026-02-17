from dtutils import getInput
import re

response = getInput("https://adventofcode.com/2024/day/3/input")

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