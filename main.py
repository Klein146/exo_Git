
class Contact():
    def __init__(self, name: str, surname: str, email: str, telephone: int):
        self.name = name.strip().lower()
        self.surname = surname.strip().lower()
        self.email = email.strip().lower()
        self.telephone = telephone
    def get_name(self):
        return self.name

    def set_name(self, value: str):
        self.name = value.strip().lower()
    
    def get_surname(self):
        return self.surname

    def set_surname(self, value):
        self.surname = value.strip().lower()

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value.strip().lower()

    def get_telephone(self):
        return self.telephone 

    def set_telephone(self, value : int):
        self.telephone = value


class GestionnaireContact:

    def __init__(self):
        self.list_de_contact = []
    def add_contact(self):
        pass

    def shows_all_contact(self):
        print("\n------- Liste de tout les contacts ----\n")
        for contacts in self.list_de_contact :
            print(f"full name : {contacts.get_name()} {contacts.get_surname()}\n  Contact : {contacts.get_email()}, {contacts.get_telephone()}\n")
        return 

    def find_contact(self):
        pass

    def update_already_contact(self):
        pass

    def drop_already_contact(self):
        pass

    def saveContact(self):
        pass

    def uploadContact(self):
        pass

def main_menu():
    pass


if __name__ == "__main__":
    main_menu()