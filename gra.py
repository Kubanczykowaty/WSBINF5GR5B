import random
print("Zagrajmy w gre!\n wylosowalem liczbe od 0-10, a ty musisz ja zgadnac")
x = random.randint(0, 10)
z = 1
while z <= 9:
  print("Podejscie ",z)
  try:
      liczba = int(input("Podaj liczbe:\n"))
      if liczba == x:
        print("Gratuluje")
        break
      elif liczba > x:
        print("za duzo\n")
        z=z+1
      else:
        print("Za malo\n")
        z=z+1
  except ValueError:
      print("To nie jest liczba")