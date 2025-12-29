'''num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))
add = num1+num2
sub = num1-num2
multi = num1*num2 
div = num1/num2 
mod = num1%num2
expo = num1**num2
print("Sum of num1 and num2 is : ",add)
print("Subtraction of num1 and num2 is : ",sub)
print("Multiplication of num1 and num2 : ", multi)
print("Division of num1 and num2 : ",div)
print("Modules of num1 and num2 : ",mod)
print("Exponent value of num1 and num2 : ",expo)'''


years = int(input("Enter a year "))
if( years % 400 == 0 ) or (years % 4 and years % 100 != 0 ):
    print("It is a leap year ")

else:
    print("It is a ordinary year ")