cp1 = int(input("digite o código da peça 1:"))
num1 = int(input("digite o número de peças 1:"))
vuni = int(input("o valor unitário da peça 1:"))
cp2 = int(input("digite o código da peça 2:"))
num2 = int(input("digite o número de peças 2:"))
vuni2 = int(input("o valor unitário da peça 2:"))
IPI = int(input("percentagem do IPI acrescentado:"))
conta1 = (num1* vuni )* (IPI/100)
conta2 = (num2* vuni2 )* (IPI/100)
cont1 = (num1* vuni ) + conta1
cont2 = (num2* vuni2 ) + conta2

print("o valor a ser pago é:", cont1 + cont2 )