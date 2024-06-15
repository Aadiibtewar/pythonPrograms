a=10


# try:
#     print(a/0)
# except Exception:       #defualt exception
#     print("error occured")
#

# try:
#     print(a/0)
# except ZeroDivisionError:       #specific execept block
#     print("can't divide by zero")

# try:
#     print(a / 0)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("value is not present")
# except KeyError:
#     print("key is not present")

a=[1,5,6,3,6,6,8]

try:
    print(a[22])
except (NameError,KeyError,ZeroDivisionError,IndexError):
    print("error occuerd")

# a=[1,5,6,3,6,6,8]
# try:
#     print(a.index(2))
# except Exception as err:    #generic except block
#     print(err)

