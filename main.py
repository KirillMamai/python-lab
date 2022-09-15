a= int(input("Введите число\n"))
sum=0
while a>0:
    k=a%10
    if k%2==0:
        sum=sum+k
    a=a//10
if sum==0:
    print("0")
else:
    print(sum)


