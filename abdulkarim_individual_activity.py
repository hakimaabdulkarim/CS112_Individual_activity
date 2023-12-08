def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            break

user_input = int(input("Enter an integer >= 2: "))
find_smallest_factor(user_input)