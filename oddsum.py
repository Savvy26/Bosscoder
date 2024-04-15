#sum of first N odd natural numbers
n = int(input("Enter the number of natual odd number sum you want"))
sum = 0
for i in range (1, 2*n, 2):
    sum += i
print(sum)