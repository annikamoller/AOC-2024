# Read data into two lists
list1, list2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

# Sort both lists
list1.sort()
list2.sort()

# Calculate total distance
total_distance = 0

for num1, num2 in zip(list1, list2):
    total_distance += abs(num1 - num2)
