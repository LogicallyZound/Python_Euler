
n = 1000
ans = 0

for x in range(0, n):
   
   if   x % 3 == 0:
      ans += x
   elif x % 5 == 0:
      ans += x

print ans
