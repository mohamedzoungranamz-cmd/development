patients = []

while True :
     print(f"\n 1- Ajouter un patient \n 2- Voir toutes les patients \n 3- Voir les trois derniers patients \n 4- Supprimer un patient \n 5- Marquer un patient comme soigné \n 6- Voir tous patients soignés \n 7- Voir tous les patients non soignés \n 8- Quitter ")

     try : 
          choice = int(input("Que voulez-vous faire ?: "))
     except ValueError:
          print(f"Ceci est un choix invalide")
          continue
          # Ajouter un patient
     if choice == 1:
          patient_name = input("Quel est le nom du patient ?: ")
          
          if patient_name == "":
               print(f"Vous devez entrer un nom")
          else:
               if any( patient[0] == patient_name for patient in patients ):
                    print(f"Ce nom existe déjà dans la liste")
               else:
                    try:
                         patient_status = int(input("Quel est l'etat du patient 1) Soigné(e)  2) Pas soigné(e) : "))                        
                    except ValueError:
                         print(f"Ceci est un choix invalide")
                         continue
                    if patient_status == 1:
                         patients.append([patient_name, "Soigné(e)"])
                         print(f"Vous avez ajouté un nouveau patient")
                    elif patient_status == 2:
                         patients.append([patient_name, "Pas soigné(e)"])
                         print(f"Vous avez ajouté un nouveau patient")
                    else:
                         print(f"Ce choix est invalide !")
     # Voir tous les patients
     elif choice == 2:
          if  not patients:
               print(f"Aucun patient pour le moment")
          else:
               for i, patient in enumerate(patients, start=1):
                    print(f"{i}- {patient[0]} : {patient[1]}")
     # Voir les trois derniers patients
     elif choice == 3:
          if not patients:
               print(f"Aucun patient pour l'instant")
          else:
               for i, patient in enumerate(patients[-3:], start=1):
                    print(f"{i}- {patient[0]} : {patient[1]}")
     # suppr un patient
     elif choice == 4:
          if not patients:
               print(f"Aucun patient pour l'instant")
          else:
               try:
                    patient_index = int(input("Quel est l'index du patient ?: "))
               except ValueError:
                    print(f"Ce choice est invalide ")
                    continue
               
               patient_index -= 1
               if 0 <= patient_index < len(patients):
                    patients.pop(patient_index)
                    print(f"Vous avez supprimé un patient de votre liste ")
               else:
                    print(f"Cet index n'est pas dans la liste")
     # Mettre l'etat d'un patient à jour
     elif choice == 5:
          if not patients:
               print(f"Aucun patient pour l'instant")
          else:
               try:
                    patient_index = int(input("Quel est l'index du patient ?: "))
               except ValueError:
                    print(f"Ce choice est invalide ")
                    continue

               patient_index -= 1
               if 0 <= patient_index < len(patients):
                    patients[patient_index][1] = "Soigné(e)"
                    print(f"Vous avez  mis à jour l'état d'un patient")
               else:
                    print(f"Cet index n'est pas dans la liste")
     elif choice == 6:
          if  not patients :
               print(f"La liste est vide ")
          else:
               found = False
               for i, patient in enumerate(patients, start=1):
                    if patient[1] == "Soigné(e)":
                         print(f"{i}- {patient[0]} : {patient[1]}")
                         found = True
                    if not found:
                         print(f"Aucun patient soigné pour l'instant")

     elif choice == 7:
          if  not patients :
               print(f"La liste est vide ")
          else:
               found = False
               for i, patient in enumerate(patients, start=1):
                    if patient[1] == "Pas soigné(e)":
                         print(f"{i}- {patient[0]} : {patient[1]}")
                         found = True
                    if not found:
                         print(f"Aucun patient pa s soigné pour l'instant")




     