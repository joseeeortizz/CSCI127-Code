nums = [1, 4, 10, 6, 5, 42, 9, 8, 12]
maxNum = 0
for n in nums:
    if n > maxNum:
       maxNum = n
print(maxNum)

############################

def ask_number():
    while True:
        number = int(input("Please enter a number between 2001 and 2021: "))
        if 2001 <= number <= 2021:
            return number
        else:
            print("The number is not valid. Please enter a number between 2001 and 2021.")

# Test the function
result = ask_number()
print(f"The valid number is: {result}")