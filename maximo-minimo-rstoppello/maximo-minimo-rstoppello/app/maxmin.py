maxCalled = 0
minCalled = 0

'''
Este programa indica cual de los numeros es mayor de 2 que recibe
'''


def max_val(a,b):
    '''
    Se utiliza para indicar cual es el numero mayor

    :param a: Primer numero a comparar
    :type a: int


    :param b: Segundo numero a comparar
    :type b: int

    '''
    global maxCalled
    maxCalled = maxCalled + 1
  
    if(a > b):
        return a   
    elif(b > a):
        return b
    else:
        return a

def min_val(a,b):
    '''

    Indica cual es el numero menor de los que recibe

    :param a: Primer numero a comparar
    :type a: int

    :param b: Segundo numero a comparar
    :type b: int

    '''
    global minCalled 
    minCalled = minCalled + 1
  
    if(a < b):
        return a
    elif(b < a):
        return b
    else:
        return a 

def print_usage(init_msg, max_val=True, min_val=True):
    '''
    Indica la cantidad de veces llamadas tinen las funciones max_val y min_val

    :param init_msg: Mensaje
    :type init_msg: str


    '''
    global maxCalled, minCalled
    if max_val:
        print('Funcion max_val fue llamada', maxCalled, ' veces')
    if min_val:
        print('Funcion min_Val fue llamada', minCalled, ' veces')


if __name__ == '__main__':
    print('Ejecutado max_val')
    max_val(5,7)
    max_val(5,b=8)
    max_val(2,a=8)

    print('Calling function min_val')
    min_val(5,7)
    min_val(5,b=8)
    min_val(2,b=8)

    print_usage('The usage of functions min_val and max_val')
