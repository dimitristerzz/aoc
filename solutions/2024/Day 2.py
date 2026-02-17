from dtutils import getInput

response = getInput("https://adventofcode.com/2024/day/2/input")

def readRowsFromResponse(response):
    rows = []
    for line in response.splitlines():
        rows.append([int(x) for x in line.split()])
    return rows

# Part 1
#
# def is_gradually_increasing_or_decreasing(row):
#     increasing = all(x < y for x, y in zip(row, row[1:]))
#     decreasing = all(x > y for x, y in zip(row, row[1:]))
#     return increasing or decreasing

# def is_difference_between_1_and_3(row):
#     return all(1 <= abs(x - y) <= 3 for x, y in zip(row, row[1:]))

# rows = readRowsFromResponse(response)
# passed_both_checks = 0

# for i, row in enumerate(rows):
#     if is_gradually_increasing_or_decreasing(row):
#         if is_difference_between_1_and_3(row):
#             print(f"Row {i} passed checks: {row}")
#             passed_both_checks += 1
#     else:
#         print(f"Row {i} failed checks: {row}")

# print(f"Total rows that passed both checks: {passed_both_checks}")


# Part 2

def is_gradually_increasing_or_decreasing(row):
    increasing = all(x < y for x, y in zip(row, row[1:]))
    decreasing = all(x > y for x, y in zip(row, row[1:]))
    return increasing or decreasing

def is_difference_between_1_and_3(row):
    return all(1 <= abs(x - y) <= 3 for x, y in zip(row, row[1:]))

def is_safe_if_one_removed(row):
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if is_gradually_increasing_or_decreasing(new_row) and is_difference_between_1_and_3(new_row):
            return True
    return False

rows = readRowsFromResponse(response)
passed_both_checks = 0

for i, row in enumerate(rows):
    if is_gradually_increasing_or_decreasing(row) and is_difference_between_1_and_3(row):
        print(f"Row {i} passes both checks: {row}")
        passed_both_checks += 1
    elif is_safe_if_one_removed(row):
        print(f"Row {i} is safe if one level is removed: {row}")
        passed_both_checks += 1
    else:
        print(f"Row {i} fails checks: {row}")

print(f"Total rows that passed both checks or are safe if one level is removed: {passed_both_checks}")