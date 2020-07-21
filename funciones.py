
def menu(opciones,titulo):
    print('*'*20)
    print('{}'.format(titulo))
    print('*'*20)
    for op in range(0,len(opciones)):
        print("{}){}".format(op, opciones[op]))
    op= input('ELIJA UNA OPCIÓN[0...{}]: '.format(len(opciones)-1))
    return op


def soloLetra(cadena):
    try:
        str(cadena)
        return True
    except(TypeError,ValueError):
        return False


