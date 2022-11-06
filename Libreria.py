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
import csv
from csv import DictWriter
import pandas as pd
from os import system
system("cls")         

def libreria():
  def menu():
        return( "Opción 1: Leer archivo de libros.\nOpción 2: Mostrar libros.\nOpción 3: Agregar libro.\nOpción 4: Eliminar libro.\nOpción 5: Buscar libro por ISBN o por título.\nOpción 6: Ordenar libros por título.\nOpción 7: Buscar libros por autor, editorial o género. \nOpción 8: Buscar libros por número de autores. \nOpción 9: Editar o actualizar datos de un libro.\nOpción 10: Guardar libros en archivo\n")
  
  # def clean(): #Definimos la función para limpiar pantalla segun el SO
  #   if os.name == "posix":
  #     os.system ("clear")
  #   elif os.name == "ce" or os.name == "nt" or os.name == "dos":
  #     os.system ("cls")
  
  # Agregar las funciones para cada opcion

  # opcion 1: leer archivo de disco duro (.txt o csv) que cargue 3 libros
  def leer_archivo():
      # Se lee el archivo de libros
      print("Leyendo archivo de libros ...\n")
      datos = pd.read_csv("libros.csv")
      # Se imprime 3 libros del archivo
      print(datos[["ID","TITULO","GENERO","ISBN","EDITORIAL","AUTORES"]].iloc[0:3])

  # opción 2: Listar libros.
  def listar():
      # Se lee el archivo de libros
      print("Mostrando libros ...\n")
      datos = pd.read_csv("libros.csv")
      # Se imprime todos los libros del archivo
      print(datos.iloc[:,[0,1,2,3,4,5]])
      
  # Opción 4: Eliminar libro.
  def eliminar():
      print("Libros disponibles:\n")
      datos = pd.read_csv("libros.csv")
      print(datos.iloc[:,[0,1,2,3,4,5]])
      elim = int(input("\nIngrese id del libro que desea eliminar: ")) 
      while elim not in datos.index:          
        print("Ingrese un ID que se encuentre en la lista\n")
        elim = int(input("\nIngrese id del libro que desea eliminar: "))
      datos.drop(inplace=True, index = (elim-1))
      print(datos.iloc[:,[0,1,2,3,4,5]])   
      
  #Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
  def buscar_isbn_titulo():
      # Se lee el archivo de libros
      datos = pd.read_csv("libros.csv")
      while True:
        print("\nElija una opción\n")
        print("1. Buscar por ISBN")
        print("2. Buscar por Título")
        print("3. Salir\n")  
        opcion = input("Ingresar opción: ")    
        # Se realiza la busqueda por datos ISBN
        if (opcion == "1"):
          print("Ingrese un número ISBN (número de 10 0 13 digitos),\nEjemplo: 9788437638973\n")
          # Se ingresa el número ISBN
          isbn_num = input("Ingrese número: ")
          # Se buscan las coincidencias
          buscar_isbn = datos[datos["ISBN"].astype(str).str.contains(isbn_num, case=False)]
          coincidencias_isbn = buscar_isbn.size
          if coincidencias_isbn == 0:
            print("\nNo se han encontrado coindiciencias")
          else: 
          # Se muestran las coincidencias
            print(buscar_isbn[["TITULO","AUTORES","ISBN","GENERO","EDITORIAL"]])
        # Se realiza la busqueda por titulo
        elif (opcion == "2"):
          # Se ingresa el titulo o coincidencias
          name_titulo = input("Ingrese el titulo del libro que desea buscar: ")
          # Se buscan las coincidencias
          buscar_titulo = datos[datos["TITULO"].str.contains(name_titulo, case=False)]
          coincidencias_titulo = buscar_titulo.size
          if coincidencias_titulo == 0:
            print("\nNo se han encontrado coindiciencias")
          else:
          # Se muestran las coincidencias      
            print(buscar_titulo[["TITULO","AUTORES","ISBN","GENERO","EDITORIAL"]])
        else:
          selector()

  # Opción 6: Ordenar libros por título.
  def orden_por_titulo():
      # Se lee el archivo csv de libros
      libros_ordenados = pd.read_csv("libros.csv")
      # Se ordenan los libros por titulo con sort_values
      libros_ordenados.sort_values(["TITULO"], axis=0, ascending=[True], inplace=True)
      print("Libros ordenados alfabéticamente por titulo:\n")
      # Se imprime columna de titulos ordenados de libros 
      print(libros_ordenados.iloc[:,[1]])
  
  #Opción 7: Buscar libro por autor, editorial o genero
  def buscar_autor_editorial_genero():
    # Se lee el archivo de libros
      while True:
        print("\nElija una opcion del 1 al 4:\n")
        print("1. Buscar por autor")
        print("2. Buscar por editorial")
        print("3. Buscar por genero")
        print("4. Volver al menu principal\n")  
        opcion = input("Ingresar opción: ") 
        with open("libros.csv", "r",encoding="UTF-8") as file:
          libros = csv.reader(file)
          
          if opcion == "1":
            system("cls")
            busqueda = input("Ingresar el autor a buscar: ")
            print("Busquedas encontradas: \n")
            for fila in libros:
              if busqueda.upper() in fila[5] or busqueda.lower() in fila[5] or busqueda.capitalize() in fila[5]:
                print(" ".join(fila))
          
          elif opcion == "2":
            system("cls")
            busqueda = input("Ingresar la editorial a buscar: ")
            print("Busquedas encontradas: \n")
            for fila in libros:
              if busqueda.upper() in fila[4] or busqueda.lower() in fila[4] or busqueda.capitalize() in fila[4]:
                print(" ".join(fila))
          elif opcion == "3":
            system("cls")
            busqueda = input("Ingresar el genero a buscar: ")
            print("Busquedas encontradas: \n")
            for fila in libros:
              if busqueda.upper() in fila[2] or busqueda.lower() in fila[2] or busqueda.capitalize() in fila[2]:
                print(" ".join(fila))
          elif opcion == "4":
            system("cls")
            selector()
          else:
            buscar_autor_editorial_genero()
          
  #Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
  def buscar_autores():
      print("BUSCAR LIBRO POR EL NÚMERO DE AUTORES\n")
      #Ingresamos el número de autores a buscar
      cant_autores = int(input("Ingrese el número de autores: "))
      #Se lee el archivo libros.csv
      datos = pd.read_csv("libros.csv")
      datos.set_index("TITULO", inplace=True)
      #Imprime solo datos de libros con el número de autores escogido
      print(datos.loc[datos["NUM_AUTORES"]==cant_autores,["AUTORES","GENERO", "EDITORIAL","ISBN"]])
      
  # Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
  def guardar():
      class libro():
          libros = ["ID","TITULO","GENERO","ISBN","EDITORIAL","AUTORES","NUM_AUTORES"]
          def __init__(self):
            self.id = input("Ingrese ID: ")
            self.titulo = input("Ingresar el titulo del libro: ")
            self.genero = input("Ingrese genero del libro: ")
            self.isbn = input("Ingrese ISBN: ")
            self.editorial = input("Ingrese editorial: ")
            self.autores = input("Ingrese autores: ")
            self.num_autores = input("Ingrese el número de autores: ")  
      insert = True
      while insert:
        libro1 = libro()
        lib_datos = {"ID":libro1.id, "TITULO":libro1.titulo, "GENERO":libro1.genero, "ISBN":libro1.isbn, "EDITORIAL":libro1.editorial, "AUTORES":libro1.autores, "NUM_AUTORES":libro1.num_autores}
        with open ('libros.csv','a',newline='') as nueva_linea:
          escribir = DictWriter(nueva_linea, fieldnames=libro1.libros)
          escribir.writerow(lib_datos)
          nueva_linea.close()
        if (input("\nRegistrar otro libro? S/N: ")).lower() == "n":
          insert = False
            
  # Menú de opciones para el usuario  
  def selector():
    print(menu())
    opcion = input("Ingresa una opcion: ")
    while True:
      try:
        opcion = int(opcion)
      except:
        opcion = input("Ingresa una opcion válida: ")
      else:
        lista_menu = [leer_archivo, listar, eliminar, buscar_isbn_titulo, orden_por_titulo, buscar_autor_editorial_genero, buscar_autores, editar_actualizar]
        system("cls")
        lista_menu[opcion - 1]() 
        opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
        while True:
            if opcion2 == "S" or opcion2 == "SI":
              system("cls")
              print(menu())
              opcion = input("Ingresa una opcion: ")
              break
            elif opcion2 == "N" or opcion2 == "NO":
              return "\nGracias por usar la libreria virtual"
            else:
              opcion2 = input("Debes ingresar S o N: " ).upper()
              
  print("---- BIENVENIDO A TU LIBRERIA VIRTUAL ----\n")
  print(selector())            

print(libreria())
