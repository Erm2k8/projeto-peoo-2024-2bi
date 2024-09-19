from enum import IntFlag, auto

class Permissions(IntFlag):
    READ = auto()
    WRITE = auto()
    ADMIN = auto()

class Member:
    def __init__(self, id: int, username: str, id_group: int, id_contact: int, permissions: Permissions):
        self.__id = id
        self.__username = username
        self.__id_group = id_group
        self.__permissions = permissions
        self.__id_contact = id_contact

    def __str__(self):
        return f'id: {self.__id}, username: {self.__username}, permissions: {self.__permissions}'

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def id_group(self):
        return self.__id_group

    @property
    def permissions(self):
        return self.__permissions

    @property
    def id_contact(self):
        return int(self.__id_contact)

    def set_id(self, id: int):
        if not (isinstance(id, int) and id > 0):
            raise ValueError('ID precisa ser um inteiro positivo.')
        self.__id = id

    def set_username(self, username: str):
        if not (isinstance(username, str) and len(username) >= 3):
            raise ValueError('Nome de usuário inválido.')
        if len(username) > 20:
            raise ValueError('Nome de usuário precisa ter no máximo 20 caracteres.')
        self.__username = username

    def set_id_group(self, id_group: int):
        if not (isinstance(id_group, int) and id_group > 0):
            raise ValueError('ID do grupo precisa ser um inteiro positivo.')
        self.__id_group = id_group

    def set_permissions(self, permissions: Permissions):
        if not isinstance(permissions, Permissions):
            raise ValueError('As permissões devem ser do tipo Permissions.')
        self.__permissions = permissions

    def set_id_contact(self, id_contact: int):
        if not (isinstance(id_contact, int) and id_contact > 0):
            raise ValueError('ID do contato precisa ser um inteiro positivo.')
        self.__id_contact = int(id_contact)

    def to_dict(self):
        return {
            'id': self.__id,
            'username': self.__username,
            'id_group': self.__id_group,
            'permissions': self.__permissions.value,
            'id_contact': self.__id_contact
        }
