
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, my name is", self.name, "and I'm", self.age, "years old.")
 

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1.name)  # Output: Alice
print(p2.age)   # Output: 25


p1.introduce()  # Output: Hi, my name is Alice and I'm 30 years old.
p2.introduce()  # Output: Hi, my name is Bob and I'm 25 years old.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print("Length:", rect.length)
print("Width:", rect.width)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())





class laptop():
    def __init__(self,laptop_company,laptop_ram,laptop_pro,laptop_price):
        self.a=laptop_company
        self.n=laptop_ram
        self.f=laptop_pro
        self.v=laptop_price
    def laptop_details(self):
        print("Laptop Company:",self.a)
        print("Laptop Ram:",self.n)
        print("Laptop Processor:",self.f)
        print("Laptop Price:",self.v)
while True:
    lpc=input("Enter the Laptop Company:")
    lpr=input("Enter the Laptop Ram:")
    lpp=input("Enter the Laptop Processor:")
    lp=input("Enter the Laptop Price:")
    laptop_obj=laptop(lpc,lpr,lpp,lp)
    laptop_obj.laptop_details()



















# class rajesh():
#     print("this is class")

# suresh=rajesh() # object creation

# class rajesh():
#     def display(self):
#         print("this is class")
# suresh=rajesh() # object creation
# suresh.display()




# class Ghopi(): # class defination
#     a=13535 # attribute
#     def func(self): # method
#         print("this is function",self.a)
# # object name=Classname
# obj=Ghopi()
# obj.func() # objectname.method
# print(obj.a) # objectname.attribute






# class saikiran():
#     ff=1
#     def sai_fun(self):
#         print("hii",self.ff)
# sai_obj=saikiran()
# sai_obj.sai_fun()










# # class vasu():
# #     def vasuu(self):
# #         print("bye")
# # v=vasu() # obj 1
# # v1=vasu() # obj2

# # v.vasuu()
# # v1.vasuu()







# # class vijay():
# #     def vi(self):
# #         print('ooo')
# # v=vijay()
# # while True:
# #     v.vi()







# # a=10
# # b=20
# # c=30
# # d=40
# # e=6
# # f=4
# # j=6
# # g=77
# # def aa():
# #     print(a)
# # aa()
# # def bb():
# #     print(b)
# # bb()




# # class raj():
# #     def __init__(self,a,b,c,d,e,f):
# #         self.aa=a
# #         self.bb=b
# #         self.cc=c
# #         self.dd=d 
# #         self.ee=e
# #         self.ff=f
# #     def Output(self):
# #         print(self.aa)
# # r=raj(1,2,3,4,5,6)
# # r.Output()















# class laptop():
#     def __init__(self,laptop_company,laptop_ram,laptop_pro,laptop_price):
#         self.a=laptop_company
#         self.n=laptop_ram
#         self.f=laptop_pro
#         self.v=laptop_price
#     def laptop_details(self):
#         print("Laptop Company:",self.a)
#         print("Laptop Ram:",self.n)
#         print("Laptop Processor:",self.f)
#         print("Laptop Price:",self.v)
# while True:
#     lpc=input("Enter the Laptop Company:")
#     lpr=input("Enter the Laptop Ram:")
#     lpp=input("Enter the Laptop Processor:")
#     lp=input("Enter the Laptop Price:")
#     laptop_obj=laptop(lpc,lpr,lpp,lp)
#     laptop_obj.laptop_details()



























# # class Mobiles():
# #     def __init__(self,mobile_name,mobile_model,mobile_ram,mobile_price):
# #         self.a=mobile_name
# #         self.b=mobile_model
# #         self.c=mobile_ram
# #         self.d=mobile_price
# #     def Mobile_details(self):
# #         print("Mobile Name:",self.a)
# #         print("Mobile Model:",self.b)
# #         print("Mobile Ram:",self.c)
# #         print("Mobile Price:",self.d)
# # mn=input("Enter the Mobile Name:")
# # mm=input("Enter the Mobile Model:")
# # mr=input("Enter the Mobile Ram:")
# # mp=input("Enter the Mobile Price:")
# # mobile_obj=Mobiles(mn,mm,mr,mp)
# # mobile_obj.Mobile_details()
# # mobile_obj.Test()