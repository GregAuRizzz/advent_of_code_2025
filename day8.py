import sys
from scipy.spatial import KDTree

points = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    x, y, z = map(int, line.replace(" ", "").split(","))
    points.append((x, y, z))

n = len(points)

parent = list(range(n))
size = [1] * n

def find(x):
    path = []
    while parent[x] != x:
        path.append(x)
        x = parent[x]
    for node in path:
        parent[node] = x
    return x

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parent[ry] = rx
    size[rx] += size[ry]
    return True

tree = KDTree(points)
edges = []

k_neighbors = min(50, n) 

for i, p in enumerate(points):
    distances, indices = tree.query(p, k=k_neighbors)
    
    if not hasattr(distances, "__iter__"):
        distances = [distances]
        indices = [indices]
        
    for dist, j in zip(distances, indices):
        if i < j:
            edges.append((dist, i, j))

edges.sort()
edges_to_process = edges[:1000]

for dist, i, j in edges_to_process:
    union(i, j)

circuit_sizes = {}
for i in range(n):
    root = find(i)
    circuit_sizes[root] = size[root]

largest_sizes = sorted(circuit_sizes.values(), reverse=True)[:3]

result = 1
for s in largest_sizes:
    result *= s

print(result)