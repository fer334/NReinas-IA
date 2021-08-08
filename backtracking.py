import array
#import numpy as np
N=4

def subs(row1,col1,row2,col2):
    return True if (abs(row1-row2)==abs(col1-col2)) else False
    

def is_valid(row_quen,colum_quen,quen_positions_aux):
    #verificamos que no exista dos reinas en la misma fila
    if row_quen in quen_positions_aux:
         return False
    #[2,0,3,-10]
    #verificamos que las reinas no se ataquen en la diagonal
    for quen_position_colum in range(N):
        if(quen_positions_aux[quen_position_colum]!=-10): #verificar que el casillero este ocupado
            if subs(row_quen,colum_quen,quen_positions_aux[quen_position_colum],quen_position_colum):
                return False
        else: #si no esta ocupado retornamos  True
            return True


def putQuen2(quen_colum,quen_positions,solution):
    
    if(quen_colum==N):
        return solution

    #print(quen_positions_aux)
    print('para colum ',quen_colum,'position=',quen_positions,' solution=',solution)
    for row_quen in range(N):
        if (is_valid(row_quen,quen_colum,quen_positions)):
            quen_positions[quen_colum]=row_quen
            solution[quen_colum]=row_quen
            array_solution=putQuen(quen_colum+1,quen_positions,solution)
            if( not -10 in array_solution):
                return array_solution
    
    quen_positions[quen_colum]=-10
    solution[quen_colum]=-10
    return solution



def putQuen(quen_colum,quen_positions,solution):
    
    if(quen_colum==N): #ya coloque todas las reinas, tengo una solucion
        return solution

    colum=quen_colum
    quen_positions_aux=[quen_positions[i] for i in range(N)]
    solution_aux=[solution[i] for i in range(N)]
    #print(quen_positions_aux)
    print('para colum ',quen_colum,'position=',quen_positions,' solution=',solution)
    for row_quen in range(N):
        if (is_valid(row_quen,colum,quen_positions_aux)):
            quen_positions_aux[quen_colum]=row_quen
            solution_aux[quen_colum]=row_quen
            array_solution=putQuen(colum+1,quen_positions_aux,solution_aux)
            if( not -10 in array_solution):
                return array_solution
    
    solution_aux[quen_colum]=-10
    return solution_aux    
        

def n_quen(n):
    global N
    N=n #definimos el valor de N global
    quen_positions=array.array('i',[ -10 for i in range(N)]) #inicializamos el array de posiciones con valores -1 
    solution=array.array('i',[ -10 for i in range(N)])
    print(putQuen2(0,quen_positions,solution)) #colocamos cada reina en la fila correspondiente


##Prubas de funciones
#array_test=array.array('i',[-10,-10,-10,-10])
#print(is_valid(1,0,array_test))
n_quen(4)
"""
def prueba1(array):
    array[0]=10
    print(array)
    """

#ar=array.array('i',[1,2,3])
#prueba1(ar)
#print(ar)