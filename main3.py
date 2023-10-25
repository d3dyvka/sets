a = [1, 2, 3, 4, 1, 1, 2, 5, 8, 11 ,2, 5]
b = [1 ,5, 6,2, 8, 9, 8, 11, 2 , 7, 1, 1]
c = set()
for i in a:
    if i in b:
        c.add(i)

print(sorted(c))