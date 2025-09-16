
print ("MENU-------\n"
 "Escolha uma opção:\n"
 "1 para subtração\n"
 "2 para soma\n"
 "3 para multiplicação\n"
 "4 para divisão\n"
 "5 para número primo\n"
 "6 para fatorial\n"
 "7 para verificar ímpar ou par\n" 
 "Para sair, digite 'sair'\n")
a = 1
while a==1:
 x = input("escolha: ")
 if x =="1":
  v1 =float(input("digite:"))
  v2 =float(input("digite:"))
  print(v1-v2)
 elif x =="2":
  v1 =float(input("digite:"))
  v2 =float(input("digite:"))
  print(v1+v2)
 elif x =="3":
  v1 =float(input("digite:"))
  v2 =float(input("digite:"))
  print(v1*v2)
 elif x =="4":
  v1 =float(input("digite:"))
  v2 =float(input("digite:"))
  print(v1/v2)
 elif x =="5":
  cont = 0
  v1 =float(input("digite:"))
  for i in range (1,v1+1):
   if v1 % i == 0:
    cont += 1
    if cont == 2:
     print("é primo")
    else:
     print("não é primo")
 elif x == "6":
    fatorial = 1
    v1 = float(input("digite:")) 
    for i in range(1,v1+1):
     fatorial *=i
     print (fatorial)
 elif x == "7":
     v1 = float(input("digite:")) 
     y = v1%2
     if y == 0:
      print("é par")
     else:
      print("é ímpar")
t = input("quer sair? 1 = sim 2 = 2")
if t =="sim":
  a+=1