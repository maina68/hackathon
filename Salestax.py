pywallSpace = int(input("Enter wall space in square feet: "))
paintPrice = float(input("Enter paint price per gallon: "))
val = (pywallSpace//115)

paintCharge = val*paintPrice
laborCharge = val*20*8

print("The number of gallons of paint required: %d" %val)
print("The hours of labor required : %d" %(val*8))
print("The cost of the paint:$%.2f" %paintCharge)
print("The Labor charges:$%.2f" %laborCharge)
print("The total cost of paint job :$%.2f" %(paintCharge + laborCharge))