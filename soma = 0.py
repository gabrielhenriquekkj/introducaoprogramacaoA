soma = 0 
nega = 0
a = 0
while a <= 20:
    num = int(input("digite o valor"))
    a+=1
    if num>0:
        soma += num
    else:
        nega +=1

print(nega)
print(soma-1)
