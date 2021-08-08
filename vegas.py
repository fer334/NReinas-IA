#librerias
import array
import copy
import timeit
import random as rd
import time
#variables globales
N=4
list_solution=[]
visited_nodes=0

rd.seed(time.time()) #generar diferente numeros aleatorios

def draw_solution(list_solution):
    """Grafica el Tablero de solucion"""
    for i in range(len(list_solution)):
        print("La solucion encontrada es: \n")
        line=""
        for j in range(len(list_solution[i])):
            newLine="  |"
            for k in range(len(list_solution[i])):
                if(k == list_solution[i][j]):
                    newLine+="  O"
                else :
                    newLine+="  X"
            newLine+="  |\n"
            line+=newLine
        print(line)    
        print('Vector solucion:',list_solution[i].tolist(),'\n' )

def subs(row1,col1,row2,col2):
    """ Verifica si dos Array se atacan en una Diagonal"""
    return True if (abs(row1-row2)==abs(col1-col2)) else False
    

def is_valid(row_quen,colum_quen,quen_positions_aux):
    """Verifica si una nueva reina no es ataca por las demas reinas anteriores"""

    #verificamos que no exista dos reinas en la misma fila
    if row_quen in quen_positions_aux:
         return False

    #verificamos que las reinas no se ataquen en la diagonal
    for quen_position_colum in range(N):
        if(quen_positions_aux[quen_position_colum]!=-10): #verificar que el casillero este ocupado
            if subs(row_quen,colum_quen,quen_positions_aux[quen_position_colum],quen_position_colum):
                return False
        else: #si no esta ocupado retornamos  True
            return True

def calculatePosibleValues(colum_quen,quen_positions):
    """Funcion que calcula el dominio de valores posibles"""
    result=[]
    for row_quen in range(N):
        if is_valid(row_quen,colum_quen,quen_positions):
            result.append(row_quen)
    return result
#quen position == solution
#no es necesario crear array_solution

def findQuenSolution(quen_colum,quen_positions,posible_values):
    """Encuentra una unica solucion para el problema de las N-Reinas"""

    """ 
    Valores que se van eligiendo en cada llamada
    print('quen position',quen_positions)
    print('posible values',posible_values)
    print('column',quen_colum)
    """

    if(quen_colum==N):  #encontre un solucio
        return 

    if len(posible_values)==0: #la varaiable de desicion se quedo sin valores posibles que tomar
        return 
    
    posible_values_aux=copy.deepcopy(posible_values)
    global visited_nodes

    while ( len(posible_values_aux)!=0):
        visited_nodes+=1 #cantidad de nodos visitados

        random_position=rd.randint(0,len(posible_values_aux)-1) #generamos los valores aleatorios
        quen_positions[quen_colum]=posible_values_aux[random_position] #asignamos la posicion  elegida en el tablero
        posible_values_aux.remove(posible_values_aux[random_position]) #el valor elegido ya eliminamos de las posibles soluciones
        
        next_posible_values=calculatePosibleValues(quen_colum+1,quen_positions)
        array_solution=findQuenSolution(quen_colum+1,quen_positions,next_posible_values)

        if (not -10 in quen_positions):
            return 
    
    quen_positions[quen_colum]=-10

    return        

    
    


        

def n_quen():
    global N
    N=int(input("Ingrese el tamaño de N:")) 

    if(N<4):
        print("N debe ser de un tamaño mayor que 4")
        return
    
    quen_positions=array.array('i',[ -10 for i in range(N)]) #inicializamos el array de posiciones con valores -1 
    posible_values=[ i for i in range(N)] #posibles valores que puede tomar un nodo no Meta
    
    start = timeit.default_timer()
    findQuenSolution(0,quen_positions,posible_values)
    stop = timeit.default_timer()

    print("\n\nSolucion : ")
    draw_solution([quen_positions])
    print('Cantidad de nodos Expandidos:',visited_nodes)
    print('Tiempo en encontrar la solucion: ', stop - start, 'segundos')    
    
          

    

n_quen()
#draw_solution([[1,3,0,2]])


