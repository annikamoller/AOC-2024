with open("input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]


def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = 4
    count = 0

    # (dx,dy)
    directions = [
        (0, 1),  # Horisontal
        (0, -1),  # Horisontal
        (1, 0),  # Vertical
        (-1, 0),  # Vertical
        (1, 1),  # Diagonal
        (-1, 1),  # Diagonal
        (1, -1),  # Diagonal
        (-1, -1),  # Diagonal
    ]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                end_x = i + (word_len - 1) * dx
                end_y = j + (word_len - 1) * dy
                if 0 <= end_x < rows and 0 <= end_y < cols:
                    match = True
                    for k in range(word_len):
                        ni = i + k * dx
                        nj = j + k * dy
                        if grid[ni][nj] != word[k]:
                            match = False
                            break
                    if match:
                        count += 1
    return count
