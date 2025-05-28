
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
        pass

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

    mon_gestionnaire = GestionnaireContact()

    while True:
        print("\n\n========== MENU PRINCIPAL ==========")
        print("1• Ajouter un contact")
        print("2• Afficher un contact")
        print("3• Rechercher un contact")
        print("4• Modifier un contact")
        print("5• Supprimer un contact")
        print("0• Quitter")

        
    choix = input("Votre choix : ")
    if choix == "1":
        mon_gestionnaire.add_contact()
    elif choix == "2":
        mon_gestionnaire.shows_all_contact() 
    elif choix == "3":
        mon_gestionnaire.find_contact()
    elif choix == "4":
        mon_gestionnaire.update_already_contact()
    elif choix == "5":
        mon_gestionnaire.drop_already_contact()
    elif choix == "0":
        print("👋 Au revoir !")
    else : 
        print("❌ Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main_menu()