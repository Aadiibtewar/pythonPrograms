
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

di={1:"raja", 2:"hi" ,"go":"come" }
# for i in di:                      # it will give only keys
#     print(i,end =" ")

# for i in di.values() :              # values give the values of dict
#     print(i ,end=" ")

# for i in di.items():              # it will show the key and value
#     print(i, end=" ")

a= "hello good morning"
# for i in enumerate(a):
#     print(i ,end=" ")


# for i in reversed(a):
#     print( i,end="")

l1=[1,32,5,3,5]
l2=["hi","helo","a",20,50]

# for i in zip(l1,l2):
#     print(i,end=" ")

l3=["d","dj",]
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

s="hello world sentence"
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

