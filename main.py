import os 

python_files={
    1:"backtracking.py",
    2:"vegas.py",
    3:"heuristica.py"
}

print('\nProblemas de las N-Reinas \n ')
print('Eliga que estrategia utilizar para resolver el Algoritmo')
print("""
      1-) Backtracking
      2-) Las Vegas
      3-) Heuristica  
""")

opcion=int(input("Opcion:"))
while(opcion not in [1,2,3]):
    opcion=int(input("Opcion:"))

file=python_files[opcion]
os.system('python '+file)
