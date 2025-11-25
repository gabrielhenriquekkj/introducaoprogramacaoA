x = int(input(":"))
c = 0
total = 0
for i in range (1,x+1):
  for p in range(1,i):
   if p%i == 0:
     c+=p
   if c == i:   
    total +=(c*c)
print(total)