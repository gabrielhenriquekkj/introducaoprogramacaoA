n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, n+1):
    fatorial *= i

print("O fatorial de",n,"é", fatorial)