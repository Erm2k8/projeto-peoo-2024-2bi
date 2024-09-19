import re
import json

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
        return f'Nome: {self.__name}, ID: {self.__id}'

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    def set_id(self, id: int):
        if not (isinstance(id, int) and id >= 0):
            raise ValueError('ID precisa ser um inteiro positivo.')
        self.__id = id

    def set_name(self, name: str): 
        if not (isinstance(name, str) and len(name) > 0):
            raise ValueError('Nome precisa ser uma string não vazia.')
        if not (name.strip().replace(' ', '').isalpha()):
            raise ValueError('Nome precisa ter apenas letras.')
        if len(name) > 50:
            raise ValueError('Nome precisa ter no máximo 50 caracteres.')
        self.__name = name
    
    def set_email(self, email: str):
        if not (isinstance(email, str) and len(email) > 0):
            raise ValueError('Email precisa ser uma string não vazia.')
        if not re.match(EMAIL_REGEX, email):
            raise ValueError('Email inválido.')
        self.__email = email
    
    def set_phone(self, phone: str):
        if not (isinstance(phone, str) and len(phone) > 0):
            raise ValueError('Telefone precisa ser uma string não vazia.')
        if not re.match(r"\d{11}", phone):
            raise ValueError('Telefone inválido.')
        self.__phone = phone
    
    def to_dict(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'email': self.__email,
            'phone': self.__phone
        }

class Contacts:
    __contacts = []

    @classmethod
    @property
    def contacts(cls):
        cls.open()
        return cls.__contacts

    @classmethod
    def create_contact(cls, contact: Contact):
        cls.open()
        contact.set_id(len(cls.__contacts) + 1)
        cls.__contacts.append(contact)
        cls.save()

    @classmethod
    def delete_contact(cls, id: int):
        cls.open()
        cls.__contacts = [contact for contact in cls.__contacts if contact.id != id]
        cls.save()
        
    @classmethod
    def list_contacts(cls):
        cls.open()
        return cls.__contacts
    
    @classmethod
    def update_contact(cls, contact: Contact):
        cls.open()
        for i in range(len(cls.__contacts)):
            if cls.__contacts[i].id == contact.id:
                cls.__contacts[i] = contact
                break
        cls.save()
        
    @classmethod
    def search_contact(cls, id: int):
        cls.open()
        for contact in cls.__contacts:
            if contact.id == id:
                return contact
        return None
    
    @classmethod
    def open(cls):
        try:
            with open('./data/contacts.json', 'r') as file:
                cls.__contacts = [Contact(**contact) for contact in json.load(file)]
        except FileNotFoundError:
            cls.__contacts = []

    @classmethod
    def save(cls):
        with open('./data/contacts.json', 'w') as file:
            json.dump([contact.to_dict() for contact in cls.__contacts], file, indent=4)

    def __str__(self):
        return f'Contacts: {self.__contacts}'
