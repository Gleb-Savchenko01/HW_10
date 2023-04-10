from collections import UserDict

class AddressBook(UserDict):
    pass


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def __str__(self):
        return f"{', '.join(self.phones)}"


class Field:
    def __init__(self, value):
        self.value = value

    def set_value(self, new_value):
        self.value = new_value


class Name(Field):
    pass


class Phone(Field):
    pass


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid command format"
        except IndexError:
            return "Invalid command format"
    return wrapper


@input_error
def add(command, address_book):
    name, phone = command.split()[1:]
    record = Record(name)
    record.add_phone(phone)
    address_book[name] = record
    return f"{name} added with phone number {phone}"


@input_error
def change(command, address_book):
    name, field_index, new_value = command.split()[1:]
    record = address_book[name]
    record.edit_field(int(field_index), new_value)
    return f"{name}'s field {field_index} updated to {new_value}"


@input_error
def show_all(address_book):
    if not address_book:
        return "No contacts found"
    return "\n".join([f"{name}: {record}" for name, record in address_book.items()])


@input_error
def remove(command, address_book):
    name, phone = command.split()[1], command.split()[2]
    record = address_book[name]
    record.remove_phone(phone)
    return f"{phone} removed from {name}'s phones"



def main():
    address_book = AddressBook()
    print("How can I help you?")
    while True:
        command = input(">>>")
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            print(add(command, address_book))
        elif command.startswith("change "):
            print(change(command, address_book))
        elif command.startswith("remove"):
            print(remove(command, address_book))
        elif command == "show all":
            print(show_all(address_book))
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
