import re

# Read data
with open("input.txt", "r") as file:
    data = file.read()

# Pattern to mach mul(a,b)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches
matches = re.findall(pattern, data)

# Calculate sum of products
result = sum(int(a) * int(b) for a, b in matches)