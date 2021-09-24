print('1. structures de contrôle : boucle for')
print('1.1 Écrire un programme qui écrit 50 fois « facile ! »')

for i in range(50):
    print("facile ! ")

print('1.2 Afficher 25 étoiles « * » sur une ligne (avec une boucle )')
end= '\n'

for i in range(25):
    print("*", end='')

print('1.3 Afficher tous les entiers de 21 à 145 avec une boucle for')

for i in range (21, 146):
  print(i)

print('1.4 Afficher le carré de i avec i variant de 1 à 40 et affiche « le carre de 1 = 1 », « le carre de 2=4 »... « le carré de 40 = 1600 »')

for i in range (1, 41):
  print("le carre de " + str(i) + " = " + str(i**2))

print('1.5 Calculer la somme de tous les entiers de 21 à 145 puis l’afficher')

somme = 0
for i in range (21, 146):
  somme += i

print('La somme de tous les entiers de 21 à 145 est' , somme)

print('1.6 Calculer 35! (factorielle).')

factorielle = 1
for i in range (1, 36):
  factorielle = i * factorielle

print('La factorielle de 35 est' , factorielle)

print("1.7 Afficher un triangle rectangle composé d'étoiles « * » dont la largueur du côté est 15 * :")

for i in range(1, 15 + 1, 1):
    print(i*'*')

print('2. structures de contrôle : boucle while')
print('2.1 remplissage de dictionnaire')

dicoAF = {}
saisie = 'o'

while (saisie == 'o'):
    eng = input("Mot anglais: ")
    fr = input("Mot francais: ")
    dicoAF[eng] = fr
    saisie = input("Voulez vous continuer ? o ou autre touche pour stopper")

print('Taille du dico : {0}'.format(len(dicoAF)))

for k, v in dicoAF.items():
    print(k, v)

print('2.2 remplissage de dictionnaire : variante')

dicoAF = {}
saisie = 'o'
while (saisie == 'o'):
    eng = input("Mot anglais: ")
    fr = input("Mot francais: ")
    if eng[0] == '$' or fr[0] == '$':
        break
    dicoAF[eng] = fr

print('Taille du dico : {0}'.format(len(dicoAF)))

for k, v in dicoAF.items():
    print(k, v)

print('2.3 remplissage de dictionnaire : amélioration')
dicoAF = {}
saisie = 'o'
while (saisie == 'o'):
    eng = input("Mot anglais: ")
    fr = input("Mot francais: ")
    if eng[0] == '$' or fr[0] == '$':
        break
    dicoAF[eng] = fr

print('Taille du dico : {0}'.format(len(dicoAF)))

for k, v in dicoAF.items():
    print(k, v)
if len(dicoAF) <= 1:
    print('le dictionnaire contient {0} entrée'.format(len(dicoAF)))
else:
    print('le dictionnaire contient {0} entrées'.format(len(dicoAF)))

print('2.4 Construction d’un dictionnaire français anglais')

dicoFA = {v: k for k, v in dicoAF.iteritems()}

print(dicoAF)
print(dicoFA)