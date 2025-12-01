c = 50
count = 0
try:
    while(True):
        line = input()
        if len(line) > 2:
            remove = int(line[-2:])
        if len(line) == 2:
            remove = int(line[-1:])
        if line[0] == "L":
            c-=remove
            if c < 0:
                c = 100-abs(c)
        else:
            c+=remove
            if c > 0:
                if c > 99:
                    c = 100-abs(c)
                c = abs(c)
        if c == 0:
            count+=1
except EOFError:
    pass
print(count)
