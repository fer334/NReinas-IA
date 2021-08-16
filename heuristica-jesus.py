import random as rd
import time
import array
import timeit


###Variables Globales
P=[] #matriz de Pesos
N=5 #tamaño de N
visited_nodes=0


rd.seed(time.time())

def draw_solution(list_solution):
    """Grafica el Tablero de solucion"""

    for i in range(len(list_solution)):
        print("La solucion encontrada es: \n")
        line=""
        if(N<=40):
            for j in range(len(list_solution[i])):
                newLine="  |"
                for k in range(len(list_solution[i])):
                    if(k == list_solution[i][j]):
                        newLine+="  R"
                    else :
                        newLine+="  -"
                newLine+="  |\n"
                line+=newLine
            print(line)    
        print('Vector solucion:',list_solution[i].tolist(),'\n' )

def generateInitialState():
    """Funcion que genera mi Estado Inicial, seteando matriz de conflictos, vector Posiciones y valor ant"""
    #genero mis posiciones aleatoriamente
    positions=array.array('i',[rd.randint(0,N-1) for j in range(N)])
    positions_conflict=array.array('i',[ -N for j in range(N)])
    #genero mi matriz de Pesos
    for i in range(N):
        setAndUnsetPesos(positions[i],i,1)

    return (positions,-N,positions_conflict)

def setAndUnsetPesos(currentRow,correntCol,c):
    """Funcion que suma o Resta los conflictos que genera una reina en una pocision (i,j)"""
    global P
    for i in range (1,N,1):
        nextCol,nextRow,prevRow,prevCol=(correntCol+i,currentRow+i,currentRow-i,correntCol-i)
        
        if(nextCol<=N-1):
            P[currentRow][nextCol]+=c #misma fila hacia la derecha
            if(nextRow<=N-1):
                P[nextRow][nextCol]+=c  #recorrer diagonal secundiria  arriba-derecha 
            if (prevRow>=0):
                P[prevRow][nextCol]+=c #recorrer diagonal premaria abajo-derecha
        if(prevCol>=0):
            P[currentRow][prevCol]+=c #misma fila hacia la izquierda
            if(nextRow<=N-1):
                P[nextRow][prevCol]+=c  #recorrer diagonal secundiria  arriba-izquierda 
            if (prevRow>=0):
                P[prevRow][prevCol]+=c #recorrer diagonal primaria abajo-derecha

def is_valid(positions_conflict):
    """Valido que mis posiciones sean validas, si todas mis varibles tienen conflicto 0, llegue a una solucion"""
    for i in range(N):
        if positions_conflict[i]!=0: 
            return False

    return True

def getConflictVars(base):
    """Funcion que me devuelve todas mis variables que generan minimo conflictos"""
    result=[]
    min=N
    for i in range (N):
        for j in range (N): #Este reccorrido lo hago por columnas, primero toda la columna Xi luego Xi+1
            if P[j][i]>base:
                if(P[j][i]<min): ## si encuentro un Peso de conflicto Minimo del que ya tenia
                    result=[]
                    result.append(i)
                    min=P[j][i]
                elif P[j][i]==min: #si encuentro uno que es igual, agrego si es que ya no lo agregue anteriormente
                    if i not in result:
                        result.append(i)
    return (result,min)

def getValues(col,min):
    """Obtiene las filas que tienen valores minimos en  mi variable elegida (col) """
    resulset=[]
    for i in range(N):
        if(P[i][col]==min):
            resulset.append(i)
    return resulset

def findMinConf():
    positions,ant,positions_conflict=generateInitialState()
    global P, visited_nodes
    min=-N
    while (not is_valid(positions_conflict)):
    #for cont in range(50): 
       visited_nodes+=1 #Aumentamos a 1 la cantidad de nodos visitados
       vars,min =getConflictVars(-N)
       #print("vars:",vars,"min:",min)
       try:
            vars.remove(ant) #elimino mi variable anterior para no elegir mas esa
       except Exception: 
           pass

       while(len(vars)==0):
           vars,min=getConflictVars(min)

       varCol=vars[rd.randint(0,len(vars)-1)]
       vars.remove(varCol)

       currentRow=positions[varCol]
       values=getValues(varCol,min)
       try:
           values.remove(currentRow) #eliminos de los valores posibles, la posicion en donde ya estoy
       except Exception:
           pass

       while(len(values)==0):
            if(len(vars)==0):
                vars,min=getConflictVars(min)
            
            varCol=vars[rd.randint(0,len(vars)-1)]
            vars.remove(varCol)
            currentRow=positions[varCol]
            values=getValues(varCol,min)
            try:
                values.remove(currentRow)
            except Exception:
                pass

       nextRow=values[rd.randint(0,len(values)-1)] #elijo aleatoriamente una de las variable
       setAndUnsetPesos(currentRow,varCol,-1)
       setAndUnsetPesos(nextRow,varCol,1)
       positions_conflict[varCol]=min
       positions[varCol]=nextRow
       ant=varCol
       if is_valid(positions_conflict): return positions

    return positions


M=[]
def main():

    print("\n -----------------Heuristica----------------- \n")
    global N
    N=int(input("Ingrese el tamaño de N:")) 
    if(N<4):
        print("N debe ser de un tamaño mayor que 4")
        return
    global P
    for i in range(N) : #inicializo todo a cero mi matriz de Pesos
        P.append([ 0 for j in range(N)])


    start = timeit.default_timer()
    result=findMinConf()
    position,n,pe=generateInitialState()
    stop = timeit.default_timer()
    print("\n\n")
    draw_solution([result])
    print('Cantidad de nodos Expandidos:',visited_nodes)
    print('Tiempo en encontrar la solucion: ', stop - start, 'segundos')  


main()



