# input given by user 
p = int(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period in years: "))

# compound interest formula principal p, rate r,time t
ci= p * ((1 + (r / 100)) ** t - 1)

#  compound interest
print("Compound interest = ", ci)