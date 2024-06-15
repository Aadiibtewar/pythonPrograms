#            GENERATOR EXAMPLES
#
# """
# wap to generate a+b,a-b,a*b,a/b by taking a and b from user
#
# def arithmetic(a,b):
#     yield a+b,a-b,a*b,a/b
#
# a=eval(input("enter first value"))
# b=eval(input("enter second value"))
#
# # print(arithmetic(a,b))                #<generator object arithmetic at 0x0000024F91D6DFC0>
# print(next(arithmetic(a,b)))              # we csn use typecast to list





# wap to generate only values which are divisible by 5
#
# l=[34,55,60,56,78,90,25,40]
# #
# def divBy5(l):
#    for i in l:
#        if i % 5 == 0:
#            yield i
#
# print(list(divBy5(l)))



#
# wap to return a iterator which is having square root of values present in the list
#
# l=[25,36,49,81,9,16]
# def sqrt(l):
#     for i in l:
#         yield int(i**(1/2))
#
# print(list(sqrt(l)))


#
#
# wap to return a iterator having tuples of word and its len pair and typecast into dictionary
#
# l=["instagram","facebook","whatsapp","meta","oracle"]
#
# def word_len(l):
#     for i in l:
#         yield i,len(i)
#
# print(dict(word_len(l)))



#
#
# wap to generate only numeric values in given list
#
# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
# #
# def num_val(l):
#     new =[]
#     for i in l:
#         if isinstance(i,(int,float,complex)):
#             new.append(i)
#         elif isinstance(i,(tuple,list)):
#             if num_val(i):
#                 new.extend(i)
#     yield new
#
# print(next(num_val(l)))
#

# wap to generate a list if it is individual data type reverse it else return as it is
#
# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
# def rev(l):
#     for i in l:
#         if isinstance(i,(int,float,complex,bool)):
#             yield eval(str(i)[::-1])
#         else:
#             yield i
# print(list(rev(l)))
#
#
# wap to generate only the string with odd length in given list
#
# l=["alexa","siri","google","cortrena"]
# def odd_len(l):
#     for i in l:
#         if len(i)%2==1:
#             yield i
# print(next(odd_len(l)))
#
#


# wap to create a list of numbers if number are even square it else cube it
# l=[2,3,4,5,6,7]
# def sq_cube(l):
#     for i in l:
#         if i%2==0:
#             yield i**2
#         else:
#             yield i**3
# print(list(sq_cube(l)))

#
#
# wap to return a list if words is of even length reverse it

#
# l=["hello","world","python","apple","google","walmart"]
# def even_len(l):
#     for i in l:
#         if len(i)%2==0:
#             yield i[::-1]
# print(list(even_len(l)))


# wap to generate the first letter of the word as key and words starting with letter as value
s="python is a programming language and programming is part of life"
#
def start_word(l):
    d={}
    s=l.split()
    for i in s:
        if i[0] in d:
            d[i[0]] +=[i]
        else:
            d[i[0]] = [i]
    yield d
print(list(start_word(s)))



# output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]
#
# """
