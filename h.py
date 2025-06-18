from utils import add, subtract, multiply, divide
def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Add: {add(a, b)}")
    print(f"Subtract: {subtract(a, b)}")
    print(f"Multiply: {multiply(a, b)}")
    print(f"Divide: {divide(a, b)}")
if __name__ == "__main__":
    main()
