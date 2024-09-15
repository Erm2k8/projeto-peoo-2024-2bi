from members import Member
import json

class Group:
    def __init__(self, id: int, title: str, description: str, members: list[Member]):
        self.__id = 0
        self.__title = ""
        self.__description = ""
        self.__members = []

        self.set_id(id)
        self.set_title(title)
        self.set_description(description)
        self.set_members(members)

    def __str__(self):
        return f'Group: {self.title}'

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def members(self):
        return self.__members

    def set_id(self, id: int):
        if not (isinstance(id, int) and id > 0):
            raise ValueError('ID precisa ser um inteiro positivo.')
        self.__id = id

    def set_title(self, title: str):
        if not (isinstance(title, str) and len(title) > 0):
            raise ValueError('Título precisa ser uma string não vazia.')
        if len(title) > 50:
            raise ValueError('Título precisa ter no máximo 50 caracteres.')
        self.__title = title

    def set_description(self, description: str):
        if not (isinstance(description, str) and len(description) <= 255):
            raise ValueError('Descrição precisa ter no máximo 255 caracteres.')
        self.__description = description

    def set_members(self, members: list[Member]):
        if not isinstance(members, list):
            raise ValueError('Os membros devem estar em uma lista.')
        if len(members) == 0:
            raise ValueError('A lista de membros deve conter pelo menos um membro.')
        if not all(isinstance(member, Member) for member in members):
            raise ValueError('Os membros devem ser uma lista de objetos Member.')
        self.__members = members

    def insert_member(self, member: Member):
        self.__members.append(member)

    def list_members(self):
        return self.__members

    def remove_member(self, id: int):
        self.__members = [member for member in self.__members if member.id != id]

    def update_member(self, id: int, member: Member):
        for i in range(len(self.__members)):
            if self.__members[i].id == id:
                self.__members[i] = member
                break

    def get_member_by_id(self, id: int):
        for member in self.__members:
            if member.id == id:
                return member
        return None

    def open(self):
        try:
            with open('./data/groups.json', 'r') as file:
                data = json.load(file)
                for group in data:
                    if group['id'] == self.__id:
                        self.__title = group['title']
                        self.__description = group['description']
                        self.__members = [Member(**member) for member in group['members']]
                        break
        except FileNotFoundError:
            pass

    def save(self):
        try:
            with open('./data/groups.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        group_found = False
        for group in data:
            if group['id'] == self.__id:
                group['title'] = self.__title
                group['description'] = self.__description
                group['members'] = [member.to_dict() for member in self.__members]
                group_found = True
                break

        if not group_found:
            data.append({
                'id': self.__id,
                'title': self.__title,
                'description': self.__description,
                'members': [member.to_dict() for member in self.__members]
            })

        with open('./data/groups.json', 'w') as file:
            json.dump(data, file, indent=4)


class Groups:
    __groups = []

    @classmethod
    @property
    def groups(cls):
        return cls.__groups

    @classmethod
    def add_group(cls, group: Group):
        cls.__groups.append(group)

    @classmethod
    def delete_group(cls, id: int):
        cls.__groups = [group for group in cls.__groups if group.id != id]

    @classmethod
    def update_group(cls, id: int, group: Group):
        for i in range(len(cls.__groups)):
            if cls.__groups[i].id == id:
                cls.__groups[i] = group
                break

    @classmethod
    def get_group_by_id(cls, id: int):
        for group in cls.__groups:
            if group.id == id:
                return group
        return None

    @classmethod
    def open(cls):
        cls.__groups = []
        try:
            with open('./data/groups.json', 'r') as file:
                data = json.load(file)
                for group in data:
                    cls.add_group(Group(**group))
        except FileNotFoundError:
            pass

    @classmethod
    def save(cls):
        data = []
        for group in cls.__groups:
            data.append({
                'id': group.id,
                'title': group.title,
                'description': group.description,
                'members': [member.to_dict() for member in group.members]
            })

        with open('./data/groups.json', 'w') as file:
            json.dump(data, file, indent=4)
