# Write a Python program to sum all the items in a list. 
def add():
    list1=[10,20,30,40]
    sum=0
    for x in list1:
        sum+=x
        print(sum)    
add()

def addition(*numbers):
    sum=0
    for y in numbers:
        sum+=y
        print(sum)
addition(10,20,30,40,50,60)

#  Write a Python program to multiply all the items in a list.
def multiple():
    list3=[60,40,30,20,70]
    multiply=1
    for w in list3:
        multiply*=w
        print(multiply)
multiple()

def multi(*number):
    multiple=1
    for i in number:
        multiple*=i
        print(multiple)
multi(60,40,30,20,70)
#  Write a Python program to get the largest number from a list.

def largest_number():
    x=[10,5,60,3]
    y=max(x)       
    print (f"The largest number is {y}")
largest_number()





