#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem1
num1=int(input("Enter Number1: " ))
num2=int(input("Enter Number2: "))
product = num1*num2
#print("Result:", product)
if product>1000:
    print("Sum of the two integers: ",num1+ num2)


# In[2]:


import math
radius=int(input("Enter the radius of a circle" ))
perimerter=2*math.pi*radius
print("perimerter=",perimerter,"cm")
Area=math.pi*radius**2
print("Area=",Area,"cm^2")


# In[3]:


#problem3
#print("Finding The Total Amount" )
p=int(input("principal:" ))
r=int(input("Interest rate:"))
t=int(input("time:"))
def compound_interest_2019_1_60_156(p,r,t):
    return p * (1 + r/100)**t
print("compund interest",compound_interest_2019_1_60_156(p,r,t))


# In[4]:


number = int(input("Please Enter any Positive Number  : "))
total = 0

total = (number * (number + 1) * (2 * number + 1)) / 6

for i in range(1, number + 1):
    if(i != number):
        print("%d^2 + " %i, end = ' ')
    else:
        print("{0}^2 = {1}".format(i, total))


# In[5]:


#problem no-4
sum = 0
n = int(input("Enter a value : "))
for i in range(1,n+1):
  sum=sum+i**2
print(sum)


# In[6]:


#problem no-5
n = int(input("Enter the number for check prime or not: "))
def prime_find_2019_1_60_156(n):
    for i in range(2, int(n+1/2)):
        if(n%i==0):
             return 1
    else:
      return 0
if(prime_find_2019_1_60_156(n)==0):
   print("It is a Prime number")
else:
   print("It is Not a Prime number")


# In[7]:


#problem no-6
#Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci
#number based on the following assumptions.
#Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1
n = int(input("Enter the nth number to know from fibonacci: "))
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fibonacci(n)


# In[8]:


#problem-7
#Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
#the list. Do not use any built-in function.
lists=[1,11,111,1111,2,22,222,2222,3,33,333,3333]
sum1=0
for i in range(12):
    sum1= sum1 + lists[i]
print("sum is ",sum1)
    


# In[10]:


#problem-8
#Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
#the even-indexed elements in the list.
list=[1,11,111,1111,2,22,222,2222,3,33,333,3333]
sum1=0
for i in range(12):
    if list[i]%2==0:
        sum1= sum1 + lists[i]
    else:continue
print("sum is ",sum1)


# In[15]:


#problem-9
#Given a list of numbers (hardcoded in the program), write a Python program to find the largest and
#smallest element of the list. Define two functions largest_number_<your-student-id> and
#smallest_number_<your-student-id> in your program. Do not use any built-in function.
list=[1,11,111,1111,2,22,222,2222,3,33,333,3333,-4,-44,-444]
def largest_number_2019_1_60_156():
    L=0
    for i in range(13):
        if list[i]>L:
            L=list[L]
    print("Largest number from list is",L)
    
def smallest_number_2019_1_60_156():
    S=56000 #suppose S is S bigger number
    for j in range(13):
        if list[j]<S:
            S=list[j]    
    print("Smallest  number from list is",S)

largest_number_2019_1_60_156()
smallest_number_2019_1_60_156()


# In[16]:


#PROBLEM10
#Given a list of numbers (hardcoded in the program), write a Python program to find the second
#largest element of the list.
#PROBLEM10
list=[1,11,111,1111,2,22,222,2222,3,33,333,3333,-4,-44,-444]
list.sort()
 
# printing the second last element
print("Second largest element is:", list[-2])


# In[18]:


#prOBLEM11
#Given a string, display only those characters which are present at an even index number. Read inputs
#from the user.
# iterate over string
str="mynameissagar"
for index in range(len(str)):
    # check if index is divisible by 2
    if index % 2 == 0:
        # print character at index
        print(str[index], end='')


# In[23]:


#PROBLEM12
#Given a string and an integer number n, remove characters from a string starting from zero up to n
#and return a new string. N must be less than the length of the string. Read inputs from the user. Do
#not use any built-in function.
string=input("Enter String -")
n=int(input("Enter the number n-"))
j=""#define j as a new string for store
for i in range(n,len(string)):
    j=j+string[i]
print(j)


# In[1]:


#PROBLEM13
#Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any
#built-in function.
a = input("Enter the String: ")
sum=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i:j] =='CSE303':
            sum=sum+1
print(f'CSE303 comes in {sum} times.')


# In[28]:


#PROBLEM14
#Given a string, write a python program to check if it is palindrome or not. Define a function named
#palindrome_checker_<your-student-id> in your program.
str1 = input("Enter the String: ")
c=len(str1)
def palindrome_checker_2019_1_60_156():
    for i in range(0,c,1):
        if str1[i] == str1[c-(1+i)]:
            return 1
        else:
            return 0
        
if(palindrome_checker_2019_1_60_156()):
    print("Palindrome")
else:
    print("Not palindrome")


# In[27]:


#PROBLEM15
#Given a two list of numbers (hardcoded in the program), create a new list such that new list should
# contain only odd numbers from the first list and even numbers from the second list.
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
newlist=[]
len1=len(list1)
len2=len(list2)
for i in range (0,len1):
    if(list1[i]%2!=0):
        newlist.append(list1[i])
for j in range(0,len2):
    if(list2[j]%2==0):
        newlist.append(list2[j])
print(newlist)


# In[ ]:





# In[ ]:




