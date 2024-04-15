#Reverse the given integer.
n = int(input("enter a integer:"))
rev = 0
while(n>0):
    ld = n % 10
    rev = rev*10 + ld
    n //= 10
print(rev)
