def calculator():
    """Provides basic calculator functionality.you can use it easily """

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")
            continue

        if choice in (1, 2, 3, 4):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == 1:
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == 2:
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == 3:
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == 4:
                try:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                except ZeroDivisionError:
                    print("Cannot divide by zero.")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()
