import os

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_dir}\\in.txt", "r") as f:
    data = list(map(lambda x: x.split('-'), f.read().split(',')))

def A(data):
    ans = 0
    for x, y in data:
        for i in range(int(x), int(y) + 1):
            n = len(str(i))
            if n % 2 == 0:
                if str(i)[:n//2] == str(i)[n//2:]:
                    ans += i
    return ans

def B(data):
    ans = 0
    for x, y in data:
        for i in range(int(x), int(y) + 1):
            n = len(str(i))
            for j in range(1, n // 2 + 1):
                if n % j == 0 and str(i)[:j] * (n // j) == str(i):
                    ans += i
                    break
    return ans

print(A(data))
print(B(data))
