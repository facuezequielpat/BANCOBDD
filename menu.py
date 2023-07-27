from Banco1 import Conectar
from Banco2 import Metodos

class Mostrar():

  def principal(self):
    repetir = True
    while repetir:
      print("""\n1- Registro de usuarios
2- Mostrar usuarios
3- Buscar usuario
4- Editar saldo (depositar/retirar)
5- Editar todo
6- Eliminar usuario
7- Historial
8- Salir \n""")
      # Plazo fijo,cuenta corriente, caja de ahorro( Investigar y crear )
      opcion=int(input("Elija un numero: "))
      if opcion < 1 or opcion > 8:
            print("Opcion invalida")
      elif opcion == 8:
          repetir = False
          print("Programa finalizado")
      else:
          opciones(opcion)

def opciones(opcion):
  conectar=Conectar()
  metodos=Metodos()
  if opcion==1:
    persona=metodos.registroUsuario()
    try:
      conectar.registro(persona)
    except:
      print("Ocurrio un error")
  
  elif opcion==2:
    try:
      lista=conectar.listarUsuarios()
      if len(lista)>0:
        metodos.listado(lista)
      else:
        print("No se han registrado usuarios")
    except:
      print("Ocurrio un error")
    
  
  elif opcion == 3:
    try: 
      dni = metodos.buscar()
      usuario_encontrado = conectar.buscarUsuario(dni)
      if usuario_encontrado:
        metodos.listado(usuario_encontrado)
      else:
        print("No se encontró un usuario con el DNI proporcionado")
    except:
      print("Ocurrió un error")

  elif opcion == 4:
    try: 
      personas=conectar.listarUsuarios()
      if len(personas)>0:
        datos = metodos.editarSaldo(personas)
        conectar.editarSaldo(*datos)
      else:
        print('No se encontraron registros')
    except: 
      print('Ocurrió un error')
  
  elif opcion == 5:
    try:
      personas=conectar.listarUsuarios()
      if len(personas)>0:
        datos = metodos.editarTodo(personas)
        conectar.editarTodo(*datos)
      else:
        print('No se encontraron registros')
    except: 
      print('Ocurrió un error')
  
  elif opcion == 6:
    try:
        personas=conectar.listarUsuarios()
        if len(personas)>0:
            persona=metodos.eliminarDni(personas)
            if persona:
                conectar.eliminarDni(persona)
            else:
                print('DNI incorrecto')
        else:
            print('No se encontraron registros')
    except:
        print('Ocurrio un error')
  
  elif opcion == 7:
    try:
      respuesta=conectar.historial()
      if respuesta:
        metodos.historial(respuesta)
      else:
        print("No se encontró historial para el DNI proporcionado")
    except:
      print("Ocurrio un error")
  
  

      
  
  


    


    

mostrar = Mostrar()
mostrar.principal()
