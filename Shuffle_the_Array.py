#Given the array nums consisting of n(n will be even) elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].
def shuffle():
    n = int(input("enter the lenght of array"))
    if(n%2 != 0):
        print ("please fill even no")
        exit
    else:
        nums = []
        for i in range(0,n):
            x = int(input(f"enter a {i} element"))
            nums.append(x)
        print(nums)

        arr = []
        i = 0
        j= n//2
        while(j<n):
            arr.append(nums[i])
            arr.append(nums[j])
            i+= 1
            j+= 1
        
        print(arr)

shuffle()
      