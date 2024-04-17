functions ---  so when we are definig/creating a function and we are returning something or say like function is returning something(output) then we call it as
print(function_name(x)) and if inside a function its not returning anything for example(printing the output) we call it as function_name(x)
 for example:                                                   |
** def evesum(n):                                               |   def evesum(n):
    for i in range(2, n+1, 2):                                  |     for i in range(2, n+1, 2):
        sum += i                                                |        sum += i
    return sum                                                  |     print(sum) **                                                       
                                                                |
here, the function is returning the sum                         |here , the function is not returning anything it just  printing the sum , like something happening inside it 
so we need its return value so for printing the return value    |not returning just working 
we do **print(evesum(n))**                                      |so we do **evesum(n)**
                                                                |
