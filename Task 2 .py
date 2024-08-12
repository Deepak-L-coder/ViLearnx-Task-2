def calculator():
  while True:
    num1 =float(input("Enter the first number: "))
    num2 =float(input("Enter the second number: "))
    operator =input("Enter operator (+, -, *, /): ")

    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      if num2 == 0:
        print("Error: Division by zero")
      else:
        result = num1/num2
    else:
      print("Invalid operator")
      continue

    print("Result:", result)

    choice =input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower() != "yes":
      break

if __name__ == "__main__":
  calculator()
