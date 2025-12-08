import os

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_dir}\\in.txt", "r") as f:
    data = [tuple(map(int, row.split(','))) for row in f.read().split()]

def find(i, parent):
    if i == parent[i]:
        return i
    parent[i] = find(parent[i], parent)
    return parent[i]

def union(i, j, parent, size):
    i, j = find(i, parent), find(j, parent)
    if i == j:
        return
    
    if size[i] < size[j]:
        parent[i] = j
        size[j] += size[i]
    else:
        parent[j] = i
        size[i] += size[j]

def join_closest(boxes, parent, size):
    min_dist = 1e9
    box1_idx, box2_idx = 0, 0
    for i in range(len(boxes)):
        x1, y1, z1 = boxes[i]
        for j in range(i + 1, len(boxes)):
            x2, y2, z2 = boxes[j]
            dist = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 + abs(z1 - z2) ** 2
            if dist < min_dist and parent[i] != parent[j]:
                min_dist = dist
                box1_idx = i
                box2_idx = j

    union(box1_idx, box2_idx, parent, size)
    return data[box1_idx], data[box2_idx]
    
def A(data):
    parent = [i for i in range(len(data))]
    size = [1] * len(data)

    for t in range(1000):
        print(t)
        join_closest(data, parent, size)

    p = 1
    sizes = sorted([size[i] for i in set(parent)])[-3:]
    for i in sizes:
        p *= i
    return p

def B(data):
    parent = [i for i in range(len(data))]
    size = [1] * len(data)

    t = 0
    while len({find(i, parent) for i in range(len(data))}) > 2:
        join_closest(data, parent, size)
        t += 1
        print(t)

    (x1, _, _), (x2, _, _) = join_closest(data, parent, size)
    return x1 * x2

print(A(data))
print(B(data))