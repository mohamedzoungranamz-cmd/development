products = []

while True:
     print(f"\n 1- Ajouter un produit \n 2- Voir tous les produits \n 3- Voir les 5 derniers produits \n 4- Supprimer un produit \n 5- Modifier le prix d'un produit \n 6- Voir les produits chers (prix > 1000)\n 7- Voir les produits pas chers (prix <= 1000)\n 8- Quitter")

     try :
          choice = int(input("Que voulez-vous faire ?: "))
     except ValueError:
          print(f"Ceci est un choix invalide ")
          continue

     if choice == 1:
          product_name = input("Quel est le nom du produit : ")

          if product_name == "":
               print(f"Vous devez entrer un nom ")
          else:
               if any (product_name == product[0] for product in products):
                    print(f"Ce nom existe déjà dans la liste")
               else:
                    while True:
                         try:
                              product_price = int(input("Quel est son prix ? "))
                              
                              products.append([product_name, product_price])
                              print(f"Vous avez ajouté un produit")
                              break
                         except ValueError:
                              print(f"Ceci n'est pas un prix")
                              continue
     elif choice == 2:
          if not products:
               print(f"Aucun produit pour l'instant")
          else:
               for i, product in enumerate(products, start=1):
                    print(f"{i}- {product[0]} : {product[1]} Fcfa")

     elif choice == 3:
          if not products:
               print(f"Aucun produit pour l'instant")
          else:
               for i, product in enumerate(products[-5:], start=1):
                    print(f"{i}- {product[0]} : {product[1]} Fcfa")

     elif choice == 4:
          if not products:
               print(f"Votre liste est vide")
          else:
               try:
                    product_index = int(input("Quel est l'index du produit "))
               except ValueError:
                    print(f"Ceci n'est pas un index")
               product_index -= 1

               if 0 <= product_index < len(products):
                    products.pop(product_index)
                    print(f"Vous avez supprimé un produit")
               else:
                    print(f"Cet index n'existe pas la liste ")
          
     elif choice == 5:
          if not products:
               print(f"Votre liste est vide")
          else:
               try:
                    product_index = int(input("Quel est l'index du produit "))
               except ValueError:
                    print(f"Ceci n'est pas un index")
               product_index -= 1
               
               if 0 <= product_index < len(products):
                    while True:
                         try:
                              product_price = int(input("Indiquer le nouveau prix ? "))
                              for product in products:
                                   products[product_index][1] = product_price
                              
                              print(f"Vous avez mis à jour le prix  d'un produit")
                              break
                         except ValueError:
                              print(f"Ceci n'est pas un prix")
                              continue
                    
               else:
                    print(f"Cet index n'existe pas la liste ")
          
     elif choice == 6:
          if not products:
               print(f"Votre liste est vide")
          else:
               found = False
               for i, product in enumerate (products, start=1):
                    if product[1] > 1000:      
                         print(f"{i}- {product[0]} : {product[1]} Fcfa")
                         found = True

               if not found :
                    print(f"Aucun produit cher") 


     elif choice == 7:
          if not products:
               print(f"Votre liste est vide")
          else:
               found = False
               for i, product in enumerate (products, start=1):
                    if product[1] <= 1000:      
                         print(f"{i}- {product[0]} : {product[1]} Fcfa")
                         found = True

               if not found :
                    print(f"Aucun produit pas cher") 


          



                         