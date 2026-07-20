def get_number(message):
    while True:
        try:
            value = input(message).strip()

            if value == "":
                raise ValueError("Input cannot be empty.")

            return float(value)

        except ValueError:
            print("Invalid input! Please enter an integer or a float.")


def compare_numbers(first_number, second_number):
    if first_number > second_number:
        print("The first number is greater than the second number.")
    elif first_number < second_number:
        print("The first number is less than the second number.")
    else:
        print("Both numbers are equal.")


def main():
    print("=== Comparison Number ===")

    number1 = get_number("Enter number 1: ")
    number2 = get_number("Enter number 2: ")

    compare_numbers(number1, number2)


if __name__ == "__main__":
    main()
