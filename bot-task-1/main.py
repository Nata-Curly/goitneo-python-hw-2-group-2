"""module with functions for parsing commands and adding contacts"""
from handlers import add_contact, parse_input, show_phone, change_contact


def main():
    """function for starting and/or stopping bot-app"""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
