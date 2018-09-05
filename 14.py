#Q.1

l1=[1,4,7,12,25]
l2=[i**3 for i in l1]
print(l2)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
low=int(input())
high=int(input())
lst=[i for i in range(low,high+1) if i>1 if all(i%j!=0 for j in range(2,i))]
print(lst)

#Q.3- Write the main differences between List Comprehension and Generator Expression.
#LIST COMPREHENSION:->list comprehensions allow you to create lists with a for loop with less code.

#The comprehensions are not limited to lists.
#You can create dicts and sets comprehensions as well.

#GENERATOR EXPRESSION:->Generator is an iterable created using a function with a yield statement. 

#The main feature of generator is evaluating the elements on demand.
#When you call a normal function with a return statement the function
#is terminated whenever it encounters a return statement.
#In a function with a yield statement the state of the function is
#“saved” from the last call and can be picked up the next time you
#call a generator function.


#LAMBDA & MAP
#Q.4- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit=list(map(lambda c:((c*9)/5)+32,Celsius))
print(Fahrenheit)

#Q.5- Apply an anonymous function to square all the elements of a list using map and lambda.


lst=[2,4,5,8,12,13,45]
lst2=list(map(lambda x:x*x,lst))
print(lst2)

#FILTER & REDUCE
#Q.6- Filter out all the primes from a list.

def prime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
       else:
           return True

lst=[1,2,3,4,5,6,7,21,23]
pr=list(filter(prime,lst))
print(pr)

#Q.7- Write a python program to multiply all the elements of a list using reduce.

from functools import *
lst=[1,2,3,5,7,12]
m=reduce(lambda x,y:x*y ,lst)
print(m)













