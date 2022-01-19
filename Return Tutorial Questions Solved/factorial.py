# defining the function
def factorial(num):

    # initializing factorial variable
    fact = 1

    # running loop from 1 to n
    for i in range(1, num+1):

        # calculating
        fact *= i
    
    # returning the factorial
    return fact

# Taking input
n = int(input("Enter an integer: "))

# Print the factorial
print("Factorial of ", n, "is: ", factorial(n))