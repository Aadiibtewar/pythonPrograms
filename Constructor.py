# class Test:
#     def __init__(self):
#         print("printing Default consructor")
#
# c=Test()#----------->calling through obj
#
# Test.__init__(c)    #-------->calling through class


# class Bank:
#     # def __init__(self):
#     #     print("No arguments")
#
#     def __init__(self,name,ifsc):
#         print(f"name of the bank is {name} and ifsc is {ifsc}")
#
#
#
# b=Bank("SBI", "SBIN000011")         #-------->parameterized constrocture
# b1=Bank("PNB","PNB00001")
#
# Bank.__init__(b,"icici","ICICI0001")




# class Account:
#     bal=0.0
#     def depo(self,amount):
#         self.bal+=amount
#
#     def ShowBal(self):
#         print(self.bal)

# o=Account()
# o.depo(100)
# print(o.bal)
# Account.bal=100
# print(o.bal)
# print(Account.bal)

# Account.depo(o,100)
# o.ShowBal()

# Account.ShowBal(o)          #200.0




# class Student:
#     def __init__(self,name,rollNo,dep):
#         self.name=name
#         self.rollNo=rollNo
#         self.dep=dep
#
#     def details(self):
#         print(f"name is {self.name} roll number is {self.rollNo} and department is {self.dep}")
#
# o=Student("raju",420,"cs")
#
# o.details()
#
# Student.__init__(o,"sham",421,'EEE')
# Student.details(o)



# method overloding
# class Over:
#     # def add(self,a,b):
#     #     print("add1 " , a+b)
#     #
#     # def add(self,a,b,c):
#     #     print("add2",a,b,c)
#
#
#     def add(self, a=0,b=0,c=0):
#         print("add3", a+b+c)
#
#     def add(self,a=0,b=0,c=0):
#         print("add4",a+b+c)
#
# o=Over()
#
# # o.add(1,2)     # TypeError: Over.add() missing 1 required positional argument: 'c'
#
# o.add(4,2)      #add4 6
# o.add(1,2,10)


#Consructor overLoding
# class Test:
#     # def __init__(self,a,b):
#     #     print("add1 " , a+b)
#     #
#     # def __init__(self,a,b,c):
#     #     print("add2",a,b,c)           gives error
#
#     def __init__(self, a=0,b=0,c=0):
#         print("add3", a+b+c)
#
#     def __init__(self,a=0,b=0,c=0):
#         print("add4",a+b+c)
#
#
# t=Test(1,2)     #add4 3

class Test:
    def __init__(self,name, age,*args):
        print(f"name is {name} and age is {age}")
        print(f"address is {args}")

o=Test("raja",20,"pune")


