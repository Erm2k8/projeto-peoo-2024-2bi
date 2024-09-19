from views import *
import os

# Estilo:
# 0 - Resetar todos os atributos
# 1 - Negrito/Bright
# 2 - Atenuado/Dim
# 3 - Itálico
# 4 - Sublinhado
# 5 - Blink
# 7 - Inverso
# 8 - Escondido

# Cor do Texto:
# 30 - Preto
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Magenta
# 36 - Ciano
# 37 - Branco

# Cor de Fundo:
# 40 - Preto
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Magenta
# 46 - Ciano
# 47 - Branco

class UI:
    bold_blue = '\033[1;34m'
    bold_white = '\033[1;37m'
    bold_green = '\033[1;32m'
    italic_white = '\033[3;37m'
    italic_red = '\033[3;31m'
    bold_yellow = '\033[1;33m'
    
    @classmethod
    def main(cls):
        while True:
            option = cls.menu()
            
            match option:
                case '1':
                    cls.create_contact()
                case '2':
                    cls.list_contacts()
                case '3':
                    cls.search_contact_by_id()
                case '4':
                    cls.update_contact()
                case '5':
                    cls.delete_contact()
                case '6':
                    cls.add_group()
                case '7':
                    cls.list_groups()
                case '8':
                    cls.search_group_by_id()
                case '9':
                    cls.update_group()
                case '10':
                    cls.delete_group()
                case '11':
                    cls.insert_member()
                case '12':
                    cls.list_members()
                case '13':
                    cls.search_member_by_id()
                case '14':
                    cls.update_member()
                case '15':
                    cls.delete_member()
                case '16':
                    print(f"{cls.bold_yellow}Saindo...")
                    exit()
                case _:
                    print(f"\n{cls.italic_red}Opção inválida\n")
    
    @classmethod
    def menu(cls):
        print("="*30)
        print(f"{cls.bold_yellow}O que desejas fazer?\n")
        print(f"{cls.bold_blue}[01] {cls.italic_white}Criar contato")
        print(f"{cls.bold_blue}[02] {cls.italic_white}Listar contatos")
        print(f"{cls.bold_blue}[03] {cls.italic_white}Buscar contato")
        print(f"{cls.bold_blue}[04] {cls.italic_white}Atualizar contato")
        print(f"{cls.bold_blue}[05] {cls.italic_white}Deletar contato")
        print(f"{cls.bold_blue}[06] {cls.italic_white}Inserir grupo")
        print(f"{cls.bold_blue}[07] {cls.italic_white}Listar grupos")
        print(f"{cls.bold_blue}[08] {cls.italic_white}Buscar grupo")
        print(f"{cls.bold_blue}[09] {cls.italic_white}Atualizar grupo")
        print(f"{cls.bold_blue}[10] {cls.italic_white}Deletar grupo")
        print(f"{cls.bold_blue}[11] {cls.italic_white}Inserir membro")
        print(f"{cls.bold_blue}[12] {cls.italic_white}Listar membros")
        print(f"{cls.bold_blue}[13] {cls.italic_white}Buscar membro")
        print(f"{cls.bold_blue}[14] {cls.italic_white}Atualizar membro")
        print(f"{cls.bold_blue}[15] {cls.italic_white}Deletar membro")
        print(f"{cls.bold_blue}[16] {cls.italic_red}Sair")
        print()
        option = input(f"{cls.bold_blue}Escreva aqui: {cls.bold_white}")
        
        # os.system('cls' if os.name == 'nt' else 'clear')
        return option
                
    @classmethod
    def create_contact(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Criar contato\n")
        name = input(f"{cls.bold_green}Nome: {cls.bold_white}")
        email = input(f"{cls.bold_green}E-mail: {cls.bold_white}")
        phone = input(f"{cls.bold_green}Telefone: {cls.bold_white}")
        
        Views.create_contact(name, email, phone)
    
    @classmethod
    def list_contacts(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Listar contatos\n")
        contacts = Views.list_contacts()
        for contact in contacts:
            print(f"{cls.bold_white}{contact}")
    
    @classmethod
    def search_contact_by_id(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Buscar contato\n")
        try:
            id = int(input(f"{cls.bold_green}ID: {cls.bold_white}"))
            contact = Views.search_contact_by_id(id)
            if contact:
                print(f"{cls.bold_white}{contact}")
            else:
                print(f"{cls.bold_white}Contato não encontrado")
        except ValueError:
            print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
    
    @classmethod
    def update_contact(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Atualizar contato\n")
        try:
            id = int(input(f"{cls.bold_green}ID: {cls.bold_white}"))
            name = input(f"{cls.bold_green}Nome: {cls.bold_white}")
            email = input(f"{cls.bold_green}E-mail: {cls.bold_white}")
            phone = input(f"{cls.bold_green}Telefone: {cls.bold_white}")
            
            Views.update_contact(id, name, email, phone)
        except ValueError:
            print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
    
    @classmethod
    def delete_contact(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Deletar contato\n")
        try:
            id = int(input(f"{cls.bold_green}ID: {cls.bold_white}"))
            Views.delete_contact(id)
        except ValueError:
            print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
    
    @classmethod
    def add_group(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Inserir grupo\n")
        title = input(f"{cls.bold_green}Título: {cls.bold_white}")
        description = input(f"{cls.bold_green}Descrição: {cls.bold_white}")
        
        Views.add_group(title, description)
    
    @classmethod
    def list_groups(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Listar grupos\n")
        groups = Views.list_groups()
        for group in groups:
            print(f"{cls.bold_white}{group}")
    
    @classmethod
    def search_group_by_id(cls):
        print("="*30)
        print(f"{cls.bold_yellow}Buscar grupo\n")
        try:
            id = int(input(f"{cls.bold_green}ID do Grupo: {cls.bold_white}"))
            group = Views.search_group_by_id(id)
            if group:
                print(f"{cls.bold_white}{group}")
            else:
                print(f"{cls.bold_white}Grupo não encontrado")
        except ValueError:
            print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
    
    @classmethod
    def update_group(cls):
        cls.list_groups()
        print("="*30)
        print(f"{cls.bold_yellow}Atualizar grupo\n")
        try:
            id = int(input(f"{cls.bold_green}ID: {cls.bold_white}"))
            title = input(f"{cls.bold_green}Título: {cls.bold_white}")
            description = input(f"{cls.bold_green}Descrição: {cls.bold_white}")
            
            Views.update_group(id, title, description)
        except ValueError:
            print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
    
    @classmethod
    def delete_group(cls):
        cls.list_groups()
        print("="*30)
        print(f"{cls.bold_yellow}Deletar grupo\n")
        try:
            id = int(input(f"{cls.bold_green}ID: {cls.bold_white}"))
            Views.delete_group(id)
        except ValueError:
            print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
    
    @classmethod
    def insert_member(cls):
        cls.list_groups()
        print("="*30)
        print(f"{cls.bold_yellow}Inserir membro\n")
        try:
            group_id = int(input(f"{cls.bold_green}ID do grupo: {cls.bold_white}"))
            cls.list_contacts()
            contact_id = int(input(f"{cls.bold_green}ID do contato: {cls.bold_white}"))
            username = input(f"{cls.bold_green}Nome de usuário: {cls.bold_white}")
            permissions = input(f"{cls.bold_green}Permissões (1 - Ler, 2 - Escrever, 3 - Ler e Escrever, 4 - ADMIN): {cls.bold_white}")
            
            match permissions:
                case '1':
                    permissions = Permissions.READ
                case '2':
                    permissions = Permissions.WRITE
                case '3':
                    permissions = Permissions.READ | Permissions.WRITE
                case '4':
                    permissions = Permissions.ADMIN
                case _:
                    permissions = Permissions.READ
            
            Views.insert_member(username, group_id, contact_id, permissions)
        except ValueError:
            print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
    
    @classmethod
    def list_members(cls, group_id: int = 0):
        print("="*30)
        if group_id == 0:
            cls.list_groups()
            print()
            try:
                group_id = int(input(f"{cls.bold_green}ID do grupo: {cls.bold_white}"))
            except ValueError:
                print(f"{cls.italic_red}ID inválido. Deve ser um número inteiro.")
                return
        print(f"{cls.bold_yellow}Listar membros\n")
        members = Views.list_members(group_id)
        for member in members:
            print(f"{cls.bold_white}{member}")
    
    @classmethod
    def search_member_by_id(cls):
        print("="*30)
        cls.list_groups()
        print()
        print(f"{cls.bold_yellow}Buscar membro\n")
        try:
            group_id = int(input(f"{cls.bold_green}ID do grupo: {cls.bold_white}"))
            member_id = int(input(f"{cls.bold_green}ID do membro: {cls.bold_white}"))
            member = Views.search_member_by_id(group_id, member_id)
            if member:
                print(f"{cls.bold_white}{member}")
            else:
                print(f"{cls.bold_white}Membro não encontrado")
        except ValueError:
            print(f"{cls.italic_red}IDs inválidos. Devem ser números inteiros.")
    
    @classmethod
    def update_member(cls):
        print("="*30)
        cls.list_groups()
        print()
        print(f"{cls.bold_yellow}Atualizar membro\n")
        try:
            group_id = int(input(f"{cls.bold_green}ID do grupo: {cls.bold_white}"))
            cls.list_members(group_id)
            print()
            id = int(input(f"{cls.bold_green}ID do membro: {cls.bold_white}"))
            username = input(f"{cls.bold_green}Nome de usuário: {cls.bold_white}")
            permissions = input(f"{cls.bold_green}Permissões (1 - Ler, 2 - Escrever, 3 - Ler e Escrever, 4 - ADMIN): {cls.bold_white}")
            
            match permissions:
                case '1':
                    permissions = Permissions.READ
                case '2':
                    permissions = Permissions.WRITE
                case '3':
                    permissions = Permissions.READ | Permissions.WRITE
                case '4':
                    permissions = Permissions.ADMIN
                case _:
                    permissions = Permissions.READ
            
            Views.update_member(group_id, id, username, permissions)
        except ValueError:
            print(f"{cls.italic_red}IDs ou permissões inválidos.")
    
    @classmethod
    def delete_member(cls):
        print("="*30)
        cls.list_groups()
        print()
        print(f"{cls.bold_yellow}Deletar membro\n")
        try:
            group_id = int(input(f"{cls.bold_green}ID do grupo: {cls.bold_white}"))
            cls.list_members(group_id)
            print()
            id = int(input(f"{cls.bold_green}ID do membro: {cls.bold_white}"))
            Views.delete_member(group_id, id)
        except ValueError:
            print(f"{cls.italic_red}IDs inválidos. Devem ser números inteiros.")
