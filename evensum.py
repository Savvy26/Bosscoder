#Write a function to find sum of all even numbers from 1 to N.
n = int(input("Enter your number : "))
def evesum(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += i
    return sum
    
print(evesum(n))

