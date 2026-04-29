
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.favorite = False

    def add_favorite(self):
        if self.favorite == True:
            print(f"Contact déjà ajouté aux favoris")
            return 
        self.favorite = True
        print(f"Contact ajouté au favoris")

    def withdraw_favorite(self):
        if self.favorite == False:
            print(f"Contact déjà retiré des favoris")
            return
        self.favorite = False
        print(f"Contact retiré des favoris")

    def show_contact(self,name, number):
        state = "⭐​" if self.favorite else ""
        print(f"Nom: {name} \n Numéro: {number}{state}")

name = input(f"Quel est le nom du contact ? ")
number = int(input("Quel est son numéro ? "))
contact = Contact(name, number)

contact.add_favorite()
contact.show_contact(name, number)

contact.withdraw_favorite()
contact.show_contact(name, number)