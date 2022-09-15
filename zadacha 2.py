a=str(input("Введите строку"))
print(max(a.split(), key=len))
print(a.swapcase())
cnt=0
for s in a:
    if s.isdigit():
        cnt+=int(s)
if cnt==0:
    print("Нет цифр")
else:
    print(cnt)
