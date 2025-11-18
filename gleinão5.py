x = int(input("Digite sua idade:"))
x = 0
if x < 12:
   x+=10
elif x >= 12 and x <= 17:
    x+=15
elif x >= 18 and x <= 59:
    x+=20
if x > 59:
   x+=12
print("O valor do ingresso é:",x)