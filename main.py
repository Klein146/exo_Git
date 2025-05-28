
class Contact():
    def __init__(self, name: str, surname: str, email: str, telephone: int):
        self.name = name.strip().lower()
        self.surname = surname.strip().lower()
        self.email = email.strip().lower()
        self.telephone = telephone


class GestionnaireContact:

    def __init__(self):
        self.list_de_contact = []


def main_menu():
    pass
if __name__ == "__main__":
    main_menu()