# for ref_var in (iterable/collection):
#     statements
#
# for ref_var in range(si,ei,sv):
#     statements

# a="Good morning"
# for i in a:
#     print(i,end=" ")

# li=[1,2,5,8,5,2,55,5]
# for i in li:
#     print(i,end=" ")

# print()
#
#
# tu=(10,20,3,452,2)
# for i in tu:
#     print(i,end=" ")


# s={1,"hi","a","a",20,30,10,1}
# for i in s:
#     print(i,end=" ")

# di = {1: "raja", 2: "hi", "go": "come"}
# for i in di:                      # it will give only keys
#     print(i,end =" ")

# for i in di.values() :              # values give the values of dict
#     print(i ,end=" ")

# for i in di.items():              # it will show the key and value
#     print(i, end=" ")

a = "hello good morning"
# for i in enumerate(a):
#     print(i ,end=" ")


# for i in reversed(a):
#     print( i,end="")

l1 = [1, 32, 5, 3, 5]
l2 = ["hi", "helo", "a", 20, 50]

# for i in zip(l1,l2):
#     print(i,end=" ")

l3 = ["d", "dj", ]
# for i in zip(l1,l3):
#     print(i, end=" ")

from itertools import zip_longest

# for i in zip_longest(l1,l3):
#     print(i,end=" ")

# for i in zip_longest(l1,l3, fillvalue="missed"):
#     print(i,end=" ")

#---------------------------------------------------------------------------------

# 1
# 1.wap to print the number form 1 -20 segregate even and odd number into list

# even=[]
# odd=[]
# for i in range (21):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"odd-->{odd}\neven-->{even}")

# 2.wap to extract vowels and digits in a string
# s="hello123"
# for i in s:
#     if i in ("a","e","i","o","u") or i.isdigit():
#         print(i, end=" ")

# 3.wap to capitalize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l:
#     print(i.capitalize(),end=" ")


# 4.wap to extract only individual data types form the list

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if isinstance(i ,(int,float,complex,bool)):
#         print(i,end=" ")


# 5.wap to extract only individual data types from the list and sum all the individual data types

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# sum=0
# for i in l:
#     if isinstance(i ,(int,float,complex,bool)):
#         sum=sum+i
# print(sum)

# 6.wap to print the count of alphabets and numbers and space in the given string

# s="india got the independence in the year 1947"
# alCount=diCount=spCount=0
# for i in s:
#     if i.isalpha():
#         alCount+=1
#     elif i.isdigit():
#         diCount+=1
#     elif i.isspace():
#         spCount+=1
#
# print(f"alphabet:{alCount} digit:{diCount} spaces:{spCount}")

# 7.wap to check how many words are present in the given sentence

s = "hello world sentence"
# l=s.split()
# count=0
# for i in l:
#     if i.isalpha():
#         count+=1
#
# print(count)


# 8.wap to create a dictionary and print the characters and its Ascii value pair
# s="hello world"
# d={}
# for i in s:
#     d.update({i:ord(i)})
# print(d)

# # 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it
#
# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# d={}
# for i in names:
#     if len(i)%2==0:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
#
# print(d)

# 10.wap to print series of factorial(take user input)

# ip=int(input("enter the number: "))
# fact=1
# for i in range(5,0,-1):
#     fact*=i
# print(f"factorial of {ip} is {fact}")
#


# 11.wap to create a dictionary with element and its count pair


# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
#
# d={}
# for i in l:
#     if i in d:
#         d[i]+=1
#
#     else:
#         d[i]=1
#
# print(d)


# # 12.wap to find the length of the string without using inbuilt function
# s="Never Give Up"
# ct=0
# for i in s:
#     ct+=1
# print(ct)
#

# 13.wap to reverse a string without using inbuilt function
# x="you did it guys"
#
# res=""
# for i in (x):
#     res=i+res
# print(res,end="")


# 14.wap to print alternative character from a given string
# s="hello python"
# for i in range(0,len(s),2):
#     print(s[i],end=" ")


