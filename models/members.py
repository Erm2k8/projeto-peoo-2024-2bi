from enum import IntFlag, auto

class Permissions(IntFlag):
    READ = auto()
    WRITE = auto()
    ADMIN = auto()

class Member:
    def __init__(self, id: int, name: str, username: str, idGroups: set[int], idContact: int, permissions: Permissions):
        self.__id = self.set_id(id)
        self.__name = ""
        self.__username = ""
        self.__idGroups = set()
        self.__permissions = set()
        self.__idContact = 0
        
        self.set_name(name)
        self.set_username(username)
        self.set_idGroups(idGroups)
        self.set_permissions(permissions)
        self.set_idContact(idContact)
        
    def __str__(self):
        return f'id: {self.__id}, name: {self.__name}, username: {self.__username}, permissions: {self.__permissions}'
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def username(self):
        return self.__username

    @property
    def idGroups(self):
        return self.__idGroups
    
    @property
    def permissions(self):
        return self.__permissions
    
    @property
    def idContact(self):
        return self.__idContact
    
    def set_id(self, id: int):
        if not (isinstance(id, int) and id > 0):
            raise ValueError('ID precisa ser um inteiro positivo.')
        return id
    
    def set_name(self, name: str): 
        if not (isinstance(name, str) and len(name) > 0):
            raise ValueError('Nome precisa ser uma string não vazia.')
        if not (name.strip().isalpha().replace(' ', '').isalpha()):
            raise ValueError('Nome precisa ter apenas letras.')
        if len(name) > 50:
            raise ValueError('Nome precisa ter no máximo 50 caracteres.')
        
        self.__name = name
    
    def set_username(self, username: str):
        if not (isinstance(username, str) and len(username) >= 3):
            raise ValueError('Nome de usuário inválido.')
        if len(username) > 20:
            raise ValueError('Nome de usuário precisa ter no máximo 20 caracteres.')
        
        self.__username = username
    
    def set_idGroups(self, idGroups: set[int]):
        if not isinstance(idGroups, set):
            raise ValueError('Os grupos devem estar em um conjunto.')
        if len(idGroups) == 0:
            raise ValueError('O conjunto de grupos deve conter pelo menos um grupo.')
        
        self.__idGroups = idGroups
    
    def set_permissions(self, permissions: Permissions):
        if not isinstance(permissions, Permissions):
            raise ValueError('As permissoes devem ser do tipo Permissions.')
        
        self.__permissions = permissions
    
    def set_idContact(self, idContact: int):
        if not (isinstance(idContact, int) and idContact > 0):
            raise ValueError('ID do contato precisa ser um inteiro positivo.')
        
        self.__idContact = idContact