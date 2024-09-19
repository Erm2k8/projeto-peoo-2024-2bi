bold_blue = '\033[1;34m'
bold_white = '\033[1;37m'
italic_white = '\033[3;37m'
italic_red = '\033[3;31m'
bold_yellow = '\033[1;33m'

from views import Views

print("="*30)
print(f"{bold_yellow}Listar contatos\n")
contacts = Views.list_contacts()
for contact in contacts:
    print(contact)