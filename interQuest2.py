# Write a function to find the nth Fibonacci number using recursion.
def fibonacci(num):
   fab=[0,1]
   for x in range(2,num):
      next_fab=fab[x-1] + fab[x-2]
      fab.append(next_fab) 
   return fab
number=int(input("Please Enter Number"))
print(fibonacci(number))