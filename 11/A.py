import os

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_dir}\\in.txt", "r") as f:
    data = [row.split(': ') for row in f.read().split('\n')]

graph = {}
for node, neighbors in data:
    for neighbor in neighbors.split():
        x = graph.get(node, [])
        x.append(neighbor)
        graph[node] = x

def A(graph):
    def dfs(node):
        if node == 'out':
            return 1
        
        paths = 0
        for neighbor in graph[node]:
            paths += dfs(neighbor)

        return paths

    return dfs('you')

def B(graph):
    memo = {}
    def dfs(node, visited_fft, visited_dac):
        if (node, visited_fft, visited_dac) in memo:
            return memo[(node, visited_fft, visited_dac)]

        if node == 'out':
            if visited_fft and visited_dac:
                return 1
            return 0

        visited_fft = visited_fft or (node == 'fft')
        visited_dac = visited_dac or (node == 'dac')

        paths = 0
        for neighbor in graph[node]:
            paths += dfs(neighbor, visited_fft, visited_dac)

        memo[(node, visited_fft, visited_dac)] = paths
        return paths

    return dfs('svr', False, False)

print(A(graph))
print(B(graph))