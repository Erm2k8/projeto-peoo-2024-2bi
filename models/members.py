from enum import IntFlag, auto

class Permissions(IntFlag):
    READ = auto()
    WRITE = auto()
    ADMIN = auto()

class Member:
    def __init__(self, id: int, name: str, username: str, id_groups: set[int], id_contact: int, permissions: Permissions):
        self.__id = id
        self.__name = name
        self.__username = username
        self.__id_groups = id_groups
        self.__permissions = permissions
        self.__id_contact = id_contact

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
    def id_groups(self):
        return self.__id_groups
    
    @property
    def permissions(self):
        return self.__permissions
    
    @property
    def id_contact(self):
        return self.__id_contact
    
    def set_id(self, id: int):
        if not (isinstance(id, int) and id > 0):
            raise ValueError('ID precisa ser um inteiro positivo.')
        self.__id = id
    
    def set_name(self, name: str): 
        if not (isinstance(name, str) and len(name) > 0):
            raise ValueError('Nome precisa ser uma string não vazia.')
        if not (name.strip().isalpha().replace(' ', '').isalpha()):
            raise ValueError('Nome precisa ter apenas letras.')
        if len(name) > 50:
            raise ValueError('Nome precisa ter no máximo 50 caracteres.')
        self.__name = name
    
    def set_username(self, username: str):
        if not (isinstance(username, str) and len(username) >= 3):
            raise ValueError('Nome de usuário inválido.')
        if len(username) > 20:
            raise ValueError('Nome de usuário precisa ter no máximo 20 caracteres.')
        self.__username = username
    
    def set_id_groups(self, id_groups: set[int]):
        if not isinstance(id_groups, set):
            raise ValueError('Os grupos devem estar em um conjunto.')
        if len(id_groups) == 0:
            raise ValueError('O conjunto de grupos deve conter pelo menos um grupo.')
        self.__id_groups = id_groups
    
    def set_permissions(self, permissions: Permissions):
        if not isinstance(permissions, Permissions):
            raise ValueError('As permissões devem ser do tipo Permissions.')
        self.__permissions = permissions
    
    def set_id_contact(self, id_contact: int):
        if not (isinstance(id_contact, int) and id_contact > 0):
            raise ValueError('ID do contato precisa ser um inteiro positivo.')
        self.__id_contact = id_contact
