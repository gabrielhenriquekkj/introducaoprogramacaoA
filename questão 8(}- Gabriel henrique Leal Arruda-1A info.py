x = int(input("coloque aqui os segundos:"))
hora = x // 3600
r = x% 3600
min = r//60
seg = r/60
print("suas horas são:",hora,"seus minutos:",min,"seus segundos",seg)