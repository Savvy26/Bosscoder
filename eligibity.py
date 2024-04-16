#Write a function that takes in a number as age (an integer) and returns whether that user is eligible for driving. (Assume if the user's age is greater than or equal to 18 years, then the user is eligible for driving otherwise not).
n = int(input("enter tyhe age of driver: "))
def eligibility(n):
    if(n >= 18):
        return True
    else:
        return False
    
print(eligibility(n))