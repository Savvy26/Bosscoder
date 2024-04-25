#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#Specifically, ans is the concatenation of two nums arrays.
#Return the array ans.
n = int(input("enter the size of array"))
arr=[]
#arr2 = []

for i in range(0,n):
    x = int(input(f"enter the {i} element"))
    arr.append(x)
print(arr)

#arr2[:] =arr 
arr += arr
print(arr)

