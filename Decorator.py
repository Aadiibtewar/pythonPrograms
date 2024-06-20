'''
def outer (func):
    def inner(*args, **kwargs):
    print(modified main func)
    func(*args, **kwargs)
return inner

@outer
def main_func():
    statements
    return statement
print(main_func(arguments))
'''



#2. WADF TO ADD 2 NUMBERS AND DISPLAY THE MESSAGE
# BEFORE AND AFTER PERFORMING THE ADDITION

# def addition(func):   #func==add
#     def inner(*args):
#         print("im performing addition")
#         func(*args)
#         print("addition is done")
#     return inner
# @addition
# def add(*args):
#     c=sum(args)
#     print(c)
# add(1,2,3,4,5,3,4,6,8)



#3. CREATE A DECORATOR TO RETURN ONLY POSITIVE OUT FROM ANY SUBTRACTION

# def outer(func):
#     def inner(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return (abs(res))
#     return inner
# @outer
# def sub(a,b):
#     return a-b
# print(sub(-20,2))


#4. WAP TO CREATE A DECORATOR FUNCTION THAT MEASURES
# THE EXECUTION TIME OF THE FUNCTION AND PRINT IT

# import time
#
# def outer(func):
#
#     def inner():
#
#         start= time.time()
#
#         func()
#
#         end = time.time()
#
#         execution_time = end-start
#
#         print(f"{func.__name__} took {execution_time} seconds")
#
#     return inner
#
# @outer
# def display():
#     time.sleep(3)
# display()

#5. WRITE A DECORATIVE FUNCTION TO PRINT THE TYPE OF DATA TYPE BEFORE
# PERFORMING THE ACTION

# def outer(func):
#     def inner(*args):
#         for i in args:
#             print(f"type of {i} is {type(i)}")
#         func(*args)
#     return inner
# @outer
# def display(*args):
#     print(sum(args))
# display(2,3)






#1. WADF TO CHECK HOW MUCH TIME IT IS TAKING TO PERFORM EACH TASK

# import time
# def outer(func):
#     def inner(*args):
#         start= time.time()
#         time.sleep(2)
#         func(*args)
#         end=time.time()
#         print(end-start)
#     return inner
#
# @outer
# def add(a,b):
#     print(f"addition of two numbers is {a+b}")
# add(2,4)
#
# @outer
# def sub(a,b):
#     print(f"subtraction of two numbers is {a-b}")
# sub(4,5)

#2. WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME
# , DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS ,
# DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER
# import time
# def outer(name):
#     def inn(arg):
#         time.sleep(3)
#         print(name(arg))
#     return inn
#
#
# @outer
# def name(name):
#     return name
#
# @outer
# def email(mail):
#     return mail
# @outer
# def phn(phn):
#     return phn
# name(input("Enter name"))
# email(input("enter email"))
# phn(eval(input("enter phone number")))


#3. WAP TO CREATE A DECORATOR TO WHICH PRINTS
# THE NAME OF THE CALLED FUNCTION ALONG WITH IT SHOULD
# CHECK IF THE NUMBER IS EVEN OR ODD


# def outer(func):
#     def inner(*args,**kwargs):
#         print(f"the decorated function is {func.__name__}")
#         res = func(*args,**kwargs)
#         return res
#     return inner
#
# @outer
# def display(num):
#     if num % 2 ==0:   #1% 2 == 0
#         return "num is even"
#     else:
#         return "num is odd"
# print(display(1))
# print(display(2))


# # 5..wadf to input 3 seconds before executing function?
# import time
# def delay(func):
#     def inner(*args):
#         time.sleep(3)
#         func(*args)
#     return inner
# @delay
#
# def even():
#     for i in range(1,11):
#          print(i)
# even()


# multiple decorators---------------
# def msg1(func):
#     def inner(*args):
#         print("good morning guys")    #decorator func1
#         func(*args)
#     return inner
#
#
# def msg2(func):
#     def wrapper(*args):
#         print("good night")         #decorator func2
#         func(*args)
#     return wrapper
#
#
# def msg3(func):
#     def display(*args):
#         print("its rainy day")
#         func(*args)
#     return display
#
#
# @msg1
# @msg2
# @msg3
# def greet():
#     print("good evening")    #main function
# greet()

