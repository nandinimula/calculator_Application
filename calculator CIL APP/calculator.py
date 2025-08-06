def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 
    return x / y
def percentage(x, y):
    if y == 0:
        return "Error: Cannot calculate percentage with zero denominator."
    return (x / y) * 100    

def main():
    print("Welcome to the CLI Calculator APP!")
    while True:
        try:
            x = float(input("Enter First Number: "))
            y = float(input("Enter Second Number: "))
            operation = input("Choose Cal Operation (+, -, *, /,%): ")

            if operation == '+':
                result = add(x, y)
            elif operation == '-':
                result = subtract(x, y)
            elif operation == '*':
                result = multiply(x, y)
            elif operation == '/':
                result = divide(x, y)
            elif operation == '%':
                result = percentage(x, y)
                print(f"Result: {result}%")    
            else:
                print("Invalid Cal Operation.Please try again.")
                continue

            print("Result:", result)

            cont = input("Do you want to Calculate again? (yes/no): ").lower()
            if cont != 'yes':
                print("Thanks for using the calculator APP!")
                break
        except ValueError:
            print("Invalid input, Please Enter Numeric Values.")

if __name__ == "__main__":
    main()