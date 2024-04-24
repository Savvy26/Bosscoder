#WAP to take size and integral inputs from user. Find the maximum and minimum from the elements.
def find_max_min():
    n = int(input("enter the size for your array"))
    arr=[]
    for i in range(0,n):
        x= int(input(f"enter {i} the element"))
        arr.append(x)
    max = arr[0]
    min= arr[0]

    for i in range(0,n):
        if(arr[i] > max):
            max = arr[i]
        if(arr[i] < min):
            min = arr[i]

    print(f"the max value elemet is {max}")
    print(f"the min value element is {min}")

find_max_min()