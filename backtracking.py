#librerias
import array
import copy
import timeit

#variables globales
N=4
list_solution=[]
visited_nodes=0



def draw_solution(list_solution):
    for i in range(len(list_solution)):
        print("Esta es la solucion nr:",i+1,"\n")
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


def findQuenSolution(quen_colum,quen_positions):
    """Encuentra una unica solucion para el problema de las N-Reinas"""

    if(quen_colum==N):
        return 

    global visited_nodes
    
    for row_quen in range(N):
        visited_nodes+=1 #aumentamos la cantidad de nodos expandidos

        if (is_valid(row_quen,quen_colum,quen_positions)):
            quen_positions[quen_colum]=row_quen
            array_solution=findQuenSolution(quen_colum+1,quen_positions)
            if( not -10 in quen_positions):
                return 
    
    quen_positions[quen_colum]=-10
    return 


def findAllQuenSolution(quen_colum,quen_positions):    
    """Encuentra todas las soluciones para el problema de las N-Reinas"""

    if(quen_colum==N):
        global list_solution
        list_solution.append(copy.deepcopy(quen_positions))
        return
   
    global visited_nodes
    for row_quen in range(N):
        visited_nodes+=1
        if (is_valid(row_quen,quen_colum,quen_positions)):
            quen_positions[quen_colum]=row_quen
            array_solution=findAllQuenSolution(quen_colum+1,quen_positions)
    
    quen_positions[quen_colum]=-10
    
    return

        

def n_quen():
    global N
    N=int(input("Ingrese el tamaño de N:")) 
    if(N<4):
        print("N debe ser de un tamaño mayor que 4")
        return
    
    quen_positions=array.array('i',[ -10 for i in range(N)]) #inicializamos el array de posiciones con valores -1 

    print(" Seleccione una de las opciones: \n  Opcion 1: Encontrar una unica Solucion \n Opcion 2: Encotrar todas las soluciones     ")
    option=int(input("Ingrese la Opcion(1 o 2):"))
   
    
    if(option==1):
        start = timeit.default_timer()
        findQuenSolution(0,quen_positions)
        stop = timeit.default_timer()
        print("\n\nSolucion : ")
        draw_solution([quen_positions])
        print('Cantidad de nodos Expandidos:',visited_nodes)
        print('Tiempo en encontrar solucion: ', stop - start, 'segundos')  

    
    elif(option==2):
        start = timeit.default_timer()
        findAllQuenSolution(0,quen_positions)
        stop = timeit.default_timer()
        print('Las soluciones encontradas son :')
        draw_solution(list_solution)
        print('Cantidad de soluciones Encontradas:', len(list_solution))
        print('Cantidad de nodos Expandidos:',visited_nodes)
        print('Tiempo en encontrar todas las soluciones: ', stop - start, 'segundos')  
     
    else:
        print("Opcion ingresada no valida") 
    

n_quen()
#draw_solution([[1,3,0,2]])


