import math
n = int(input("Enter a positive number"))
if n <= 0:
  print("Please enter a positive integer:")
else:
  total = 0
  for i in range (1,n+1):
    total += i/math.factorial(i)
    print("sum of the series:",total)
    
  
