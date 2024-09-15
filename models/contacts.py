import re

EMAIL_REGEX = r"^\S+@\S+\.\S+$"

class Contact:
    def __init__(self, id: int, name: str, email: str, phone: str):
        self.__id = 0
        self.__name = ""
        self.__email = ""
        self.__phone = ""

        self.set_id(id)
        self.set_name(name)
        self.set_email(email)
        self.set_phone(phone)

    def __str__(self):
        return f'Contact: {self.name}, ID: {self.id}'

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
    
    def phone(self):
        return self.__phone
    
    def set_id(self, id: int):
        if not (isinstance(id, int) and id > 0):
            raise ValueError('ID precisa ser um inteiro positivo.')
        
        self.__id = id
        
    def set_name(self, name: str): 
        if not (isinstance(name, str) and len(name) > 0):
            raise ValueError('Nome precisa ser uma string não vazia.')
        if not (name.strip().isalpha().replace(' ', '').isalpha()):
            raise ValueError('Nome precisa ter apenas letras.')
        if len(name) > 50:
            raise ValueError('Nome precisa ter no máximo 50 caracteres.')
        
        self.__name = name
        
    def set_email(self, email: str):
        if not (isinstance(email, str) and len(email) > 0):
            raise ValueError('Email precisa ser uma string não vazia.')
        if not re.match(EMAIL_REGEX, email):
            raise ValueError('Email inválido.')
        
        self.__email = email
        
    def set_phone(self, phone: str):
        if not (isinstance(phone, str) and len(phone) > 0):
            raise ValueError('Telefone precisa ser uma string não vazia.')
        if not re.match(r"\d{11}", phone):
            raise ValueError('Telefone inválido.')
        
        self.__phone = phone