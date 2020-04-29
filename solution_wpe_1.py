# Defined the print_solutions() method
# Doesn't use the min() and max() methods, instead uses the comparison methods to assign and store values


def print_solutions():
    all_numbers = []
    smallest = None
    largest = None

    while True:
        n = input("Enter a number: ").strip()

        if not n: #if not true which means not empty, it exits
            break

        n = int(n)
        all_numbers.append(n)

        if (smallest is None or n < smallest):
            smallest = n

        if (largest is None or n > largest):
            largest = n

    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")
    print(f"Sum: {sum(all_numbers)}")
    print(f"Mean: {sum(all_numbers ) / len(all_numbers)}")

#print_solutions()
