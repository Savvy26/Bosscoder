#Write a program to print Fibonacci series of n terms where n is input by user -->> 0 1 1 2 3 5 8 13 21 ....

#Fibonacci series in which each number is the sum of the two preceding ones.
def fibonacci(n):
        last_digit = 1
        second_last_digit = 0
    # as we know fibonacci number starts with  0 , 1 and goes on so we stored that values in variable and print it/    
        
        print(second_last_digit)
        print(last_digit)

    # now as 0,1 is already printed which means 2 term is already printed so we starts from 2 and why "n" not "n+1"
    # because suppose we need to check for n = 4 , so it will give 4 outputs and 2 outputs are already there so we need 
    # 2 more therefore n so it will work for 2 iteration only if we take n+1(what we usually do in python)
    #it will go for 2,3,4 and we already have 2 terms beore hand which make make 5 term thats why "n"
        for i in range (2, n):
            next_term = second_last_digit + last_digit

        # here we are makeing(a,b = b,c) so now b and c will become second_last_digit and last_digit
            second_last_digit, last_digit = last_digit, next_term
            
            print(next_term)

n = int(input("enter the number"))
fibonacci(n)