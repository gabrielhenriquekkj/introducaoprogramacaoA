n = float(input("digite o valor da compra:"))
por = n*0.10
if n<100:
    print("sem desconto")
else:
 print("o desconto é de:",por,"reais, o valor final é",n-por)