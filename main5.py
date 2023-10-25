with open("input.txt", encoding='utf-8') as file:
    a = file.read().split()

print(len(set(a)))