# 1.write a decorator function that prints "HELLO EVERYONE" message before execute any function
# def hello(fun):
#     def inner():
#         print("HELLO EVERYONE")
#         fun()
#     return inner
# @hello
# def info():
#     print("I Am Software Developer")
# info()



# 2.write a decorator function to print main function name before executing any decorator function

# def outer(fun):
#     def inn():
#         print(fun.__name__)
#         fun()
#     return inn
# @outer
# def greet():
#     print("Good Morning")
# greet()




# 3.write a decorator which inputs 5 seconds of delay before executing any decorator function
# from time import sleep
# def test(fun):
#     def test2():
#         sleep(5)
#         fun()
#     return test2
# @test
# def func():
#     print("5 sec delay")
# func()


# 4.write a decorator function calculate the execution time of any function
#
# import time
# def outer(fun):
#     def inner(a,b):
#         st=time.time()
#         fun(a,b)
#         end=time.time()
#         print(f"execution time is {end - st}")
#     return inner
# @outer
# def add(a,b):
#     time.sleep(1)               # it executes very fast so i put delay for 1 sec
#     print(a+b)
# (add(40,50))


# 5.wadf to check if the 1st arguments is lesser than 2nd argument if then swap them and perform division
# but the condition is you should not modify the original function

# def out(fun):
#     def inn(a,b):
#         fun(a,b)
#         return a/b
#     return inn
# @out
#
# def arg(a,b):
#     if a<b:
#         temp=a
#         a=b
#         b=temp
#     return a,b
# print(arg(20,30))
# 6.wadf to add 2 numbers and display the message before "i am doing addition operation" after performing print the message "addition operation is done"
#
# o/p--->i am doing addition operation"
#        value
#      "addition operation is done
#
# def out(fun):
#     def inn(a,b):
#         print("i am doing addition operation")
#         print(fun(a,b))
#         print("addition operation is done")
#     return inn
# @out
# def add(a,b):
#     return a+b
# add(20,60)

# 7.create a decorator to return only positive out from any subtraction

# def ot(f):
#     def i(a,b):
#         print(abs(f(a,b)))
#     return i
# @ot
# def sub(a,b):
#     return a-b
# sub(10,20)




# 8.create a decorator which counts the number of function calls
#
# ct=0
# def outer(co):
#     def inner():
#         global ct
#         co()
#         ct+=1
#     return inner
# @outer
# def greet():
#     print("hi")
# greet()
# greet()
#
# print(ct)
#
# 9.wap to sum of the positional arguments and get the length of the keywords arguments
#9

# def outer(func):
#     def inner(*args,**kwargs):
#         print(sum(args),len(kwargs))
#     return inner
# @outer
# def add(a,b,c,d,e,i=10,j=20,k=30):
#     ...
# add(10,20,30,40,5,i=20,j=30,k=50)




# 10.write a decorator function to print the type of datatype before performing the action

# def outer(fun):
#     def inner(*args):
#         for i in args:
#             print(i,type(i))
#         print(fun(args))
#     return inner
# @outer
# def add(*args):
#     return sum(*args)
# add(45451,55.45,True,False,33*2j)









# 11.write a decorator operation on the given number and the condition is A>B then perform multiplication in decorator function else
#  cube it in decorator

# def outer(fun):
#     def inner(a,b):
#         if a>b:
#             print(a*b)
#         else:
#             print(a**3,b**3)
#     return inner
# @outer
# def op(a,b):
#     ...
# op(10,20)
#
# 12.create a decorators to which prints name of called main function and counts the function calls
#
# 13.create a decorators to which prints names of called functions and checks the number is even or odd
#
# 14.create a decorator which delays its execution as per user input
#
# 15.write a multilevel decorator to log some message
#
# 16.write a multilevel decorators to accept username and register number of employee

# 17.WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME, DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS ,
#  DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER

# 18 using 3 decorators show me one example
