from Conexion import Conector
class DaoPlanCuenta(Conector):
    def __init__(self):
        super().__init__()

    def Consultar(self,buscar):
        result=False
        try:
            sql="select * from planCuenta where descripcion like '%"+ str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta de planCuenta",e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def Ingresar(self,modelo):
        correcto=True
        try:
            sql="insert into planCuenta(codigo,idGrupo,descripcion,naturaleza,estado) values(%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql,(modelo.codigo,modelo.idGrupo,modelo.descripcion,modelo.naturaleza,modelo.estado))
            self.conn.commit()
        except Exception as e:
            print("Error en insertar planCuenta", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def Modificar(self,modelo):
        correcto = True
        try:
            sql="update planCuenta set codigo=%s,idGrupo =%s,descripcion =%s,naturaleza=%s,estado=%s where id = %s"
            self.conectar()
            self.conector.execute(sql,(modelo.codigo,modelo.idGrupo,modelo.descripcion,modelo.naturaleza,modelo.estado,modelo.id))
            self.conn.commit()
        except Exception as e:
            print("Error en la Modificar planCuenta", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto


    def Eliminar(self,modelo):
        correcto =True
        try:
            sql='delete from planCuenta where id= %s'
            self.conectar()
            self.conector.execute(sql, (modelo.id))
            self.conn.commit()
        except Exception as e:
            print("Error en la Eliminación planCuenta", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

