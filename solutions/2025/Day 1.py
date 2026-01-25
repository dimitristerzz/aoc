import requests

SESSION_COOKIE = "53616c7465645f5f5d4b262b6473136e17634719c6129df046cd548d781b5b4523d9326759da7574a67d8dc5176ec4d122d9420f3e04c5a92b9e00ca2670dd58"

url = "https://adventofcode.com/2025/day/1/input"

headers = {
    "Cookie": f"session={SESSION_COOKIE}",
}

response = requests.get(url, headers=headers).text


rotations = response.splitlines()
dial = 50
count = 0

for rotation in rotations:
    direction = rotation[0]
    steps = int(rotation[1:])

    if direction == "L":
        for step in range(steps):
            dial = (dial - 1) % 100
            if dial == 0:
                count += 1
    else:
        for step in range(steps):
            dial = (dial + 1) % 100
            if dial == 0:
                count += 1

print(count)


# import time

# def timeit(func, *args, **kwargs):
#     start = time.perf_counter()
#     result = func(*args, **kwargs)
#     elasped = time.perf_counter() - start
#     print(f"Elapsed time: {elasped:.6f} seconds")
#     return result

# def stepcount(n, steps):
#     if n == 0:
#         return 1
    
#     if n < 0:
#         return 0

#     return sum(stepcount(n-s, steps) for s in steps)

# def memsteps(n, steps):
#     return memsteps_cache(n, steps, {})

# def memsteps_cache(n, steps, cache):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0

#     if n in cache:
#         return cache[n]

#     total = sum(memsteps_cache(n - s, steps, cache) for s in steps)

#     cache[n] = total
#     return total