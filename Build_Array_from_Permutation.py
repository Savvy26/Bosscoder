#Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

#A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
def permutation():
    nums = []
    n = int(input("enter the lenght of array"))
    for i in range (0,n):
        i = int(input(f"enter the {i} element"))
        nums.append(i)

    print(nums)

    output = []
    a = len(nums)
    for i in range(0,a):
        output.append(nums[nums[i]])
    print(output)


permutation()