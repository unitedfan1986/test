while True:

    first_number = int(input("Tell me First number: "))
    operation = input("Tell me operation: ")
    second_number = int(input("Tell me Second number: "))

    if operation == "+":
        print(f"Your answer: {first_number + second_number}")

    elif operation == "-":
        print(f"Your answer: {first_number - second_number}")

    elif operation == "/":

        if second_number == 0:
            print("Error")
        else:
            print(f"Your answer: {first_number / second_number}")

    elif operation == "*":
        print(f"Your answer: {first_number * second_number}")

    else:
        print(f"Print valid operation and number")
