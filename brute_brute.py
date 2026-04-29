import itertools 
import string 
import time

password = "mohamed07"

characters = string.ascii_lowercase + string.digits

start = time.time()
attempts = 0
max_attempts = 500_000_000

for length in range(1,7):
     for combo in itertools.product(characters, repeat=length):
          guess = ''.join(combo)
          attempts += 1

          if attempts % 10000 == 0:
               print(f"{attempts} essais...")

          if guess == password:
               print(f"\n Mot de passe trouvé : {guess}")
               print(f"Essais : {attempts}")
               print(f"Temps : {time.time()-start: 2f}s")
               exit()
          if attempts == max_attempts:
               print(f"\n Limite atteinte ")
               print(f"Temps: {time.time()-start: 2f}s")
               exit()