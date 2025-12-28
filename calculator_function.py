def calculator():
    num_1 = float(input("First number: "))
    num_2 = float(input("Second number: "))
    op = input("Operation (add, sub, mul, div): ")

    if op == "add":
        return num_1 + num_2
    elif op == "sub":
        return num_1 - num_2
    elif op == "mul":
        return num_1 * num_2
    elif op == "div":
        return num_1 / num_2
    else:
        return "Invalid operation"

print(calculator())















