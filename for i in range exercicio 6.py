menomedi= 10
maiormedi = 0
apro = 0
repro =0
for i in range(10):
    n1 = float(input("Nota bimestre 1:"))
    n2 = float(input("Nota bimestre 2:"))
    n3 = float(input("Nota bimestre 3:"))
    mediaa = (n1+n2+n3)/3
    if mediaa > maiormedi:
        maiormedi = mediaa
    if mediaa < menomedi:
        menomedi = mediaa
    if mediaa >= 6:
        apro += 1
    else:
        repro += 1
print("menor média:",menomedi,"maior média:",maiormedi,"aprovados:", apro,"reprovados:", repro )