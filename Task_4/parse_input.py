
# def parse_input(user_input):
#     cmd, *args = user_input.split()
#     cmd = cmd.strip().lower()
#     return cmd, *args


# def add_username_phone(args, contacts):
#     username, phone = args
#     contacts[username] = phone
#     return "Contact added."

# def change_contact(args, contacts):
#     username, phone = args
#     contacts[username] = phone
#     return "Contact changed."


# def main():
#     contacts = {}
#     print("Welcome to the assistant bot!")
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)

#         if command in ["close", "exit"]:
#             print("Good bye!")
#             print(contacts)
#             break
#         elif command == "hello":
#             print("How can I help you?")
#         elif command == "add":
#             print(add_username_phone(args, contacts))
#         elif command == "change":
#             print(change_contact(args, contacts))
#         elif command == "phone":
#             print(f"{contacts.values()}")
#         elif command == "all":
#             print(contacts)
#         else:
#             print("Invalid command.")

# if __name__ == "__main__":
#     main()

