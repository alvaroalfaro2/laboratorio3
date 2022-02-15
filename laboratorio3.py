#!/usr/bin/python3

class Vector():
    def __init__(self, m):
        self.m = int(m)
        list = []
        for i in range(m):
            list.append(0)
        self.vec = list


class Matriz():
    '''
    Esta clase define matrices de tamaño nxm
    '''
    def __init__(self, n, m):

        self.n = int(n)
        self.m = int(m)
      
        # se crea una lista vacía
        list = []
        # se añaden n objetos vector a la lista
        for i in range(n):
            list.append(Vector(m))
        # se define esta lista como un atributo
        self.filas = list

    def __str__(self):

        filas = self.filas
        matriz = []
        # mediante el siguiente for se contruye una matriz como una lista
        for object in filas:
            matriz.append(object.vec)
        n = self.n
        m = self.m
        # defino un string vacío
        string = ''
        # añado todos los elementos de la matriz donde cada línea es una
        # fila de la matriz
        for a in range(n):
            for b in range(m):
                if b != m - 1:
                    string = string + str(matriz[a][b]) + ' '
                elif a != n-1:
                    string = string + str(matriz[a][b]) + '\n'
                else:
                    string = string + str(matriz[a][b])
        return string

    def __add__(self, other):

        n = self.n
        m = self.m
        n_other = other.n
        m_other = other.m

        # se revisa si las dimensiones de ambas
        # matrices son iguales
        if (n != n_other or m != m_other):
            print('Las matrices a sumar deben ser del mismo tamaño')
            raise Exception

        matriz_suma = Matriz(n, m)

        for a in range(n):
            for b in range(m):

              matriz_suma[a][b] = self[a][b] + other[a][b]

        return matriz_suma

    def __sub__(self, other):

        n = self.n
        m = self.m
        n_other = other.n
        m_other = other.m

        # se revisa si las dimensiones de ambas
        # matrices son iguales
        if (n != n_other or m != m_other):
            print('Las matrices a restar deben ser del mismo tamaño')
            raise Exception

        matriz_resta = Matriz(n, m)

        for a in range(n):
            for b in range(m):
              matriz_resta[a][b] = self[a][b] - other[a][b]

        return matriz_resta

    def __getitem__(self, index):

        filas = self.filas
        matriz = []
        # se construye una matriz como una lista
        for object in filas:
            matriz.append(object.vec)
        # se ingresan los índices como una variable index que contiene ambos
        # índices
        return matriz[index]


if __name__ == '__main__':

  print('se esta creando una matriz nxm')
  n = int(input('ingrese el valor de n: '))
  m = int(input('ingrese el valor de m: '))
  
  matriz_1 = Matriz(n, m)
  print('Una matriz {}x{} de ceros:'.format(n,m))
  print(matriz_1)

  valor_ingresar = input('Ingrese el valor a ingresar en la matriz[1][1] para probar metodo __getitem__: ')

  try :
    float(valor_ingresar)
    matriz_1[1][1] = valor_ingresar

    valor_revisar = matriz_1[1][1]
    print('Accediendo al elemento (1,1):')
    print(valor_revisar)

    matriz_2 = Matriz(n, m)

    for a in range(n):
      for b in range(m):
          matriz_1[a][b] = 1
          matriz_2[a][b] = 2

    matriz_3 = matriz_1 + matriz_2
    print('matriz de 1\'s + matriz de 2\'s:')
    print(matriz_3)

    matriz_4 = matriz_1 - matriz_2
    print('matriz de 1\'s - matriz de 2\'s:')
    print(matriz_4)
  
  except ValueError:
    print('El valor ingresado no es un float')
