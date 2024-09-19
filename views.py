from models.contacts import Contact, Contacts
from models.groups import Group, Groups
from models.members import Member, Permissions

class Views:
    @classmethod
    def create_contact(cls, name: str, email: str, phone: str):
        contact = Contact(0, name, email, phone)
        Contacts.create_contact(contact)
        
    @classmethod
    def list_contacts(cls):
        return Contacts.list_contacts()
    
    @classmethod
    def search_contact_by_id(cls, id: int):
        return Contacts.search_contact(id)
    
    @classmethod
    def update_contact(cls, id: int, name: str, email: str, phone: str):
        contact = Contact(id, name, email, phone)
        Contacts.update_contact(contact)
        
    @classmethod
    def delete_contact(cls, id: int):
        Contacts.delete_contact(id)
    
    @classmethod
    def add_group(cls, title: str, description: str):
        group = Group(0, title, description)
        Groups.add_group(group)
        
    @classmethod
    def list_groups(cls):
        return Groups.groups
    
    @classmethod
    def search_group_by_id(cls, id: int):
        return Groups.get_group_by_id(id)
    
    @classmethod
    def update_group(cls, id: int, title: str, description: str):
        group = Group(id, title, description)
        Groups.update_group(id, group)
        
    @classmethod
    def delete_group(cls, id: int):
        Groups.delete_group(id)
        
    @classmethod
    def insert_member(cls, username: str, group_id: int, contact_id: int, permissions: Permissions):
        member = Member(0, username, group_id, contact_id, permissions)
        group = Groups.get_group_by_id(group_id)
        if group is not None:
            group.insert_member(member)
        
    @classmethod
    def list_members(cls, group_id: int):
        group = Groups.get_group_by_id(group_id)
        if group is not None:
            return group.list_members()
    
    @classmethod
    def search_member_by_id(cls, group_id: int, id: int):
        group = Groups.get_group_by_id(group_id)
        if group is not None:
            return group.get_member_by_id(id)
    
    @classmethod
    def update_member(cls, group_id: int, id: int, username: str, permissions: Permissions):
        group = Groups.get_group_by_id(group_id)
        if group is not None:
            member = group.get_member_by_id(id)
            if member is not None:
                updated_member = Member(id, username, group_id, member.id_contact, permissions)
                group.update_member(id, updated_member)
        
    @classmethod
    def delete_member(cls, group_id: int, id: int):
        group = Groups.get_group_by_id(group_id)
        if group is not None:
            group.remove_member(id)
