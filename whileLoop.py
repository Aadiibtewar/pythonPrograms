# # wap to print table
# num = int(input("enter the number"))
# i=1
# while i<=10:
#     print(f"{num} x {i} --------> {num*i}")
#     i+=1

# # wap to print 1 to 10
#
# num= 1
# while num<=10:
#     print(num)
#     num+=1

# # wap to print 10to 1
# num=10
# while num>=1:
#     print(num)
#     num-=1

# fetch the list
# a=["hello",[1,2,3],11,3+5j]
# i=0
# while i<len(a):
#     if isinstance(a[i],list):
#      print(a[i])
#     i+=1

# # wap to print char and the position of the given string
# a="hello guys good morning"
# i=0
# while i<len(a):
#     print (f"postion: {i} and character :{a[i]}")
#     i+=1
#

# # print natural numbers
# i =1
# while i<=20:
#     print(i,end=" ")
#     i+=1

# # print upper char
# i=ord("A")
# while i<=ord("Z"):
#     print(chr(i), end=" ")
#     i+=1

# # print lower  char
# i=ord("a")
# while i<=ord("z"):
#     print(chr(i),end=" ")
#     i+=1

# # printing the both upper and lower
# i=ord("A")
# j=ord("a")
# while i<=ord("Z"):
#     print(chr(i),chr(j), end=" ")
#     i+=1
#     j+=1
#

# # wap to print even num till 20 reverse
# i=20
# while i>=0:
#     if i%2==0:
#         print(i, end=" ")
#     i-=1
#

# # 6.wap to count numbers of occurrence of specified elements in the collection
# ch=input("enter the character")
#
# s = 'Hello guys Good morning python is a programming language'
# i=0
# count=0
#
# while i<len(s):
#     if ch==s[i]:
#         count+=1
#     i =i+ 1
# print(ch,count)




# # 7.wap to print even positional characters in the given string
# s="hello world"
# i=0;
# while i<len(s):
#     if i%2==0:
#         print(s[i],end=" ")
#     i+=1


# 8.wap to display the position of the substring
#
s = 'Hello guys Good morning python is a programming language'
substr=input("enter the substr :")
i=0
while i<len(s):
    if substr == s[i]:
        print(s.index(substr))
    i+=1



# #9.wap to print the number Table by using data given by user (take user input)
#
# num=int(input("enter the num"))
# i=1
# while i<=10:
#     print(f"{num}*{i}={num*i}",end=" ")
#     i+=1
#
#

# #10.wap to print the names only if the length of the names is even
# l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]
#
# i=0
# while i<len(l):
#     if len(l[i])%2==0:
#         print(l[i])
#     i+=1

# #11.wap to print the elements which in tuple, print only the if it is collection data types
# values=(10,2.5,[10,20],"hero", True,(3,4,5),{2,7},{90:"super"})
# i=0
# while i<len(values):
#     if type(values[i]) in(tuple,str,dict,set,list):
#         print(values[i])
#     i+=1
#

# #12.wap to print the name which is starting with vowel in the given list
# names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
# i=0;
# while i<len(names):
#     if names[i][0]in ("a","e","i","o","u"):
#         print(names[i])
#     i+=1

# #13.wap to print sum of numbers in the list
# l=[2,4,6,7,8,9]
# i=0;
# sum=0
# while i<len(l):
#     sum=sum+l[i]
#     i+=1
# print(sum)

# #14.wap to extract only vowels and digits from the given string
# s="hellopython123"
# i=0
# while i<len(s):
#     if s[i] in("a","e","i","o","u") or s[i].isdigit():
#         print(s[i],end=" ")
#     i+=1


# #15.wap to iterate inside the list check if it is having nested list if yes merge it
#
# list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
# i=0
# while i<len(list1):
#     if type(list1[i])==list:
#         # popItem=list1.pop(i)
#         list1=list1+list1.pop(i)
#     i+=1
#
# print(list1)

# # 16.wap if a names ends with vowels then reverse a names else print its length
# names=["Kumar","Lakita","Umesh a","Priyanka"]
#
# i=0
# while i<len(names):
#     if names[i][-1]in("a","e","i","o","u"):
#         print(names[i])
#     i+=1


# # 17.wap to print all individual data type from list
#
# data=[34,"hai",3+4j,(1,2),{3,4},False,3.4]
# i=0
#
# while i<len(data):
#     if type(data[i] in (int,float,complex,bool)):
#         print(data[i])
#     i+=1

# 18.wap to print each characters from a string

# s="python masters"
# i=0
# while i<len(s):
#     print(s[i],end=" ")
#     i+=1
