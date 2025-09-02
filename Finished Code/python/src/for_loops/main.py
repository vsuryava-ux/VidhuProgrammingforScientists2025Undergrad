def main():
    print("For loops in Python.")

    print(another_factorial(10))

def another_factorial(n: int) -> int:
    """
    Factorial, but with for.
    """
    # let's ensure that n >= 0
    if n < 0:
        print("n is", n)
        raise ValueError("Error: negative input given to factorial.")
    
    product = 1 


    # for loops are always preferable IF we know how many iterations through the loop we're going to take 
    # there are other instances where we can only use while
    for i in range(1, n+1):
        # i lives only within this loop
        product *= i

    return product

if __name__ == "__main__":
    main()