#2/     Lors d’une seule itération, l'algorithme du tri à bulles parcourt le tableau, et compare les
#       éléments consécutifs. Lorsque deux éléments consécutifs ne sont pas dans l'ordre, ils sont
#       échangés. Par conséquent, à l’issue d’une itération (et donc, d’un parcours entier du
#       tableau), le plus grand élément est systématiquement déplacé en fin de tableau ; comme s’il
#       s’agissait d’une bulle qui remonte à la surface.

myTable = [7, 5, 9, 6, 4]
sauvegarde = 0
print(myTable)

for i in range(len(myTable)-1):
    if(myTable[i]>myTable[i+1]):
        sauvegarde = myTable [i]
        myTable[i] = myTable[i+1]
        myTable[i+1] = sauvegarde
print(myTable)

