#1 Example on recursive function factorial of a number
def factorial(n):
    if (n==0 or n==1):
        return n
    else:
        return n*factorial(n-1)
print(factorial(8))

print()

#2 fibonacci series

def fibonicca(m):
    if (m==0 or m==1):
        return m
    else:
        return fibonicca(m-1) + fibonicca(m-2)
print(fibonicca(10))


#3 example on lambda function

add = lambda num: num + 4    
print( add(6) )  

#4 example of lambda function

sqr=lambda num : num * num
print(sqr(5))

# 5 example

a= lambda a,b,c : a+b+c
print(a(5,4,6))

#filter function Example 
def check_even(number):
    if number % 2 == 0:
          return True 
    else: 
       return False


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,20,30,40,23,45]

even_numbers = filter(check_even, numbers)

even_numbers = list(even_numbers)
print(even_numbers)

#filter vowels
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filter_vowels(letters):
    vowels = ['a','e' ,'i' ,'o','u']
    return True if letters in vowels else False
filter_vowels = filter(filter_vowels, letters)
vowles = tuple(filter_vowels)

print(vowles)

#example on map function
def sum(n):
    return n+n
num=(1,4,5,6,8)
result = map(sum,num)
print(list(result))

#example on map function
def sqr(n):
    return n*n
num=(1,4,5,6,8,12)
result = map(sqr,num)
print(list(result))

#example on reduse()
from functools import*
l=[20,30,40,50,100]
result = reduce (lambda x,y:x+y,l)
print(result)

#example on lambda function 
from functools import*

myNumbs = [1, 2, 3, 4]
res = reduce(lambda a, b: a * b, myNumbs)
print(res)

#nested function get cube of a number

def get_power(num):
    def power(n):
        return num**n
    return power(3)
print(get_power(10))



#example of nested function

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
f = outer_function(10)
result = f(5)
print(result)






    


