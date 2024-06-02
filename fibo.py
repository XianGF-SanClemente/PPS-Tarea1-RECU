def get_fibonacci(N):

#comprobar si N es 0,1,2
    if (N<=0):
        return None
    elif (N==1):
        return [0]
    elif (N==2):
        return [0,1]
#si N es mayor o igual a 3 empezar fibonacci en 0,1,1
    fibonacci = [0,1,1]
#for -3 porque no se empieza el array desde 0
    for i in range(N-3):
    #adjunta al array el resultado de la formula Fn = (Fn−1) + (Fn−2)
        fibonacci.append(fibonacci[-1]+fibonacci[-2])

    #devuelve el array con la secuencia fibonacci
    return fibonacci
