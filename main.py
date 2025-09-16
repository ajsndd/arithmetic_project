from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


def main():
    print("=== Arithmetic Operations ===")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Sum: {add(a, b)}")
    print(f"Difference: {subtract(a, b)}")
    print(f"Product: {multiply(a, b)}")
    print(f"Quotient: {divide(a, b)}")


if __name__ == "__main__":
    main()
