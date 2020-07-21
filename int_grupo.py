import os
from ctrGrupo import *
from md_Grupo import *
from funciones import *
ctr= ctrGrupo()

def Insertar(rango):
    for i in range(int(rango)):
        grupo= input('Ingrese Grupo: ')
        if grupo.isalpha():
            modelo= md_Grupo(desc=grupo)
            if ctr.Ingresar(modelo):
                print("Registro grabado correctamente")
            else:
                print("Error al grabar el registro")
        else:
            print("Error en la lectura de datos,intente nuevamente")

def Modificar():
    id = input('Ingrese Id: ')
    grupo = input('Ingrese grupo a modificar: ')
    if grupo.isalpha() and id.isdigit():
        modelo = md_Grupo(codigo=id, desc=grupo)
        if ctr.Modificar(modelo):
            print("Registro Modificado correctamente")
        else:
            print("Error al Modificar el registro")
    else:
        print("Error ingrese correctamente")

def Eliminar():
    id = input('Ingrese Id: ')
    if  id.isdigit():
        modelo = md_Grupo(codigo=id)
        if ctr.Eliminar(modelo):
            print("Registro Eliminado correctamente")
        else:
            print("Error al Eliminar el registro")
    else:
        print("Error ingrese correctamente")

def Consultar():
    buscar = input('Ingrese nombre a buscar: ')
    modelo = ctr.Consultar(buscar)
    print("CODIGO   GRUPO")
    for registo in modelo:
        print('{:7} {:5}'.format(registo[0], registo[1]))


def ejecutarGrupo():
    while True:
        opc = str(menu(('INGRESAR', 'MODIFICAR','ELIMINAR','CONSULTAR', 'REGRESAR AL MENU PRINCIPAL'), 'MENÚ GRUPO'))
        if opc == '0':
            print('<<<INSERTAR DATOS>>>')
            valor = input('Ingrese cantidad : ')
            if valor.isdigit():
                Insertar(valor)
            else:
                print("Error ingrese correctamente...")
        elif opc == '1':
            print('MODIFICAR ...')
            Modificar()
        elif opc == '2':
            print('ELIMINAR..')
            Eliminar()
        elif opc == '3':
            print('CONSULTAR...')
            Consultar()
        elif opc == '4':
            break
        elif opc != '4':
            print('Seleccione una opción correcta... ')
        input("PRECIONE UNA TECLA PARA CONTINUAR...")
        os.system('cls')




