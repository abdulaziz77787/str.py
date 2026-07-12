phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"
}
user_input = input("Enter the phone number: ")
if len(user_input) != 10 or not user_input.isdigit():
    print("This is invalid number")
elif user_input in phone_book:
    print(f"The owner is: {phone_book[user_input]}")
else:
    print("Sorry, the number is not found")
