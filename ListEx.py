class ListEx:
    def li(self,li):

            if isinstance(li[1],str):
                li[1]=li[1][::-1]
                return li
            elif isinstance(li[1],int):
                data=eval(input("Enter value"))
                li[1].append(data)
                return li
            else:
                li[::-1]

d=ListEx()
print(d.li([1,"Raja",3]))