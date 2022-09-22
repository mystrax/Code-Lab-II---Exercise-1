from re import A
from turtle import title

print("Hello, user!")
name=input("What is your name:")
a=name.title()
age=input("What is your age:")
print(age)
print("It is good to meet you",a)
print("The length of your name is:\n",len(name))
age2=int(age)+1
print("You will be",age2,"in a year!")