# # 15.wap to replace all the character with "-" if the characters occurs more than once in a string
# s="hellohai"
# for i in s:
#     if s.count(i)>1:
#        s= s.replace(i,"-")
#
# print(s)

# 16.wap to get  output:--->1234 in below question
# t=("1","2","3","4")
# s=""
# for i in t:
#     s+=i
# print(s)


# # 17.wap to Sum of numbers
# s = 'Sony12India567pvt21ltd'
# sum=0
# for i in s:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)
#

# 18.WAP to print sum of internal and external list
# l = [[1,2,3], [4,5,6], [7,8,9]]
#
# internal=external=0
# internal_list=[]
# for i in l:
#     internal = 0
#     for j in i:
#
#         internal=internal+j
#     internal_list.append(internal)
#     external+=internal
#     # print(internal,end=" ")
# print(internal_list)
# print(f"external {external}")
#


# 19. WAP to remove duplicates from the list without using inbuilt function
# d=[1,2,3,4,5,6,7,1,2,3,4]
# duplicate=[]
# nonDuplicate=[]
# for i in d:
#     if i in duplicate:
#         duplicate.append(j)
#
#
#             d.remove(j)
# print(d)

# 20.Print all the missing numbers from 1-10 in the below list
# l = [1, 2, 3, 4, 6, 7, 10]
# for i in range(1,11,1):
#     if i not in (l):
#         print(i ,end=" ")


# # 21.Reverse a list without using any built-in functions and slicing.
# l = [1, 2, 3, 4]
# l1=[]
# for i in l:
#     l1=i
# print(l1)

# 22.wap to get below out put
# o/p-->"uoy era woH iH'

# s="Hi How are you"
# res=""
# for i in (s):
#     res=i+res
# print(res)

# 23.wap to print repeated char and count the same
# s="helloword"
# # o/p{'l': 2, 'o': 2}
# d={}
# for i in s:
#     if s.count(i)>1:
#         d[i]=s.count(i)
# print(d)

# 24.wap to filter out even and odd numbers in the given string
# s="hello 123 world 456 welcome to python1234567"
# even=[]
# odd=[]
# for i in s:
#     if i.isdigit():
#         if int(i)%2==0:
#             even.append(int(i))
#         else:
#             odd.append(int(i))
# print(f"even ->{even}\n odd ->{odd}")


# 25.,wap to create a dictionary word and reverse word pair
# s="tomorrow is weekend and non-veg special"
# l=s.split()
# d={}
# for i in l:
#     d[i]=i[::-1]
# print(d)


# -------------------------------------------------
# # 1.wap to create a dictionary index and word pair
#
# s="tomorrow is weekend and non-veg special"
# d={}
# l=s.split()
# j=0
# for i in l:
#     d[j]=i
#     j+=1
# print(d)
#


# 2.wap to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"
# d={}
# for i in s.split():
#     d[i]=len(i)
# print(d)

# # 3.wap to create a dictionary characters and its corresponding upper case characters
# s="sunday"
# d={}
# for i in s:
#     d[i]=i.upper()
# print(d)

# # 4.wap to create a dictionary Ascii and character pair
# l=[89,51,111,77,108,120]
# d={}
# for i in l:
#     d[i]=chr(i)
# print(d)


# 5.wap to  create a list of characters and its Ascii value pair

# s="sunday"
# d={}
# for i in s:
#     d[i]=ord(i)
# # (d.items())
# print(d.items())


# 6.WAp to perform clear() in list without using inbuilt method

# lst= ['hai', 'hello', 'python', 'world', 'jingalala']
# for i in range(len(lst)):
#     lst.pop()
# print(lst)

# 7.wap to create a dictionary with words and its length pair and ends with vowel

# s="Today is Tuesday and attending python session"
# d={}
# for i in s.split():
#     if i[-1]in("a","e","i","o","u"):
#         d[i]=len(i)
# print(d)

# 8.wap to create a dictionary with letter and its words starting with that letter pair

# s="hi hello good morning welcome to python session"
# l=s.split()
# d={}
#
# for i in l:
#     li=[]
#     for j in l:
#         if i[0]==j[0]:
#             li.append(j)
#     d[i[0]]=li
# print(d)

