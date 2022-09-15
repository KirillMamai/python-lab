import random
s = tuple([random.randint(-10, 10) for _ in range(10)])
print(s)
list=list(s)
for i in range(10):
    if list[i]<0:
        a=list[i]
        list.remove(a)
        break
print(tuple(list))





