# Sarah Stephenson

#  Problem 1
 def loop(x):
     while x > 0:
         print("X is greater than one")
loop(1)



# #problem 3
def sum_n(n):
     i = 1
     sum = 0
     while i <= n:
         sum += i
         i += 1

     print("The sum of all numbers from 1 to", n,"is", sum)

sum_n(3)

# problem 4
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(8))
