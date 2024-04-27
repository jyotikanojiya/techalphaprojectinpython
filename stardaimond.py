def print_diamond(n):
    # Print upper half of diamond
    for i in range(n):
        print(" " * (n - i-1) +  "*" * (2 * i - 1 ) )
    # Print lower half of diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i-1) + "*" * (2 * i - 1))


n = int(input("enter the number"))
print_diamond(n)
