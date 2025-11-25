x = 1
c = 0
d = 0
while x == 1:
   r = float(input(":"))
   d+=1
   if r<=10:
     if r >=0:
       c+=r
   if r == -1:
    x = 2
    print(c,"total")
    print(c/d,"média")
