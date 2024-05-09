matriz = [['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-'], 
          ['-', '-', '-', '-', '-', '-']]
correcto = '◉'
incorrecto = '☢'
ls_preguntas = ['¿Que es python?\n1. Juegos\n2. Lenguaje de programación\n3. Marca de autp\n4. Ninguna de las anteriores',
'¿Que es HTML?\n1. Lenguaje de programación\n2. Marca de gaseosas\n3. Navegador\n4. Perro caliente']
ls_preguntas2 = ['2,1']

def fnt_pintar_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='  ')
            print('\n\n')

contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):    
        import os
        os.system('cls')
        fnt_pintar_matriz()
        print()
        print(ls_preguntas[contador])
        print()
        r = input('->')
        if r == ls_preguntas[contador]:
            matriz[i][j] = correcto
        else:
            matriz[i][j] = incorrecto
        contador += 1 