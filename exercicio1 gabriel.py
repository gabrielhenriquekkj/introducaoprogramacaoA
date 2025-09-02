pos = 0
nega=0
for i in range(20):
    num = int(input("sigite o valor:"))
    if num>=0:
        pos +=num
    else:
       nega +=1
print("a soma dos positivos é:",pos,"a quantidade de negativos é:",nega)