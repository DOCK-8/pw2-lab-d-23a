import esEscalar as fun

def prueba(M):
    if(fun.esEscalar(M)):
        print("Si es escalar")
    else:
        print("No es escalar")
        
#Z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Z = [[1, 2, 3], [4, 1, 6], [7, 8, 1]]
Z = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
prueba(Z)