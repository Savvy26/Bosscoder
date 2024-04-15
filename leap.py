#Check whether the given year is leapyear or not
a = int(input("Enter your year:"))
if(a % 400 == 0):
    print("True")
elif(a % 100 == 0):
    print("False")
elif(a % 4 == 0):
    print("True")
else:
    print("False")