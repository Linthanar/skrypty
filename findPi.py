# import math

# def findPi(n):
#     x = math.pi
#     return round(x, n-1)

# print(findPi(9))


import math

def print_pi(n):
    format_string = "{:.%df}" % n
    print(format_string.format(math.pi))

print_pi(6)