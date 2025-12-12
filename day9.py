import sys

points = []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    x, y = map(int, line.split(","))
    points.append((x, y))

max_area = 0
n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        
        area = width * height
        
        if area > max_area:
            max_area = area

print(max_area)