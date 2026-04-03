inventory = []
energy = 100

while True :
     print(f"\n 1- Ajouter un objet \n 2- Voir tous les objets \n 3- Voir les 3 derniers objets \n 4- Supprimer un objet \n 5- Utiliser un objet (réduit énergie) \n 6- Se reposer (augmente énergie, max 100) \n 7- Voir énergie \n 8- Quitter")
     try :
          choice = int(input("Que voulez-vous faire ? "))
     except ValueError:
          print(f"Ceci est un choix invalide")
          continue

     if choice == 1:
          object_name = input("Son nom : ")

          if object_name == "":
               print(f"Vous devez entrer un nom")
          else:
               if any (object_name == obj[0] for obj in inventory ):
                    print(f"Ce nom existe déjà dans la liste")
               else:
                    while True:
                         try:
                              object_energy = int(input("Entrer son coût en énergie : "))

                              if object_energy > 100:
                                   print(f"L'énergie de l'objet ne doit pas dépasser 100")
                              else:
                                   inventory.append([object_name,object_energy])
                                   print(f"Vous avez ajouté un nouveau objet")
                                   break
                         except ValueError:
                              print(f"Ceci n'est pas un coût d'énergie")
                              continue 
     
     elif choice == 2:
          if not inventory:
               print(f"Vous ne disposez d'aucun objet")
          else:
               for i, obj in enumerate(inventory, start=1):
                    print(f"{i}- {obj[0]} : {obj[1]}")

     elif choice == 3:
          if not inventory:
               print(f"Vous ne disposez d'aucun objet")
          else:
               for i, obj in enumerate(inventory[-3:], start=1):
                    print(f"{i}- {obj[0]} : {obj[1]}")
               
     elif choice == 4:
          if not inventory :
               print(f"Vous ne disposez d'aucun objet")
          else:
               while True:
                    try:
                         object_index = int(input("Quel est son index : "))

                         object_index -= 1
                         if 0 <= object_index < len(inventory):
                              inventory.pop(object_index)
                              print(f"Vous avez supprimé un objet ")
                              break
                         else:
                              print(f"Cet index est inexistant dans la liste")
                    except ValueError:
                         print(f"Ceci n'est pas un index")
                         
     elif choice == 5:
          if not inventory :
               print(f"Vous disposez aucun d'objet")
          else:
               if energy <= 0:
                    print(f"Vous ne disposez pas d'énergie pour pouvoir utiliser un objet")
               else:
                    while True:
                         try:
                              object_index = int(input("Quel est son index : "))

                              object_index -= 1
                              if 0 <= object_index < len(inventory):
                                   energy -= inventory[object_index][1]
                                   print(f"Vous avez utilisé un objet du nom de {inventory[object_index][0]}")
                                   break
                              else:
                                   print(f"Cet index est inexistant dans la liste")
                         except ValueError:
                              print(f"Ceci n'est pas un index")
     
     elif choice == 6:
          if energy >= 100:
               print(f"Vous êtes plein d'énergie")   
          else:
               energy = 100
               print(f"Vous avez gagné en puissance")     

     elif choice == 7:
          print(f" Vous disposez de {energy} énergie(s)")

     elif choice == 8:
          print(f"Au revoir et à bienôt")
          break
     else:
          print(f"Ce choix est inexistant la liste")         
                         