# 9.wap to create a dictionary of characters and its indices pair
# s="hello python"
# d={}
# for i in range(len(s)):
#     if s[i] not in d:
#         d[s[i]]=[i]
#
#     else:
#         d[s[i]] += [i]
#
# print(d)

# 10.wap to using this list get the below output

# o/p:-->{'flower': ['sun', 'lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}
#
# l = ['sun flower', 'lily flower', 'Marigold flower', 'lion animal','tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
#
# d={}
# for i in l:
#     s=i.split()
#
#     if s[1] in d:
#         d[s[1]]+=[s[0]]
#     else:
#         d[s[1]] = [s[0]]
# print(d)


# # 11.wap to sum of same index element from
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# l3=[11,12,13,14,15]
#
# li=[]
# for i in zip(l1,l2,l3):
#     sum=0
#     for j in i:
#       sum+=j
#     li.append(sum)
#
# print(li)


# # 12.wap to pair values of both dictionary
#
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
#
# for i in zip(d.values(),p.values()):
#     print(i)

# 13.wap to group fruit name and country pair only if a fruit is even length

# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
#
# for i in zip(d.keys(),p.values()):
#     if len(i[0])%2==0:
#         print(i)
#


# 14.WAP to check whether string is ANAGRAM or not (anagrams : characters should be same it can different meaning)
# take user input


# 15.WAp to print longest word in a sentence

# s = 'life is full of surprises and miracles'

#exp o/p : surprises
# long=""
# for i in s.split():
#     if len(long)<len(i):
#         long=i
# print(long)

# # 16.Replaces whitespaces with new line char in the below string
# s = 'hello world welcome to python'
# for i in s:
#     if i.isspace():
#        s= s.replace(i,"\n")
# print(s)
#


# # 17.wap to check  whether the elements inside the list is even or odd and i want the dictionary pair
#
# l=["apple","samsung","oracle","flipkart","facebook","instagram","amazon","ebay"]
#
# d={}
# for i in l:
#     if len(i)%2==0:
#         if "even" in d:
#             d["even"]+=[i]
# #         else:
#             d["even"] = [i]
# #     else:
#         if "odd" in d:
#             d["odd"]+=[i]
#         else:
#             d["odd"] = [i]
# print(d)

# 18.wap to traverse through a string and stop the execution at specific characters by using break keyword
# specified char="d"

# s="hello guys tomorrow holiday"
#
# for i in s:
#     if i=="d":
#         break
#     print(i, end=" ")
#


# # 19.wap to print double digit numbers present in list by using continue keyword
# l=[2,3,45,67,89,11,2,3,4,5,6,7,8,11]
# for i in l:
#     if i<10:
#         continue
#     print(i, end=" ")

# # 20.wap to print only positive numbers by using continue keyword
#

# l=[1,5,-2,-45,55,88,-100,-63]
# for i in l:
#     if i<0:
#         continue
#     print(i , end=" ")
#

# # 21.wap to skip all the vowels in the given string
#
# s="good morning guys welcome to python session"
#
# for i in s:
#     if i in ("a","e","o","i","u"):
#         continue
#     print(i , end=" ")


# ------------------------------------------------------------------------


# 1.WAP to extract & store the extensions of files in a list

# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx', 'lambda.png', 'map.py', 'python.pdf', 'oops.py']
#
#
# def extract(l):
#     py =[]
#     txt =[]
#     pdf =[]
#     pptx =[]
#     png = []
#     for i in l:
#         if i.endswith(".py"):
#             py.append(i)
#         elif i.endswith("txt"):
#             txt.append(i)
#         elif i.endswith(".pdf"):
#             pdf.append(i)
#         elif i.endswith(".pptx"):
#             pptx.append(i)
#         elif i.endswith(".png"):
#             png.append(i)
#     return py, txt, pptx, pdf, png
#
#
# print(extract(l))


# 2.wp to print first and last char of each name in the list
# l = ["Sunil", "anil", "Suresh", "Mahesh", "Dinesh"]
# new=[]
#
# def fir_lst(l):
#     for i in l:
#         new.append(i[0]+i[-1])
#     return new
# print(fir_lst(l))


