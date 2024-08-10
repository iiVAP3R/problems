def main():
    # prompt the user for input
    user_num = int(input("Enter the number you'd like to calculate the factorial for: "))

    # check if the user decides to be funny
    if user_num < 0:
        print("You can't calculate the factorial of zero or a negative number")
        exit(1) # exit with status code 1


    print(factorial(user_num))


def factorial(num):
    # TODO: Implement a factorial function that utilizes recursion to calculate the factorial of a non-zero number
    # NOTE: Remember! A recursive function should always have 2 things; A base case and the recursive step

    pass


if __name__ == "__main__":
    main()