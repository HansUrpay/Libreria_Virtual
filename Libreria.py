# Tarea 1
# Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autor(es). Considerar que un libro puede tener varios autores.

# Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.

# Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

# Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
# Opción 2: Listar libros.
# Opción 3: Agregar libro.
# Opción 4: Eliminar libro.
# Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
# Opción 6: Ordenar libros por título.
# Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
# Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
# Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
# Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
# opcion 11: Salir del programa
# Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)

#INICIO DE TAREA

import pandas as pd
import pandas as ForSortingCSV
from csv import DictWriter
from os import system
system("cls")         

def libreria():
  def menu():
        return( "Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.\nOpción 2: Listar libros.\nOpción 3: Agregar libro.\nOpción 4: Eliminar libro.\nOpción 5: Buscar libro por ISBN o por título.\nOpción 6: Ordenar libros por título.\nOpción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.\nOpción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.\nOpción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).\nOpción 10: Guardar libros en archivo de disco duro (.txt o csv).\n")
  
  # def clean(): #Definimos la función para limpiar pantalla segun el SO
  #   if os.name == "posix":
  #     os.system ("clear")
  #   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
  #     os.system ("cls")
  
  # Agregar las funciones para cada opcion
  def leer_archivo():
      datos = pd.read_csv("libros.csv")
      # print(datos.sort_values(by="id"))
      print(datos.iloc[0:3])

  def listar():
      datos = pd.read_csv("libros.csv")
      print(datos.iloc[:,[1,2,3,4,5]])
      
  def eliminar():
      datos = pd.read_csv("libros.csv")
      print(datos)       
      elim = int(input("\nIngrese id del libro que  desea eliminar: "))
      datos.drop(inplace=True, index = (elim-1))
      print(datos)

  def buscar_isbn_titulo():
      #Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
      datos = pd.read_csv("libros.csv")
      while True:
        print("\nElija una opción\n")
        print("1. Buscar por ISBN")
        print("2. Buscar por Título")
        print("3. Salir\n")  
        opcion = input("Ingresar opción: ")    
        if (opcion == "1"):
          print(datos.iloc[:,[3]])  
        elif (opcion == "2"):
          print(datos.iloc[:,[1]])
        else:
          break       

  def orderar_por_titulo():
    # Se lee el archivo csv de libros
    libros_ordenados = ForSortingCSV.read_csv("libros.csv")
    # Se ordenan los libros por titulo con sort_values
    libros_ordenados.sort_values(["titulo"], axis=0, ascending=[True], inplace=True)
    # Se imprime columna de titulos ordenados de libros 
    print(libros_ordenados.iloc[:,[1]])
  
  def buscar_autor_editorial_genero():
  #Opción 7: Buscar libro por autor, editorial o genero
  # Se lee el archivo de libros
    libros = pd.read_csv("libros.csv")
    while True:
      print("\nElija una opción\n")
      print("1. Buscar por autor")
      print("2. Buscar por editorial")
      print("3. Buscar por genero")
      print("4. Volver al menu principal\n")  
      opcion = input("Ingresar opción: ")    
      if opcion == "1":
        # Se imprime columna de autores
        print(libros.iloc[:,[5]])
      elif opcion == "2":
        # Se imprime columna de editorial
        print(libros.iloc[:,[4]])
      elif opcion == "3":
        # Se imprime columna de genero
        print(libros.iloc[:,[2]])
      else:
        break 

  def guardar():
    class libro():
        libros = ["id","titulo","genero","isbn","editorial","autores"]
        def __init__(self):
          self.id = input("Ingrese ID: ")
          self.titulo = input("Ingresar el titulo del libro: ")
          self.genero = input("Ingrese genero del libro: ")
          self.isbn = input("Ingrese ISBN: ")
          self.editorial = input("Ingrese editorial: ")
          self.autores = input("Ingrese autores: ")  
    insert = True
    while insert:
      libro1 = libro()
      lib_datos = {"id":libro1.id, "titulo":libro1.titulo, "genero":libro1.genero, "isbn":libro1.isbn, "editorial":libro1.editorial, "autores":libro1.autores}
      with open ('libros.csv','a',newline='') as nueva_linea:
        escribir = DictWriter(nueva_linea, fieldnames=libro1.libros)
        escribir.writerow(lib_datos)
        nueva_linea.close()
      if (input("\nRegistrar otro libro? S/N: ")).lower() == "n":
        insert = False
            
  # Menú de opciones para el usuario
  print("---- BIENVENIDO A TU LIBRERIA VIRTUAL ----\n")
  print(menu())
  opcion = int(input("Ingresa una opcion: ")) 
  while True:
    if  opcion == 1:
      leer_archivo()
      opcion2 = input("Deseas volver al menu? S/N: " ).upper()
      if opcion2 == "S" or opcion2 == "SI":
        system("cls")
        print(menu())
        opcion = int(input("Ingresa una opcion: "))
      else:
        print("Gracias por usar la libreria virtual")
        break
    if  opcion == 2:
      listar()
      opcion2 = input("Deseas volver al menu? S/N: " ).upper()
      if opcion2 == "S" or opcion2 == "SI":
        system("cls")
        print(menu())
        opcion = int(input("Ingresa una opcion: "))
      else:
        print("Gracias por usar la libreria virtual")
        break
    
    if  opcion == 4:
      eliminar()
      opcion2 = input("Deseas volver al menu? S/N: " ).upper()
      if opcion2 == "S" or opcion2 == "SI":
        system("cls")
        print(menu())
        opcion = int(input("Ingresa una opcion: "))
      else:
        print("Gracias por usar la libreria virtual")
        break
    
    if opcion == 5:
       buscar_isbn_titulo()
       print("Volveras al menú principal")
       system("cls")
       print(menu())
       opcion = int(input("Ingresa una opcion: "))
    if opcion == 6:
      orderar_por_titulo()
      opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
      if opcion2 == "S" or opcion2 == "SI":
        system("cls")
        print(menu())
        opcion = int(input("Ingresa una opcion: "))
      else:
        print("Gracias por usar la libreria virtual")
        break
    if opcion == 7:
      buscar_autor_editorial_genero()
      system("cls")
      print(menu())
      opcion = int(input("Ingresa una opcion: "))
    if opcion == 10:
       guardar()
       print("Volveras al menú principal")
       system("cls")
       
       print(menu())
       opcion = int(input("Ingresa una opcion: "))
   
    
print(libreria())

# def mostrar(self):
#   print()
#   for nombre, valor in self.dicc_libros.items(): # .items() funciona en Python 3.x
#       print("----")
#       Id = valor["ID"]
#       genero = valor["Genero"]
#       isbn = valor["ISBN"]
#       editorial = valor["Editorial"]
#       autor = valor["Autor"]
#       print("ID: {} | Nombre: {} | Genero: {} | ISBN: {} | Autor: {} | Editorial: {} ".format(Id,nombre,genero,isbn,autor, editorial))