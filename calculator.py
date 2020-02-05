def main():
	firstNumber = input("Enter the first number:  ")
	secondNumber = input("Enter the second number: ")
	operation = input("Choose the operation (+, -, /, *):")
	try:
		firstNumber = int(firstNumber)
		secondNumber = int(secondNumber)
	except ValueError as err:
		print("The numbers you entered were invalid, please try again later")

	else:
		if operation == "*":
			print(firstNumber * secondNumber)
		elif operation == "+":
			print(firstNumber + secondNumber)
		elif operation == "-":
				print(firstNumber - secondNumber)
		elif operation == "/":
			print(firstNumber / secondNumber)
		else :
			print("operation is not valid")

if __name__ == '__main__':
	main()
