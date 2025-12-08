import os

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_dir}\\in.txt", "r") as f:
    data = [x.split('\n') for x in f.read().split("\n\n")]

def A(data):
    fresh = 0
    ranges = [x.split('-') for x in data[0]]
    for ingredient in data[1]:
        for start, end in ranges:
            if int(start) <= int(ingredient) <= int(end):
                fresh += 1
                break
    return fresh

def B(data):
    ranges = sorted([list(map(int, x.split('-'))) for x in data[0]])
    compressed = [ranges[0].copy()]
    for [start, end] in ranges:
        if start <= compressed[-1][1]:
            start2, end2 = compressed.pop()
            compressed.append([min(start, start2), max(end, end2)])
        else:
            compressed.append([start, end])
    
    return sum([end - start + 1 for [start, end] in compressed])


print(A(data))
print(B(data))