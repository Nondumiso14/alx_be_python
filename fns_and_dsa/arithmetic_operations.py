def perform_operation (num1, num2, operation):
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2
    if num2 == 0:
        return "Division by zero is not allowed"
    else:
        return division
    print(result)
    

result = perform_operation(4, 2, "add")
print(f"Result: {result}")




    

    




