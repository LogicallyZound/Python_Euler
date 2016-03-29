#find the smallest positive number evenly divisible by all numbers 1 to 20
# https://projecteuler.net/problem=5

lcm = 1
i = 1
currMultiple = 1

# based off the premise that by adding the current multiple, the new number will be
# a multiple of (1 to i) * x with i being the current number from 1-20 and x being
# the number of times we added the number

while (i < 21):
   if lcm % i != 0:
      lcm+= currMultiple
   else:
      i +=1
      currMultiple = lcm

print lcm
