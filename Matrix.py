# Matrix algorithm 
# Autor: Joao Luis

def matrix(rows, coluns):
    ''' (int, int) create, print and return a matrixwith x rows and y coluns Ex: matrix(2,2) = Matrix 2x2
    '''
    m1 = []
    for i in range(rows):
        i_m1 = []
        for j in range(coluns):
            value = int(input(f"Type it the element i[{i+1}]j[{j+1}] of the matrix: "))
            i_m1.append(value)
        m1.append(i_m1)
    print("The matrix is: ")
    print("-"*30)
    print("-", " "*coluns*6,("\b-"))
    print("|","|"'\n| '.join([''.join(['{:^6}'.format(item) for item in row]) for row in m1]),"\b|")
    print("-", " "*coluns*6,("\b-"))
    print("-"*30)       
    return m1
matrix(2,2)