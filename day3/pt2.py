import re

# Read data
with open("input.txt", "r") as file:
    data = file.read()

# Patterns to mach mul(a,b), don't() and do()
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
dont_pattern = r"don't\(\)"
do_pattern = r"do\(\)"

enabled = True
result = 0

# Make input into tokens
tokens = re.split(r"(mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\))", data)

# Process each token
for token in tokens:
    if token:
        token = token.strip()
        if re.match(dont_pattern, token):
            enabled = False
        elif re.match(do_pattern, token):
            enabled = True
        else:
            match = re.match(mul_pattern, token)
            if match and enabled:
                a, b = map(int, match.groups())
                result += a * b