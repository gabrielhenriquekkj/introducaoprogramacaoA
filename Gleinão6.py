horas = int(input("quantas horas por semana você joga?:"))
gasto = int(input("quanto dinheiro por mês você gasta?:"))
baixados = int(input("quantos jogos você tem instalados?:"))

if horas > 10:
   print("Classificação: CASUAL 🙂")
if gasto > 30:
   print("Classificação: CASUAL 🙂")
if baixados > 10:
   print("Classificação: CASUAL 🙂")

if horas >= 30:
    if gasto >= 100:
        if baixados >= 20:
            print("Classificação: HARDCORE 🔥")

if horas <= 29:
 if horas >= 10:
    if gasto <= 99:
        if gasto >= 30:
           if baixados <= 19:
              if baixados >= 10: 
                 print("Classificação: INTERMEDIÁRIO ⚡") 
