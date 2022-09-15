n = int(input("Введите число"))
s = 0
list = []
for s in range(1, n+1):
    if n % s == 0:
        list.append(s)
print(list)
print(max(list))
print(min(list))



