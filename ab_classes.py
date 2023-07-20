from collections import UserDict
from datetime import datetime

# class BirthdayError(Exception):
#     pass

class Field:
    def __init__(self, value) -> None:
        self.value = value
        
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
    
class Phone(Field):
    pass

class Name(Field):
    pass

class Birthday:
    def __init__(self, value):
        self.__value = None
        self.value = value
        
    @property
    def value(self):
        return self.__value # datetime#.strftime("%d-%m-%Y")    
        
    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, "%d-%m-%Y")
        except Exception as err:
            return err


    def __str__(self):
        return self.__value.strftime("%d-%m-%Y")


class Record():
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None) -> None:
        self.name = name
        self.phones = []
        self.birthday = birthday
        if phone:
            self.phones.append(phone)
    
    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f'Contact {self.name} was updated with phone {phone}.'
        return f'Phone "{phone}" is already belong to contact with name "{self.name}".'
    
    def change_phone(self, old_p: Phone, new_p: Phone):
        for indx, p in enumerate(self.phones):
            if old_p.value == p.value:
                self.phones[indx] = new_p
                return f'Contacts "{self.name}" phone "{old_p}" changed to "{new_p}".'    
        return f'Contact "{self.name}" has no phone "{old_p}" to change.'    
    
    def del_phone(self, phone_to_remove: Phone):
        for indx, p in enumerate(self.phones):
            if phone_to_remove.value == p.value:
                del self.phones[indx]
                return f'Contacts "{self.name}" phone "{phone_to_remove}" was removed".'    
        return f'Contact "{self.name}" has no phone "{phone_to_remove}" to remove.'    
  

    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"           
    
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} was added"
    
    def __str__(self) -> str:
        if self.data:
            return '\n'.join(str(r) for r in self.values()) + '\n' + '...the end of phone book.'
        return 'Address book is empty'

    def get_day_to_bd(self):
        if self.birthday:
            return self.birthday.value.weekday()
        return -1

    def __iter__(self):
        pass
        #return self
    
    def __next__(self, N: int = 10):
        pass
        

