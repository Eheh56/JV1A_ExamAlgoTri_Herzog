#1Nous allons avoir besoin de permuter deux valeurs d’un tableau à partir de leurs indices.
#Écrire un programme permettant de permuter deux valeurs du tableau myTable.


myTable = [7, 5, 6, 9, 2]
sauvegarde = 0

print(myTable)
sauvegarde = myTable[1]
myTable[1] = myTable [3]
myTable[3] = sauvegarde
print(myTable)

