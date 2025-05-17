try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero error !!")
except SyntaxError:
    print("Comma is missing. Enter numbers seperated by comma.")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")