while True:
    print("\n--- Simple Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    try:
        choice = int(input("Enter operation (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1-5.")
        continue

    if choice == 5:
        print("Exiting...")
        break

    if 1 <= choice <= 4:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            try:
                print("Result:", num1 / num2)
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")

    else:
        print("Invalid choice! Please select an option from 1 to 5.")