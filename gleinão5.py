x = int(input("Digite sua idade:"))
p = 0
if x < 12:
   p+=10
elif x >= 12 and x <= 17:
    p+=15
elif x >= 18 and x <= 59:
    p+=20
if x > 59:
   p+=12

print("O valor do ingresso é:",p)
