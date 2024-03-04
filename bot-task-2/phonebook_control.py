"""control module"""
from collections import UserDict

class Field:
    """basic class for records fields"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """stores contacts name"""

    def __init__(self, name=str):
        super().__init__(name)


class Phone(Field):
    """stores phone number"""

    def __init__(self, phone=str):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Phone number must have 10 digits")
        super().__init__(phone)


class Record:
    """stores contact including name and phones list"""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """adds phone number to record"""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """removes phone number from record"""
        for p in self.phones:
            print(p)
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        """edits phone number in record"""
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

    def find_phone(self, phone):
        """finds phone number in record"""
        for p in self.phones:
            if p.value == phone:
                return p
            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """containing and controlling records in Address book"""

    def add_record(self, record):
        """adds record to Address book"""
        self.data[record.name.value] = record

    def find(self, key):
        """finds record in Address book"""
        if key in self.data:
            return self.data[key]

    def delete(self, key):
        """deletes record from Address book"""
        if key in self.data:
            del self.data[key]


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
