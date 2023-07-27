from Banco1 import Conectar
class Metodos():
  conectar=Conectar()
  def registroUsuario(self):
    print("Registro de usuario")
    dniCorrecto=False
    
    while (not dniCorrecto):
      dni= input("Dni: ")
      if dni.isnumeric():
        if len(dni)==8:
          dniCorrecto= True
        else:
          print("El dni debe tener 8 digitos")
      elif dni.isalnum():
        print("No debe ser alfanumerico")
      else:
        print("ingrese Dni valido, no es numerico")
    nombre=str(input('nombre: '))
    apellido= str(input("Apellido: "))
    deposito= float(input("Deposito: "))
    retiro=float(input("Retiro: "))
    x=True
    while x:
      if retiro <= deposito:
        x=False
      else:
        print("El retiro debe ser menor que el deposito")
        retiro=float(input("Retiro: "))

    usuario=(dni,nombre,apellido,deposito,retiro)
    return usuario
  
  def listado (self,listar):
    contador=1
    for lis in listar:
      persona="{} -- DNI: {} Nombre: {} Apellido: {} Deposito: {} Retiro: {} Saldo: {} Fecha de ingreso: {} "
      print(persona.format(
        contador,lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6]))
      contador+=1
      
  def buscar (self):
    print("Buscar usuario")
    dniCorrecto=False
    
    while (not dniCorrecto):
      dni= input("Dni: ")
      if dni.isnumeric():
        if len(dni)==8:
          dniCorrecto= True
        else:
          print("El dni debe tener 8 digitos")
      elif dni.isalnum():
        print("No debe ser alfanumerico")
      else:
        print("ingrese Dni valido, no es numerico")
    return dni
  
  def editarSaldo(self, listaDni):
    print('Editar saldo')
    documentoNac= int(input("Ingrese el DNI  "))
    for documento in listaDni:
      if documento[0]== documentoNac:
        deposito=float(input('Cuanto va a depositar? '))
        deposito+=documento[3]
        retiro=float(input("Cuanto va a retirar? "))
        retiro+= documento[4]
        while retiro > deposito:
          print("El retiro no puede ser mayor al saldo disponible.")
          retiro=float(input("Cuanto va a retirar? "))
          retiro+=documento[4]
        saldo=deposito-retiro
        return (documentoNac, deposito, retiro ,saldo)
      
  def editarTodo (self, listaDni):
    print('Editar todo')
    
    documentoNac= int(input("Ingrese el DNI  "))
    for documento in listaDni:
      if documento[0]== documentoNac:
        nombre= str(input('Nombre:'))
        apellido= str(input('Apellido: '))
        deposito=float(input('Cuanto va a depositar? '))
        deposito+=documento[3]
        retiro=float(input("Cuanto va a retirar? "))
        retiro+= documento[4]
        while retiro > deposito:
          print("El retiro no puede ser mayor al saldo disponible.")
          retiro=float(input("Cuanto va a retirar? "))
          retiro+=documento[4]
        saldo=deposito-retiro
        return (documentoNac,nombre,apellido,deposito,retiro,saldo)
    
  def eliminarDni(self,dni):
    existeDni=False
    documentoNac= int(input("Ingrese el DNI a eliminar  "))
    for documento in dni:
      if documento[0]== documentoNac:
        existeDni= True
        break
    if existeDni:
      return documentoNac
  
  def historial(self,lista):
    for lis in lista:
      imp='ID: {} Fecha: {} Hecho: {} '
      print(imp.format(lis[0], lis[1], lis[2]))
  