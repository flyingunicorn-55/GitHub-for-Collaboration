def fibonacci(n):
    """Recursive function to return the n-th Fibonacci number."""
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Main function to execute the Fibonacci sequence program."""
    print("Welcome to the Fibonacci Sequence Program!")

    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms to generate: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print("Fibonacci sequence:")
    for i in range(1, n + 1):
        print(fibonacci(i), end=" ")
    print()

if __name__ == "__main__":
    main()
