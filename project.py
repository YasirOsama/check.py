sum = 0
while True:
    user_input = input("Enter the price & press q to quit:\n")
    if user_input != 'q':
        sum = sum + int(user_input)
        print(f"Your current bill is: {sum}")
    else:
        print("Thank you! Exiting now.")
        break
