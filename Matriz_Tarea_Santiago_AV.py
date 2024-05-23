matriz = [['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-']]
correcto = '◉'
incorrecto = '☢'
import os
def fnt_limpiar():
    os.system('cls')
    print('\n\n')
    fnt_impresion()
    print('\n\n')

def fnt_agregar(x, y):
    if x == 0 and y == 0:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 0 and y == 1:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 0 and y == 2:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 0 and y == 3:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 0 and y == 4:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 1 and y == 0:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 1 and y == 1:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 1 and y == 2:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 1 and y == 3:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 1 and y == 4:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 2 and y == 0:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 2 and y == 1:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 2 and y == 2:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 2 and y == 3:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 2 and y == 4:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 3 and y == 0:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 3 and y == 1:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 3 and y == 2:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 3 and y == 3:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 3 and y == 4:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 4 and y == 0:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 4 and y == 1:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    elif x == 4 and y == 2:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 4 and y == 3:
        if matriz [x][y] == '-':
            matriz [x][y] = buena.upper()
    elif x == 4 and y == 4:
        if matriz [x][y] == '-':
            matriz [x][y] = mala.upper()
    
def fnt_impresion():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()

sw = True
while sw == True:
    import os
    os.system('cls')
    fnt_impresion()
    fnt_agregar(int(input('fila: ')), int(input('columna: ')))
