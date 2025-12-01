# Fetch Input
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
    
    # update dial
    if direction == "L":
        dial = (dial - steps) % 100
    else:
        dial = (dial + steps) % 100

    if dial == 0:
        count += 1

print(count)


# distance = distance % 100

# for i in range(0, len(input)-1):
#     distance = int(input[i].strip('RL'))
#     initLetter = input[i][0]

# if initLetter=="R":
#     distance = 50 + distance
#     print(distance)

# if initLetter=="L":
#     distance = 50 - distance





# Store Input In List
# input = response.split('\n')
# start = 50
# for i in range(0,len(input)-1):
#     # string number 
#     sez = input[i].strip('RL')
#     sez = int(sez)
 
#     if 'R' in input[i]:
#         if 99-start > sez :
#             start = -1 +sez - (99-start)
        
#     else:
#         pass
    