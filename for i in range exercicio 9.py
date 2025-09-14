cont = 0 
x = int(input("digite um número para saber se ele é primo:"))
for i in range(1,x+1):
    if x % i == 0:
     cont += 1
if cont==2:
   print(" é primo:")
else:
   print("não é primo:")