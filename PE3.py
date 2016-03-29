#Implementation of an algorithm given on http://math.stackexchange.com/questions/389675/largest-prime-factor-of-600851475143

A = 600851475143    #The large number being factored 
B = 2   #The current divisor
C = 0   #The largest divisor that worked

while(A != 1):
      if A % B == 0:
         A = A / B
         C = B
         B = 2
      else:
         B+=1

print C


