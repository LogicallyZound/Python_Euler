#Find the largest palindrome made from the product of two three digit numbers
# https://projecteuler.net/problem=4


largest = 0
A = 999
B = 999
product = 0;

def isPalindrome( product ):
   s = str(product)
   if len(s) % 2 != 0:
      return False
   else:
      fir, sec = s[:len(s)/2], s[len(s)/2:]
      sec = sec[::-1]
      if fir == sec:
         return True
      return False

#worst is n^2
while(A >= 100):
   while(B >= 100):
      product = A * B
     # print "%s, %s"  % (A, B)
      if isPalindrome(product) and product > largest:
      #  print 'replacing %s with %s' %(largest, product)
        largest = product 
        break
      B-=1
   A-=1
   B = 999

print largest
