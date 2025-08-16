total = int(input("número total de votos:"))
brancos = int(input("número total de votos  brancos:"))
nulos = int(input("número total de votos nulos:"))
validos = int(input("número total de votos válidos:"))
brancosmat = (brancos/total)*100
nulosmat = (nulos/total)*100
validosmat = (validos/total)*100
print("votos brancos:",brancosmat,"%")
print("votos nulos:",nulosmat,"%")
print("votos válidos:",validosmat,"%")
