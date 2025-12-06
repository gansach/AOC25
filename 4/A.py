import os

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_dir}\\in.txt", "r") as f:
    data = list(f.read().split())

data = list(map(lambda x: list(x), data))

def get_adjacent(i, j, rows, cols):
    adjacent = []
    d = [0, -1, 1]
    for dx in d:
        for dy in d:
            if (dx != 0 or dy != 0) and 0 <= i + dx < rows and 0 <= j + dy < cols:
                adjacent.append((i + dx, j + dy))
    return adjacent

def A(data):
    ans = 0
    rows, cols = len(data), len(data[0])
    removable = []
    for i in range(rows):
        for j in range(cols):
            if data[i][j] != '@':
                continue

            rolls = 0
            for ni, nj in get_adjacent(i, j, rows, cols):
                rolls += 1 if data[ni][nj] == '@' else 0
            
            if rolls < 4:
                ans += 1
                removable.append((i, j))
    return ans, removable

def B(data):
    r = [0]
    ans = 0
    while len(r):
        cnt, r = A(data)
        ans += cnt
        for i, j in r:
            data[i][j] = 'X'
    return ans
    

print(A(data)[0])
print(B(data))