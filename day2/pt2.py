data = []

# Read data
with open("input.txt", "r") as file:
    for line in file:
        data.append(list(map(int, line.split())))

def is_safe(report):
    increase = True
    decrease = True

    for i in range(len(report) - 1):
        level_diff = abs(report[i] - report[i + 1])

        # Check difference constraints
        if level_diff < 1 or level_diff > 3:
            safe = False
            return False

        # Check if consistently increasing or decreasing
        if report[i] < report[i + 1]:
            decrease = False
        elif report[i] > report[i + 1]:
            increase = False

    return increase or decrease

def safe_by_removing_level(report):
    # Remove each level one by one to see if report becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True
    return False

# Count number of safe reports
safe_reports = 0

for report in data:
    if is_safe(report) or safe_by_removing_level(report):
        safe_reports += 1