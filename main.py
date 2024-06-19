
def calcul(nbr,conversion):

  if conversion == 'C':
    celsius = (nbr - 32) /1.8 
    print("Temperature en Celsius : " + str(celsius)) 

  else:
    Fahrenheit = (nbr * 1.8) + 32
    print("Temperature en Fahrenheit : " + str(Fahrenheit)) 


nbr = input("entrer un chiffre : ")
try:
  nbr = int(nbr)
  conversion = str(input("Choisissez votre conversion C pour Celsius, F pour Fahrenheit : "))
  conversion = conversion.upper()
  print(conversion)
  if (conversion != 'F') and (conversion != 'C'):
    print("merci d'entrer uniquement C ou F")
  else:
    calcul(nbr,conversion)
except:
  print("Merci d'entrer uniquement un chiffre")

