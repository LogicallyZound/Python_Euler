
#Way with loops
#

ls = [1, 2 ]
i = 2
su = 0

while ( ls[i-1] < 4000001 ):
  su = ls[i-1] + ls[i-2]
  ls.append(su)
  i+=1
  print i

del ls[len(ls)-1]

print ls

su = 0

for num in ls:
   if  (num % 2) == 0:
      su += num

print su

