#Given an integer x, return true if x is a palindrome , and false otherwise
num = int(input("Enter a number"))
temp = num #storing the value of num in temp so that we can compare the result with temp
rev = 0    # this will store the number after reverse
while(num>0):
#we are running the loop till num become 0
    ld = num % 10  #In ld we are storing the last digit of number by dividing the orginal wth 10
    rev = rev * 10 + ld
    num //= 10  # value of num is also decresring with each itration  means num is getting divided by 10 
if(rev == temp):
    print("true")
else:
    print("false")