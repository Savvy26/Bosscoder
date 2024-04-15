#Check whether the given number is Armstrong or not.
#An Armstrong number is one whose sum of digits raised to the power three equals the number itself.

n = int(input("enter a number"))
temp = n
arm = 0
while(n>0):
    ld =  n % 10
    arm += ld * ld * ld
    n //= 10
if (arm == temp):
    print("True")
else:
    print("False")