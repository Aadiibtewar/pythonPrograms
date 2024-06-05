 # 1.
#
# num = int (input("Enter the num"))
# if num%2==0:
#     print("Even")
# else:
#     print("odd")

# 2.
#
# m_age=int(input("male age"))
# f_age=int(input("female age"))
# if m_age>=21 and f_age>=18:
#     print("eligible for marrage")
#
# else:
#     print("not eligible")

# # 3.
# char=input("enter char")
# if char.islower():
#     print(char.upper())
# else:
#     print(char)
#4
# char=input("enter char")
# if char.isupper():
#     print(char.lower())
# else:
#     print(char)

# 5.
# n1=34
# n2=54
#
# if n1<n2:
#     print(n2)
# else:
#     print(n1)



#6.wap to check if the given number is even or not,if
# it is not even add+1 and make it even (take user input)

# num = eval(input("Enter the num"))
# if num%2==0:
#     print (f"{num} is even")
# else:
#     num+=1
#     print(f"{num} is even")

# 7.wap to check whether the first character in the given
# string is starting with uppercase or Not if it is not Then capitalize it
# s="python"

# String ="python"
# if String[0].isupper():
#     print("Starting with upperCase")
# else:
#     String=String.capitalize()
#     print(String)

# 8.wap to check if the given number is even ,if it
# is even reduce it to its Half else make exponent (take user input)

# num= int(input("Enter the num"))
# if num%2==0:
#     print(f"it is even and half is {num/2}")
# else:
#     print(f" exponent is {num**3}")

# 9.wap to check number should be divisible by 3 and 7 (take user input)
#
# num=int(input("Enter the number"))
# if num%3==0 and num%7==0:
#     print(f"{num} is divisible by 3 and 7")
# else:
#     print("not divsible 3 and 7")

# 10.wap if the length of string is even then reverse
# else convert into upper case (take user input)

# String = input('Enter')
# if len(String)%2==0:
#     print(String[-1::-1])
# else:
#
#     print(String.upper())

# 11.wap to check a number is +ve/-ve number (take user input)

# num=int(input("Enter the num"))
#
# if num>0:
#     print(f"{num} is positive")
#
# else:
#     print(f"{num} is negative")

# 12.wap to check a data is individual or collection data type or not (take user input)
#
# data=eval(input("enter data"))
# if isinstance(data,(int,float,complex,bool)):
#     print("individual")
# else:
#     print("collection")

# 13.wap to check whether the specified character is present in
# the given string
#
# s="Python"
# ch=input("Enter the specified character")
# s="Python"
# if ch in(s):
#     print("present")
# else:
#     print("not present")
#
# # 14.wap to check the length of dictionary and length
# of dictionary is even or Not if even
# print as it is or else add a item and make it even

# D={"a":"apple","b":"ball","c":"cat"}
# if len(D)%2==0:
#     print(D)
# else:
#     D.update({"d":"dog"})
#     print(D)

# 15.wap to check the given number is greater than 5,
# if it is greater convert that number into negative number
# else print the same number

# num = int (input("enter the num"))
# if num>5:
#     print(-abs(num))
# else:
#     print(num)

# 16.wap to check the given number is smaller than 10
# ,if it is smaller find the exponent of it
# else print the number as it is

# num = int (input("enter the num"))
# if num<10:
#     print((num**3))
# else:
#     print(num)

# 17.wap to check the given number is odd, if it
# is odd divide it by 2 and print reminder and quotient
# else print it is even (take user input)

# num = int (input("enter the num"))
# if num%2==1:
#     print(f"reminder is {num%2} and quotient is {num//2}")
# else:
#     print("it is even")

# 18.wap to check if the given character is alphabets or Not ,if it is
# alphabet create a replica of it for 2 times. (take user input)

# ch =  input("enter the num")
# if ch.isalpha():
#     print(" ".join(ch*2))
# else:
#     print("not alphabet")

# 19.WAP to check whether the given number value is divisible by 6 or
# not,if it is divisible cube that number or
#    else perform left shift operation by 3 (take user input)

num = int (input("enter the num"))
if num%6==0:
    print(num**3)
else:
    print(num<<3)


