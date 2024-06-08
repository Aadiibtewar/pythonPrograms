# def about(name, age):
#     return (f"My name is {name} and age is {age}")
#
#
# print(about("raju", 22))        #positional argument
# print(about(name="ramesh", age=66))        #keyword argument


# def co(*args,**kwargs):
#     print(args,kwargs)              # we can use *args in return but can't use **args
#                                     # *args return in tuple and ** will give dict
#



# 1.wap to perform addition and subtraction if "a" is greater than "b" return sum else return difference

# def sum_diff(a,b):
#     if a>b:
#         return a+b
#     else:
#         return a-b
#
# print(sum_diff(a=25,b=24))
#
#


# 2.waf to check string is palindrome or not (take user input)
# s= input("enter")
# def palindrome(s):
#     if s == s[::-1]:
#         return "palindrome"
#     else:
#         return "not palindrome"
#
#
# print(palindrome(s))
#


# 3.wap to return length of variable keywords arguments

# def varKey(**kwargs):
#     return kwargs
#
# k=(varKey(a=10,b=20,c=30,d=40))
# print(len(k))



# 4.wap to return length of the variable positional arguments

# def varpos(*args):
#     return args
#
# p=varpos(10,20,50,45,52,"hi","hello")
# print(len(p))


# 5.waf to search for character in a given string and return corresponding index
#   string="coding part is done"


# def search(s,ch):
#     for i in range(0,len(s),1):
#         if ch in s[i]:
#             return i
# string="coding part is done"
# print(search(string,"i"))


# # 6.wap to squaring of the element in the given list
# l=[1,2,3,4,5]
#
# def square(sq):
#     return sq**2
# s=[]
# for i in l:
#     s.append(square(i))
# print(s)

# 7.wap to fetch last digit number

# def lastDigit(ip):
#     s=str(ip)
#     ld=s[-1]
#     return int(ld)
#
# print(lastDigit(545))

# 8.wap to read 3 numbers from the user,first two
# numbers should be added and the result of addition should be subtracted by third number

# def addtwo(a,b,c):
#     return (a+b)-c
#
# a,b,c=int(input("Enter values: ")),int(input()),int(input())
# print(addtwo(a,b,c))

# 9.wap to find square,cube,square root and cube root of a number

# def op(ip):
#     return ip**2,ip**3,ip**0.5,(ip**0.5)/ip
#
# print(op(100))


# 10.wap to check the given characters
# is alphabets or digit or special characters

# def check(s):
#     if s.isalpha():
#         print(f" {s} is alphabet")
#     elif s.isdigit():
#         print(f"{s} is digit")
#     else:
#         print(f"{s} is special character")
# check("g")

# 11.wap to check given iterable is a sequence,if it is a sequence
# reverse it,if not add one extra element to the iterable

# def isseq(a):
#     if isinstance(a,(list,tuple,str)):
#         return a[::-1]
#
#     else:
#         if type(a)==set:
#             a.add(input("add element in set"))
#             return a
#         if type(a)==dict:
#             a.update({eval(input("enter key")):eval(input("enter value"))})
#             return a
#
# a={"a":"one","b":"two"}
# print(isseq(a))


# 12.write a function to print the below output
# func("TRACXN",1)
#should print RCN

# def sl(s):
#     return s[1::2]
# print(sl("TRACXN"))



# 13.write a function to print the below output
# func("TRACXN",0)
#should print TAX

# def func(s):
#     return s[::2]
#
# print(func("TRACXN"))

# 14.A function take variable number of positional arguments
#    as input. how to check if the arguments are more than 5.

# def func(*args):
#     if len(args)>5:
#         return "more than 5 arguments"
#     elif len(args)==5:
#         return "equal to 5 arguments"
#     else:
#         return "less than 5 arguments"
#
# print(func(1,55,56,48,55))


# 15.WAF to reverse any iterable without using reverse function
# def rev(itr):
#     if isinstance(itr,(list,tuple,str)):
#         for i in range(len(itr)-1,-1,-1):
#             print(itr[i] , end=" ")
#     else:
#         print("unable to reverse")
# rev([1,5,565,2,6])

# 16.waf to return a dictionary with characters and ascii value pair
# def ch_ascii(s):
#     st=str(s)
#     d={}
#     for i in st:
#         d[i]=ord(i)
#     return d
# print(ch_ascii("sundAy"))

# 17.waf to reverse a iterable if you are passing
# string or list or tuple else print type of the data

# def rev(itr):
#     if isinstance(itr,(list,tuple,str)):
#         for i in range(len(itr)-1,-1,-1):
#             print(itr[i] , end=" ")
#     else:
#          print(f"{itr} is {type(itr)} data")
#
# rev({2,2,5,3,1,4})




