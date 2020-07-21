from DaoGrupo import *

class ctrGrupo:
    def __init__(self,modelo=None):
        self.modelo=modelo


    def Consultar(self,buscar):
        objDao=DaoGrupo()
        return objDao.Consultar(buscar)

    def Ingresar(self,modelo):
        objDao=DaoGrupo()
        return objDao.Ingresar(modelo)

    def Modificar(self,modelo):
        objDao=DaoGrupo()
        return objDao.Modificar(modelo)

    def Eliminar(self,modelo):
        objDao=DaoGrupo()
        return objDao.Eliminar(modelo)


