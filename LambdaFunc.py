# #lambda examples// Anonymous function


# """
# 1.wap to find square and cube of given number
# x=(lambda a:(f"square is {a**2} and cube is {a**3}"))
# print(x(2))

#
# 2.wap to check the given number is palindrome or not

# x=lambda a:"palindrome" if str(a)==str(a)[::-1]else "not palindrome"
# print(x(121))



# 3.wap to convert negative number to positive number

# x=lambda a:abs(a)
# print(x(-222))



# 4.wap to return the key of a dictionary
# a={"hello":"Sony","How":"are","you":"bye"}
# l=lambda k:[print(k.keys()) for i in k]
# l(a)


# 5.wap to check if the number is even or odd

# ev_odd=lambda x: "even" if x%2==0 else "odd"
# print(ev_odd(21))

# 6.wap which returns first element of a sequence

# first=lambda l: l[0]
# print(first([1,2,2,5,4]))


# 7.wap which returns length of any iterable

# length=lambda x:sum(1 for i in x)
# print(length([1,2,10,22]))



# 8.wap which returns the list of squares of numbers in a list
# l=[2,3,4,5,6]
#
# sq=lambda s:[i**2 for i in s]
# print(sq(l))



# 9.wap to check list elements are palindrome or not
# l=["nayana","kayak","mom","school","bag","dad"]
#
# pal=lambda x:[f"{i} is palindrome" if i==i[::-1] else f"{i} not palindrome" for i in x]
# print(pal(l))
#
#


# 10.wap to print the numbers present in a list with their corresponding indices pair

# l=[100,200,300,400,500]
# indices_pair= lambda a:[i for i in enumerate(l)]
# print(indices_pair(l))


#
#
# 11.wap to check a data is sequence if it is sequence then return length pair else type pair
# l=["rajesh","ramesh","suresh","raj"]
# seq=lambda x:[(i,len(i)) if isinstance(x,(list,tuple,str)) else (i,type(i)) for i in x]
# print(seq(l))


# 12.wap to check given number is divisible by 5 and 3

# div=lambda x:f"{x} is divisible by 5 and 3" if x%5==0 or x%3==0 else f"{x} is not divisible by 5 and 3"
# print(div(15))




# 13.wap to check even or odd,if it is even return square of that value else square root of that
# value

# ev_odd=lambda x: x**2 if x%2==0 else x**0.5
# print(ev_odd(15))


# 14.wap to check len of given string ,if length is even return as it is else return reverse
# of that string

# le=lambda x:x if len(x)%2==0 else x[::-1]
# print(le("hello"))

# 15.wap to check length of given string and return value and length in tuple and dictionary
# a=lambda x:dict(x,len(x))
# print(a("rakesh"))
