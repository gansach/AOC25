import os

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_dir}\\in.txt", "r") as f:
    data = list(map(lambda x: (x[0], int(x[1:])), f.read().split()))

def next(curr, direction, rotation):
    if direction == 'L':
        curr -= rotation
    elif direction == 'R':
        curr += rotation
    return curr % 100

def A(data):
    curr = 50
    ans = 0
    for dir, rotation in data:
        curr = next(curr, dir, rotation)
        if curr == 0:
            ans += 1
    return ans

def B(data):
    curr = 50
    ans = 0
    for dir, rotation in data:
        for _ in range(rotation):
            curr = next(curr, dir, 1)
            if curr == 0:
                ans += 1
    return ans

print(A(data))
print(B(data))