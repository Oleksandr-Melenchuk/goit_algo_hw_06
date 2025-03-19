from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.number_check(value):
            raise ValueError("Not correct form of number")
        super().__init__(value)
    
    @staticmethod
    def number_check(value):
        return value.isdigit() and len(value) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            return  
        raise ValueError(f"{phone} Number not in AddressBook")
    
    def edit_phone(self, phone, new_phone):
        phone_obj = self.find_phone(phone)
        
        if not phone_obj:
            raise ValueError(f"{phone} Number not found")
        
        if not Phone.number_check(new_phone):
            raise ValueError(f"New number is not valid {new_phone}")
            
        self.remove_phone(phone_obj.value) 
        self.add_phone(new_phone)
        return

    
    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone: 
                return ph
        return None
        
        
    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"
        
        
class AddressBook(UserDict):
    
    def add_record(self, record:Record) -> dict:
        self.data[record.name.value] = record
        
    def find(self, name) -> Record:
        return self.data.get(name)
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __str__(self):
        return "\n".join(str(value) for value in self.data.values())
        

