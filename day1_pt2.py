# Read data into two lists
list1, list2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

# Calculate similarity score
similarity_score = 0

while list1:
    similarity_score += list1[0] * list2.count(list1[0])
    list1 = list1[1:]
