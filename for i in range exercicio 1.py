#gabriel henrique leal arruda info 1° A
pos = 0
nega = 0
for i in range (20):
    x = int(input())
    if x<0:
        nega+=1
    else:
        pos+=x
print("a soma dos positivos é:", pos, " a quantidade de negativos é:", nega)