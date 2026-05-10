# Basic try-except-else-finally
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
