import os

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_dir}\\in.txt", "r") as f:
    data = list(f.read().split())

def A(data):
    ans = 0
    for bank in data:
        prev_biggest_battery = 0
        joltage = 0
        for c in bank:
            curr = prev_biggest_battery * 10 + int(c)
            prev_biggest_battery = max(prev_biggest_battery, int(c))
            joltage = max(joltage, curr)
        ans += joltage
    return ans

def max_battery(bank, n):
    ans = 0
    start = 0
    while n:
        end = len(bank) - n

        best_char = bank[start]
        best_pos = start

        for i in range(start, end + 1):
            if bank[i] > best_char:
                best_char = bank[i]
                best_pos = i
        
        start = best_pos + 1
        
        ans = ans * 10 + int(best_char)
        n -= 1
    return ans


def B(data):
    ans = 0
    for bank in data:
        ans += max_battery(bank, 12)
    return ans

print(A(data))
print(B(data))