# 3.wp to create new list as squares of each number of below list
# l = [2, 4, 5, 1, 9, 7, 3]
#
# def sq(l):
#     new=[]
#     for i in l:
#         new.append(i**2)
#     return new
# print(sq(l))


# # 4.wp if number is even the print its square else print its cube
# l = [2, 4, 5, 1, 9, 7, 3]
# def even_sq_cube(l):
#     for i in l:
#         if i%2==0:
#             print("square ",i**2)
#         else:
#             print("cube ",i**3)
# even_sq_cube(l)

# 5.wp to create a new list of separate even number and odd number
#
# l = [2, 4, 5, 1, 9, 7, 3]
#
# def even_odd(l):
#     even = []
#     odd=[]
#     for i in l :
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#
#     return even,odd
#
# print(even_odd(l))


# 6.wp to create a new list reversing each name from the list.

# names = ["Sunil", "denga", "panga", "Harsha", "manga"]
# def revList(names):
#     new=[]
#     for i in names:
#         new.append(i[::-1])
#     return new
# print(revList(names))


# 7. WAP  to find the number of digits present in a number
# n = 123456
# s=str(n)
# def find_len(n):
#     s = str(n)
#     ct=0
#     for i in s:
#         ct+=1
#     return ct
# print(find_len(n))
#


# 8.WAP to print largest number in the list without using
#inbuilt function
#
# numbers = [10, 30, 50, 80, 15, 20, 70,25]
# def largest(num):
#     largest=num[0]
#     for i in num:
#         if largest<i:
#             largest=i
#     return largest
# print(largest(numbers))


# 9.WAP to print all numeric values in a list
# l = ['apple', 123, 'google', '45.6', 'yahoo', [1,2,3],True, (1,3,7), 6+3j]
# for i in l:
#     if type(i) in (int,complex,float):
#         print(i)



# 10.WAP to perform copy method in a list without using copy()(take user input)

# l=[2,3,5,5,8,4]
# def copy(l):
#     new=[]
#     for i in l:
#         new.append(i)
#     return new
#
# print(copy(l))

# 11.WAP to check the given number is Armstrong or not
#Armstrong : Sum of cube of the digits

# num=153
# def isArmstrong(num):
#     sum=0
#     temp=num
#
#     while(temp!=0):
#         sum+=((temp%10)**3)
#         temp=temp//10
#     if sum==num:
#         return f"{num} is armstrong number"
#     else:
#         return f"{num} is not armstrong number"
#
# print(isArmstrong(num))

# 12.WAP to check given number is perfect number or not(take user input)

#sum of its proper divisor should be equal to original value

# def isPerfect(num):
#     sum=0
#     for i in range(1,(num//2)+1,1):
#         if num%i==0:
#             sum+=i
#     if num==sum:
#         return f"{num} is perfect number"
#     else:
#         return f"{num} is not perfect number"
#
# print(isPerfect(36))

# 13.WAP to print Fibonacci numbers up to 10

# def fibo(num):
#     n1=0
#     n2=1
#     res=0
#     for i in range(0,num,1):
#         print(n1, end=" ")
#         res=n1+n2
#         n1=n2
#         n2=res
#
# fibo(10)

# 14.WAP to check given number is Automorphic or not
# automorphic means:-->square end with the integer
# 1,5,6,25,76,376,625,9376

def is_automorphic(number):
    square = number * number


    if str(square).endswith(str(number)):
        return True
    else:
        return False

numbers = [1, 5, 6, 25, 76, 376, 625, 9376]

for i in numbers:
    if is_automorphic(i):
        print(f"{i} is an automorphic number")
    else:
        print(f"{i} is not an automorphic number")


# 15. WAP to reverse each element in a list, then reverse entire list
#
# l = ['apple', 'google', 'yahoo', 'Walmart']
#
# new=[]
# for i in range(len(l)-1,-1,-1):
#     new.append(l.pop()[::-1])
#
#
# print(new)



