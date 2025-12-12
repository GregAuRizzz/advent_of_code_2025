line = input().strip()
total = 0
ranges = line.split(",")

for r in ranges:
    if r == "":
        continue
    start, end = map(int, r.split("-"))

    for n in range(start, end + 1):
        s = str(n)
        if len(s) % 2 != 0:
            continue
        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]
        if a == b:
            total += n
print(total)
