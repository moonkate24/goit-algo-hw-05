def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Enter user name."
            elif isinstance(e, ValueError):
                return "Give me name and phone please."
            elif isinstance(e, IndexError):
                return "Enter the argument for the command."
    return inner

@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts saved."

def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ").lower()
        if user_input == "exit" or user_input == "close":
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        else:
            command, *args = parse_input(user_input)
            try:
                if command == "add":
                    message = add_contact(contacts, *args)
                    print(message)
                elif command == "change":
                    message = change_contact(contacts, *args)
                    print(message)
                elif command == "phone":
                    message = show_phone(contacts, *args)
                    print(message)
                elif command == "all":
                    message = show_all(contacts)
                    print(message)
                else:
                    print("Invalid command. Please try again.")
            except Exception as e:
                print(f"Error: {str(e)}")

def parse_input(user_input):
    return user_input.split()

if __name__ == "__main__":
    main()