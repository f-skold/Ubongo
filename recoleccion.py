from random import randint
import heapq as pq

gemas = [        [2, 4, 5, 3, 5, 3, 3, 1, 4, 6, 6, 2],
                 [2, 2, 6, 2, 1, 2, 6, 4, 4, 5, 1, 3],
                 [5, 4, 4, 4, 5, 3, 2, 1, 5, 5, 4, 3],
                 [2, 5, 4, 2, 5, 1, 6, 2, 4, 2, 6, 5],
                 [5, 3, 1, 5, 3, 1, 1, 3, 2, 4, 5, 5],
                 [1, 3, 5, 3, 1, 1, 6, 6, 6, 4, 6, 2]]

ocur = [[0 for i in range(6)]for j in range(6)]

for i in range(len(gemas)):
    for j in gemas[i]:
        ocur[i][j-1] +=1

pc = []
pc_ocur = [0 for i in range(7)]
pos = 0
mov = 2

for i in range(9):
    if(i == 0):
        mayor = []
        for j in range(pos-mov, pos+mov+1):
           if(j >=0 and j <6):
               ult = len(gemas[j])-1
               peult = len(gemas[j])-2
               alt1 = ocur[j][gemas[j][ult]-1]
               alt2 = ocur[j][gemas[j][peult]-1]
               entra = [alt1+alt2,j]
               pq.heappush(mayor, entra)
               
        pos = mayor.pop()[1]
        ult = len(gemas[pos])-1
        peult = len(gemas[pos])-2
        entra1 = [1,gemas[pos].pop(peult)]
        entra2 = [1,gemas[pos].pop(ult)]
        pc_ocur[entra1[1]] = 1
        pc_ocur[entra2[1]] = 1
        pq.heappush(pc,entra1)
        pq.heappush(pc,entra2)
        print(pc)
    else:
        for j in range(pos-mov, pos+mov+1):
            mayor = 0
            if(j >= 0 and j < 6):
                ult = len(gemas[j])-1
                peult = len(gemas[j])-2
                 
                
        
        
print(gemas)
print()
print(ocur)