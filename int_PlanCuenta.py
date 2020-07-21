import os
from ctrPlanCuenta import  *
from md_PlanCuenta import *
from funciones import *
ctr= ctrPlanCuenta()

def Insertar(rango):
    for i in range(int(rango)):
        codigo= input('Codigo: ')
        grupo = input('Grupo: ')
        descripcion = input('Descripcion: ')
        naturaleza = input("Ingrese Naturaleza D/A : " )
        estado = input("Ingrese Estado: ")
        if codigo.isdigit() and grupo.isdigit()  and naturaleza.isalpha() and estado.isdigit():
            modelo = md_PlanCuenta(codigo=codigo, grupo=grupo, desc=descripcion, naturaleza=naturaleza,
                                      estado=estado)
            if ctr.Ingresar(modelo):
                print("Registro grabado correctamente")
            else:
                print("Error al grabar el registro")
        else:
            print("Error en la lectura de datos")


def Modificar():
    id = input('Id: ')
    codigo = input('Codigo : ')
    grupo = input(' Grupo : ')
    descripcion = input(' Descripcion : ')
    naturaleza = input("Ingrese Naturaleza: D/A :")
    estado = input("Ingrese Estado: ")
    if id.isdigit() and codigo.isdigit() and grupo.isdigit()  and naturaleza.isalpha() and estado.isdigit():
        modelo = md_PlanCuenta(id=id, codigo=codigo, idGrupo=grupo, desc=descripcion, naturaleza=naturaleza,
                                  estado=estado)
        if ctr.Modificar(modelo):
            print("Registro Modificado correctamente")
        else:
            print("Error al Modificar el registro")
    else:
        print("Error en la lectura de datos")


def Eliminar():
    id = input('Id: ')
    if id.isdigit():
        modelo = md_PlanCuenta(id=id)
        if ctr.Eliminar(modelo):
            print("Registro Eliminado correctamente")
        else:
            print("Error al Eliminar el registro")
    else:
        print("Error en la lectura de datos")

def Consultar():
    buscar = input('Ingrese nombre a buscar: ')
    modelo = ctr.Consultar(buscar)
    print("ID  CODIGO  GRUPO  DESCRIPCIóN   NATURALEZA  ESTADO")
    for registo in modelo:
         print(
            '{:2} {:4} {:6}{:8}{:10}{:12}'.format(registo[0], registo[1], registo[2], registo[3],registo[4], registo[5]))
def ejecutarPlanCuenta():
    while True:
        opc = str(menu(('INGRESAR', 'MODIFICAR','ELIMINAR','CONSULTAR', 'REGRESAR AL MENU PRINCIPAL'), 'MENÚ PLAN CUENTA'))
        if opc=='0':
            print('<<<INSERTAR')
            valor=input('Ingrese cantidad de datos a ingresar ')
            if valor.isdigit():
                Insertar(valor)
            else:
                print("Error en la lectura de datos")
        elif opc=='1':
            print('MODIFICAR ')
            Modificar()
        elif opc=='2':
            print('ELIMINAR ')
            Eliminar()
        elif opc=='3':
            print('CONSULTAR')
            Consultar()
        elif opc=='4':
            break
        elif opc!='4':
            print('Seleccione una opción correcta... ')
        input("PRECIONE UNA TECLA PARA CONTINUAR...")
        os.system('cls')


