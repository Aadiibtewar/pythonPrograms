#Local
# def spam():
#     s=20
#     print(s)
# spam()
# print(a)    #NameError: name 'a' is not defined


# def spam ():
#     a=10
#     print(a)
#     return a
# print(spam())

# global

# a=10
# def spam():
#     a+=100    # we have to use global keyword
#     print(a)
#
# spam()      #UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
#
# a+=100
# print(a)
#
# a=10
# def spam():
#    global a
#    a+=100
#    print(a)
# spam()
#
# a+=100
# print(a)


a = 10


def spam():
    b = 20
    print(a, "spam")

    def demo():

        print(a, "demo")
        nonlocal b
        global a
        a += 100
        b = 1000

        print(a, "modified in demo()")
        print(b, "demo")
        c = 30
        print(c)

    demo()


spam()
