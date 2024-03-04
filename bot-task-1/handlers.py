"""handlers module"""


def input_error(func):
    """decorator for exceptions"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Give me name and phone please."

    return inner


def parse_input(user_input):
    """parses commands"""
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


@input_error
def add_contact(args, contacts):
    """adds contacts in format: 'name':'phone'"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """changes contact's phone"""
    name, new_phone = args
    contacts[name] = new_phone
    return "Contact changed."


@input_error
def show_phone(args, contacts):
    """shows phone of specific name"""
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError
