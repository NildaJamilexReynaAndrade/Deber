from DaoPlanCuenta import *
from md_PlanCuenta import *

class ctrPlanCuenta:
    def __init__(self,modelo=None):
        self.modelo=modelo


    def Consultar(self,buscar):
        objDao=DaoPlanCuenta()
        return objDao.Consultar(buscar)

    def Ingresar(self,modelo):
        objDao=DaoPlanCuenta()
        return objDao.Ingresar(modelo)

    def Modificar(self,modelo):
        objDao=DaoPlanCuenta()
        return objDao.Modificar(modelo)

    def Eliminar(self,modelo):
        objDao=DaoPlanCuenta()
        return objDao.Eliminar(modelo)


