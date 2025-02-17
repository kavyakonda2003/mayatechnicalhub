import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Taking input
a, b = map(int, input().split())
print(lcm(a, b))
