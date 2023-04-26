# practice operators 
arth_a = int(input("enter the value: "))
arth_b = int(input("enter the value: "))
# arithmetic operators
add = arth_a + arth_b
print("addition a+b = ", add)

sub = arth_a - arth_b
print("subtraction a-b = ", sub)

mul = arth_a * arth_b
print("multiple a*b = ", mul)

divide = arth_a / arth_b
print("divide a/b = ", divide)

modulus = arth_a % arth_b
print("remainder a%j = ", modulus)

floor_division = arth_a // arth_b
print("floor division a//b = ", floor_division)

poower = arth_a ** arth_b
print("power a**b = ", poower)
print("---------------------------")
#relational operators or comparison operators
great = arth_a > arth_b
print("greater than a<b = ", great)

less = arth_a < arth_b
print("less than a<b = ", less)

less_equ = arth_a <= arth_b
print(" a<=b = ",less_equ )

great_equ = arth_a >= arth_b
print(" a>=b = ",great_equ )



equa_to = arth_a == arth_b
print(" a==b = ",equa_to )

not_equa_to = arth_a != arth_b
print(" a!=b = ",not_equa_to )
print("---------------------------")
#assignment operators
# Add and assign operator
arth_a += arth_b
print("add", arth_a)  
# Subtract and assign operator
arth_a  -= arth_b
print("sub", arth_a)  
# Multiply and assign operator
arth_a  *= arth_b
print("mul" ,arth_a)  
# Divide and assign operator
arth_a /= arth_b
print("divide",arth_a)  
# Floor division and assign operator
arth_a //= arth_b
print("floor",arth_a)  
# Modulo and assign operator
arth_a  %= arth_b
print("modulo",arth_a)  
# Exponentiation and assign operator
arth_a  **= arth_b
print("expon",arth_a)  
print("---------------------------")
#logical operators
a = arth_a
b = arth_b
c = arth_a
#logical and 
print(a > b and a < b) 
print(a > c and a < c) 
# logical or
print(a > b or a < b) 
print(a > c or a < c) 
# logical not
print(a != b)
print(a != c)
print("----------end-----------------")
