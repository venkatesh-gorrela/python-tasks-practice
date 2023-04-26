#control statements
  # if statement
age=int(input("enter age: "))
if   age >= 18:
    print("eligible for vote")
else:
    print("not eligible for vote")
  #if elif else statement
score = int(input("enter score: "))
if score >= 90:
    grade = 'A'
    print("very very good")
elif score >= 80:
    grade = 'B'
    print("very good")
elif score >= 70:
    grade = 'C'
    print(" good")
elif score >= 35:
     grade = 'D'
     print("just pass")
else:
    grade = 'f' 
    print("fail")
print("Your grade is:",grade )
#nested if statement
a=10 
b=20
if a > b:
    print("right a > b:")
    if a == b:
        print("equal")
else:
    print("wrong")























