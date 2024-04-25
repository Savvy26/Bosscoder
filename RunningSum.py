#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
# nums = [1,2,3,4]
#Output 1: [1,3,6,10]
#Explanation 1: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

n = int(input("enter the lenght of array"))
nums = []
for i in range (0,n):
    x = int(input(f"enter a {i} element"))
    nums.append(x)
print(nums)

output= []
x = 0
for i in range(0,n): 
    x = x + nums[i]
    output.append(x)

print(output)