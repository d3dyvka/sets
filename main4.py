a = input()
b = set()
for i in a.split():
    n = int(i)
    if n in b:
        print("yes")
    else:
        print("no")
        b.add(n)