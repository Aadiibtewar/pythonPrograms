# class Student:
#     name="raj"
#     age=22
#     phoneNo=9876543210
#     address="pune"
#By using Class name
# print(f"My name is {Student.name} age is {Student.age} living at {Student.address} and Phone number is {Student.phoneNo}")

# By using Object
# s=Student()
# print(f"My name is {s.name} age is {s.age} living at {s.address} and Phone number is {s.phoneNo}")


# print(Student)  #<class '__main__.Student'>
# print(s)            #<__main__.Student object at 0x0000011A7EB78110>

# print(Student.__dict__)         # data present in key and value a
# {'__module__': '__main__', 'name': 'raj', 'age': 22, 'phoneNo': 9876543210, 'address': 'pune', '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}


# help(Student) # it will give details about the class ----->Data descriptors defined here:

# print(id(Student))  #2335494104112
# print(id(s))        #2335492768448
# print(id(s.name))   #2511292338928

# s1=Student()
# print(Student.name) #raj
# print(s.name)       #raj
# print(s1.name)      #raj   All values are same at begining


# After modification in main Class
# Student.name="Taj"
# print(Student.name) #Taj
# print(s.name)       #Taj
# print(s1.name)      #Taj   All values are modified

# modification in object
# s.name="ravi"

# print(Student.name) #Taj
# print(s.name)       #Ravi  value only change in that obj not in other obj
# print(s1.name)      #Taj

# after modify in class variable
# Student.name="Surya"
# print(Student.name) #Surya
# print(s.name)       #Ravi  here it won't affect to this object
# print(s1.name)      #Surya
# if we modify any object it will act as independent obj





# ---------------------------------------------------------------------------------------------------------------------


# class Demo:
#     def greet(self):
#         print("good day")
#         print(self)        # <__main__.Demo object at 0x000002463AF03A40>
#         # 1808581081664
#
# d=Demo()
# d.greet()       #good day
#
# print(d)                        #<__main__.Demo object at 0x000002463AF03A40>
# #self and the object address is same self which store the obj reff
#
#
# # Demo.greet()    #TypeError: Demo.greet() missing 1 required positional argument: 'self'
# # Demo.greet(d)       #good day--------------> whenever we use class name as reffernce we need to give object explicitly


# -----------------------------------------------------------------------------------------
# instance method with argument
# class Test:
#
#     def info(self,name,sal):
#         print(f"Name is {name} and salary is {sal}")

# t=Test()
# t.info("raj",5000)          #Name is raj and salary is 5000

# Test.info("karan",50000)        #TypeError: Test.info() missing 1 required positional argument: 'sal'
# we need to pass object name while calling with class name
# Test.info(t,"karan",50000)      #Name is karan and salary is 50000

#-----------------------------------------------------------------------------------

#class variable inside the instance method

# class Flipkart:
#     product = "watch"
#     price=5000
#     address="pune"
#
#     def order(self):
#         # print(f"the product is {product} price is {price} and deliver to {address}" )          #NameError: name 'product' is not defined. Did you mean: 'self.product'?
#         print(f"the product is {self.product} price is {self.price} and deliver to {self.address}" )        #the product is watch price is 5000 and deliver to pune
#
#
#     def loc(self):
#         print(f"location is {Flipkart.address}")        #location is pune
# #         we can use class name also
# fkart=Flipkart()
# fkart.order()
# fkart.loc()

#-------------------------------------------------------------------------------------

# class Emp:
#     name="virat"
#     age="30"
#     address="Pune"
#
#     def info(self):
#         print(f"name is {self.name} address is {self.address} and age is {self.age}" )
#
#     def loc(self):
#         print(f"the location is {Emp.address}")
#
#
# a=Emp()
#
# # a.info()
# # a.loc()
#
# a.name="raja"
# a.info()
# print(Emp.name)         #virat      ---> change is only done in object not in class
# Emp.info(a)

#----------------------------------------------------------------------------------------

class Sub:
    name= "ganesh"
    sub="python"
    time="2 month"


