import mysql.connector
from mysql.connector import Error

class Conectar():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(

                host='localhost',
                port=3306,
                user='root',
                password='',
                database='banco')
        except Error as ex:
            print('NO se pudo conectar la conexion: {0}'.format(ex))

    def registro(self, perso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql_persona = "INSERT INTO persona (dni, nombre, apellido) VALUES (%s,%s,%s)"
                sql_dep_ret = "INSERT INTO dep_ret (deposito, retiro, saldo, dni_dep_ret, fechaIngreso) VALUES (%s, %s,%s, %s,CURRENT_TIMESTAMP())"
                cursor.execute(sql_persona, (perso[0], perso[1], perso[2],))
                cursor.execute(sql_dep_ret, (perso[3], perso[4],perso[3]-perso[4], perso[0]))
                self.conexion.commit()
                print('Registro Exitoso')
            except Error as ex:
                print("Error en el sistema: {0}".format(ex))


    def listarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """SELECT p.dni,p.nombre,p.apellido,
                    d.deposito,d.retiro,d.saldo, d.fechaIngreso FROM persona p INNER JOIN dep_ret d ON p.dni=d.dni_dep_ret""")
                respuesta = cursor.fetchall()
                return respuesta

            except Error as ex:
                print("Error en el sistema:{0}". format(ex))
    def buscarUsuario(self, dni):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    """SELECT p.dni,p.nombre,p.apellido,
                    d.deposito,d.retiro,d.saldo,d.fechaIngreso FROM persona p INNER JOIN dep_ret d ON p.dni=d.dni_dep_ret WHERE p.dni= %s;""", (dni,))
                respuesta = cursor.fetchall()
                return respuesta
            except Error as ex:
                print("Error en el sistema:{0}". format(ex))

    def editarSaldo(self,dni, deposito, retiro, saldo ):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql="""UPDATE dep_ret SET deposito = %s , 
                retiro = %s, saldo = %s, fechaIngreso = CURRENT_TIMESTAMP()
                WHERE dni_dep_ret= %s;"""
                cursor.execute(sql, (deposito , retiro, saldo, dni))
                self.conexion.commit()
                print("Saldo modificado")
            
            except Error as ex:
                print("Error en el sistema:{0}". format(ex))

    def editarTodo(self,dni, nombre, apellido, deposito, retiro,saldo ):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql="""UPDATE persona p, dep_ret d SET nombre=%s, apellido=%s, 
                deposito = %s, retiro = %s,
                saldo= %s,fechaIngreso = CURRENT_TIMESTAMP()
                WHERE p.dni= %s AND d.dni_dep_ret= %s"""# Corregir este codigo, por que al hacer editar todo, se mantiene el saldo anterior.
                cursor.execute(sql, (nombre, apellido, deposito, retiro, saldo, dni, dni))
                self.conexion.commit()
                print("Nombre/ Apellido/ Deposito/ Retiro/ Saldo , modificado")
            
            except Error as ex:
                print("Error en el sistema:{0}". format(ex))

    def eliminarDni(self, dni):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                
                sql_dep_ret = "DELETE FROM dep_ret WHERE dni_dep_ret= {0};"
                #sql_bitacora = "DELETE FROM bitacoraTrigger WHERE dni_bitacora= {0};"
                sql_persona = "DELETE FROM persona WHERE dni= {0};" 
                cursor.execute(sql_dep_ret.format(dni))
                #cursor.execute(sql_bitacora.format(dni))
                cursor.execute(sql_persona.format(dni))
                self.conexion.commit()
                print('La cuenta a sido eliminada')
                
            
            except Error as ex:
                print('Error en el sistema:{0}'.format(ex))

    def historial (self):
        if self.conexion.is_connected:
            try:
                cursor=self.conexion.cursor()
                sql= ('''SELECT * FROM bitacoraTrigger;''')
                cursor.execute(sql)
                respuesta=cursor.fetchall()
                return respuesta
            except Error as ex:
                print('Error en el sistema: {0}'.format(ex))
