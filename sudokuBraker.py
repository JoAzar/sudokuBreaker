#sudoku=[[0, 0, 0,  0, 0, 0,  0, 0, 0],
#        [0, 0, 0,  0, 0, 0,  0, 0, 0],
#        [0, 0, 0,  0, 0, 0,  0, 0, 0],
#
#        [0, 0, 0,  0, 0, 0,  0, 0, 0],
#        [0, 0, 0,  0, 0, 8,  0, 0, 0],
#        [0, 0, 0,  0, 0, 0,  0, 0, 0],
# 
#        [0, 0, 0,  0, 0, 0,  0, 0, 0],
#        [0, 0, 0,  0, 0, 0,  0, 0, 0],
#        [0, 0, 0,  0, 0, 0,  0, 0, 0]]

sudoku=[[0, 9, 4,  1, 0, 0,  0, 0, 0],
        [3, 0, 0,  0, 0, 6,  4, 5, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 8],

        [2, 0, 0,  0, 0, 0,  0, 0, 7],
        [0, 0, 1,  6, 0, 8,  8, 2, 0],
        [0, 0, 0,  0, 0, 8,  0, 0, 3],
 
        [0, 0, 3,  0, 5, 0,  0, 0, 0],
        [5, 0, 0,  0, 0, 4,  2, 6, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0]]

def printSudo(sudoku):
    for l in sudoku:
        print(l)

#contraar_coordenada_grid
def encontrarValor(val):
    if val<=2:
        return 0
    elif val<=5:
        return 1
    else:
        return 2

#resolver_sudoku y x
def graficarSudoku(sudoku):
    for i in range(9):
        for j in range(9):
           if sudoku[i][j]==0:
                for val in range(1,10):
                    if valido(j, i, val, sudoku):
                        sudoku[i][j] = val
                        graficarSudoku(sudoku)
                        sudoku[i][j]=0
                return
    printSudo(sudoku)
    return

#es_posible
def valido(j, i, v, sudoku):
    #revisar fila
    if v in sudoku[i]:
        return False
    #revisar columna
    col=[fila[j] for fila in sudoku]
    if v in col:
        return False
    cuadrito3x3=obtenerCuadrito(j, i, sudoku)
    if v in cuadrito3x3:
        return False
    return True

def obtenerCuadrito(j, i, sudoku):
    guardoCol=encontrarValor(j)
    guardoFila=encontrarValor(i)
    cuadro=[]
    for fila in sudoku[guardoFila*3: guardoFila*3+3]:
        for col in fila[guardoCol*3: guardoCol*3+3]:
            cuadro.append(col)
    return cuadro

graficarSudoku(sudoku)