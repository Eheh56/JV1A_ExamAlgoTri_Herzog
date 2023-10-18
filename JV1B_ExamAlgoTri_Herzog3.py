#    3/ Écrire un programme implémentant le tri à bulles complet, permettant de trier totalement
#    un tableau grâce à l’algorithme du tri à bulles. On pourra se servir de la permutation, ainsi
#    que de la réponse à la question précédente.


myTable = [7, 5, 9, 6, 4]
nmbPetit = 0
sauvegarde = 0
indice = 0

print(myTable)
for i in range(1,len(myTable)):
    nmbPetit = myTable[i-1]
    for j in range(i,len(myTable)):
        if(myTable[j]< nmbPetit):
            nmbPetit = myTable[j]
            indice = j
    if(nmbPetit != myTable[i-1]):
        sauvegarde = myTable[i-1]
        myTable[i-1] = nmbPetit
        myTable[indice] = sauvegarde

print(myTable)
