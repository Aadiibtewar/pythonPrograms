# class Sample:
#     def test(self):
#         print("hello")
#
# s=Sample()
# s.test()



# Class methods-------------------
# Any method decorate with @classmethod is called as class method

# class Test:
#     @classmethod
#     def demo(cls):
#         print("calling from class method")
#         print(cls)              #<class '__main__.Test'> pointing to main class
#         # print(self)                #<class '__main__.Test'>
#
# t=Test()
# t.demo()
# print(t)                        #<__main__.Test object at 0x000001A9AC103A40> pointing to main class address


# ---------------------------------------------------------------------

# class ExamDate:
#     date="1/2/2024"
#     print(date)
#     @classmethod
#     def acb_exam(cls):
#         # print(f"the exam of acb college is on {cls.date}")      #the exam of Coep college is on 1/2/2024
#         # print(cls.date)
#         if cls.date==e.date:
#             print("both are equals")
#             print(cls.date)
#             print(e.date)
#
#     @classmethod
#     def Coep_exam(cls):
#         # print(f"the exam of Coep college is on {cls.date}")     #the exam of Coep college is on 1/2/2024
#         # print(e.date)                                           #1/2/2024
#         # print(f"the exam of Coep college is on {e.date}")       #the exam of Coep college is on 2-2-24 --> changed in the obj not in cls
#         cls.date="1-1-24"
#
#
#
# e=ExamDate()
# # e.acb_exam()
# # e.Coep_exam()       #1/2/2024
# e.date="2-2-24"
# e.acb_exam()        #1-1-24
# # e.Coep_exam()       #2-2-24
#
# --------------------------------------------------------------------------------------------------------------------




# class Gym:
#     treadMill=20
#
#     @classmethod
#     def men(cls):
#         print(f"men workout is {cls.treadMill} km")
#
#     @staticmethod
#     def women(a):
#         print(f"women workout is {a} km")
#
# c=Gym()
# c.men()                         #men workout is 20 km
# c.women(30)                     #women workout is 30 km
# c.women(c.treadMill)            #women workout is 20 km

'''
1.creat a class as bank and declare all the bank name, bank address, ifsc code , phn no as class variable and creat a
class method and print allthe bank general details for the customer

2.wap that define a class called book , the book class should have the following 
title,author,year all in string
it should also have a class attribute books which is list of all books object that have been created

3.wap that define a class called Vehicle, the vehcle class should have the follwing attributes
car name, model, and year all which are string 
it should also have class attribute count which keeps track of the number of vehicle obj that have been created 
'''

'''

class Bank:
    bank_name = "Laxmi Cheat Fund"
    bank_address = "Deccan"
    ifsc_code = "LCF00000101"
    phone_number = "9876543210"


    def detail(self):
        print(f"Bank Name: {self.bank_name}")
        print(f"Bank Address: {self.bank_address}")
        print(f"IFSC Code: {self.ifsc_code}")
        print(f"Phone Number: {self.phone_number}")



b=Bank()

b1=Bank()

b1.detail()
b1.bank_name="PNB"
b1.bank_address="Warje , Pune"
b1.ifsc_code="PNB00010"
b1.phone_number="9988776655"
b1.detail()


b2=Bank()
b2.bank_name="ICICI"
b2.bank_address="PMC , Pune"
b2.ifsc_code="IC00010"
b2.phone_number="8888776655"
b2.detail()

'''


class Book:
    title=""
    author=""
    year=""
    books=[]

    @classmethod
    def addBooks(cls,title,author,year):
        cls.title=title
        cls.author=author
        cls.year=year
        cls.books.append(cls)

    @classmethod
    def showBook(cls):
        for i in cls.books:
            print(f"title: {cls.title} author:{cls.author} year:{cls.year}")

b=Book()
# b.addBooks()
# b.showBook()

book_2=Book()
book_2.addBooks("automic habit","James Clear","2018")
Book.showBook()


book_3=Book()
book_3.addBooks("Harry Potter","J.K. Rowling","1997")
Book.showBook()
#







# 3.wap that define a class called Vehicle, the vehcle class should have the follwing attributes
# car name, model, and year all which are string
# it should also have class attribute count which keeps track of the number of vehicle obj that have been created

# class Vehicle:
#     carName=""
#     model=""
#     year=""
#     count=0
#     @classmethod
#     def addVehicle(cls,carName,model,year):
#         cls.carName=carName
#         cls.model=model
#         cls.year=year
#         cls.count+=1
#
#
#
#     @staticmethod
#     def countVehicle():
#         print(v.count)
# v=Vehicle()
# v.addVehicle("Mahindra XUV700", "AX7", "2023")
# # v.countVehicle()
#
# v2=Vehicle()
# v2.addVehicle("Maruti Suzuki Swift", "LXi", "2023")
# Vehicle.countVehicle()
#
