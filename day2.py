data = []

# Read data
with open("input.txt", "r") as file:
    for line in file:
        data.append(list(map(int, line.split())))

safe_reports = 0

for report in data:
    increase = True
    decrease = True
    safe = True

    for i in range(len(report) - 1):
        level_diff = abs(report[i] - report[i + 1])

        # Check difference constraints
        if level_diff < 1 or level_diff > 3:
            safe = False
            break

        # Check if consistently increasing or decreasing
        if report[i] < report[i + 1]:
            decrease = False
        elif report[i] > report[i + 1]:
            increase = False

    if safe and (increase or decrease):
        safe_reports += 1
