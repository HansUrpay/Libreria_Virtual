import requests
import json
import os
from itertools import zip_longest

pokemon = "https://pokeapi.co/api/v2/"  

def clean(): #Definimos la función para limpiar pantalla segun el SO
  if os.name == "posix":
    os.system("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system("cls")

def grouper(lista, n, fillvalue=""):
    args = [iter(lista)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def print_en_columnas(lista, numfilas, ancho=15):
  for fila in zip(*grouper(lista, numfilas)):
    print("".join(f"{nombre:{ancho}s}" for nombre in fila))

def menu():
  print("Tienes las siguientes opciones:\n\n1. Mostrar pokemons por generación \n2. Mostrar pokemons por forma. \n3. Mostrar pokemons por habilidad. \n4. Mostrar pokemons por hábitat. \n5. Mostrar pokemons por tipo.\n6. Salir")

def listar_nombre(lista,nombre,i):
  url = 'https://pokeapi.co/api/v2/pokemon/'
  request_url = (requests.get(url + nombre))

  if request_url.status_code == 200:
    url_req = request_url.json()
    lista_habilidades = []
    habilidad_pokemon = url_req["abilities"]
    url_imagen = url_req['sprites']['other']['official-artwork']['front_default']
    #for i in range(len(habilidad_pokemon)):

    lista.append("************ "+str(i + 1) + "-" + nombre+" ************")
    lista.append("El url de su imagen es: " + str(url_imagen))
    lista.append("Tiene las siguientes habilidades: ") #+ str(lista_habilidades[ability]))

    for ability in range(len(habilidad_pokemon)):
      nombres_habilidad = habilidad_pokemon[ability]["ability"]["name"]
      lista_habilidades.append(nombres_habilidad)

      #lista.append(str(i + 1) + "-" + nombre + ", el url de su imagen es: " +
                   #str(url_imagen) + " , sus habilidades son: ")

      lista.append(str(lista_habilidades[ability]))
      ability = ability +1

    i = i + 1

  else:
    print(str(i + 1) + "-" + nombre + " ,el url de su imagen no fue encontrada")

def generacion():
  clean()
  try:
    generacion = input("\ningrese que generacion busca (pista son solo 8 generaciones): ")
    resp_generacion = requests.get(pokemon+"generation/"+generacion)

    dato_generacion = resp_generacion.json()
    especies = dato_generacion["pokemon_species"]
    print("\nEstos son los pokemones de la generacion:",generacion,"\n")
    lista_generacion = []
    for i in range(len(especies)):
        nombres = especies[i]["name"]
        listar_nombre(lista_generacion,nombres,i)
    print_en_columnas(lista_generacion,len(lista_generacion),ancho=20)
  except:
    generacion = input("Ingrese una generacion del 1 al 8: ")

def forma():
  clean()
  resp_formas = requests.get(pokemon+"pokemon-shape/")

  dato_formas = resp_formas.json()
  print("\nEstas son los tipos de formas que puedes elegir: \n")

  formas = dato_formas["results"]
  lista_formas = []
  for i in range(len(formas)):
      nombres_formas = formas[i]["name"]
      lista_formas.append(str(i+1)+"-"+nombres_formas)
      i = i + 1

  print_en_columnas(lista_formas,4,ancho=20)

  forma_final = input("\nCual es la forma que desea buscar para los pokemons: ")
  resp_formas_final= requests.get(pokemon +"pokemon-shape/"+forma_final)
  dato_formas_final = resp_formas_final.json()
  formas_final = dato_formas_final["pokemon_species"]

  print("\nEstos son los pokemones de la forma:",forma_final,"\n")
  lista_formas_final = []
  for i in range(len(formas_final)):
      nombres_formas_final = formas_final[i]["name"]
      listar_nombre(lista_formas_final,nombres_formas_final,i)

  print_en_columnas(lista_formas_final,len(lista_formas_final),ancho=20)

def habilidades():
  clean()
  resp_habilidades = requests.get(pokemon+"ability/")

  dato_habilidades = resp_habilidades.json()
  print("\nEstas son los tipos de habilidades que puedes elegir:\n")
  habilidad = dato_habilidades["results"]
  lista_habilidad = []
  for i in range(len(habilidad)):
      nombres_habilidad = habilidad[i]["name"]
      lista_habilidad.append(str(i+1)+"-"+nombres_habilidad)
      i = i + 1

  print_en_columnas(lista_habilidad,4,ancho=20)

  habilidad_final = input("\nCual es la habilidad que desea buscar para los pokemons: ")
  resp_habilidad_final= requests.get(pokemon +"ability/"+habilidad_final)
  dato_habilidades_final = resp_habilidad_final.json()
  habilidades_final = dato_habilidades_final["pokemon"]

  print("\nEstos son los pokemones de la habilidad:",habilidad_final+"\n")
  lista_habilidad_final = []
  for i in range(len(habilidades_final)):
      nombres_habilidades_final = habilidades_final[i]["pokemon"]['name']
      listar_nombre(lista_habilidad_final,nombres_habilidades_final,i)

  print_en_columnas(lista_habilidad_final,len(lista_habilidad_final),ancho=30)


# opcion 4 habitats de pokemons
def habitats():
  clean()
  resp_habitats = requests.get(pokemon + "pokemon-habitat/")
  dato_habitats = resp_habitats.json()
  print("Estos son los tipos de hábitats que puedes elegir")
  habitat = dato_habitats["results"]
  lista_habitats = []
  for i in range(len(habitat)):
      nombres_habitat = habitat[i]["name"]
      lista_habitats.append(str(i + 1) + ". " + str(nombres_habitat).capitalize())
      i = i + 1
  print_en_columnas(lista_habitats, 3, ancho=20)

  habitat_final = input("\nIngrese la opicion del hábitat de pokemons que desea buscar: ")
  resp_habitats_final= requests.get(pokemon +"pokemon-habitat/"+habitat_final)
  dato_habitats_final = resp_habitats_final.json()

  habitats_final = dato_habitats_final["pokemon_species"]
  print("Estos son los pokemons del hábitat:", habitat_final)
  lista_habitats_final = []
  for i in range(len(habitats_final)):
      nombres_habitats_final = habitats_final[i]['name']
      lista_habitats_final.append(str(i + 1) + ". " + str(nombres_habitats_final).capitalize())
      i = i + 1
  print_en_columnas(lista_habitats_final, 15, ancho=20)

# opcion 5 Tipos de pokemon
def tipos():
  clean()
  resp_tipos = requests.get(pokemon+"type/")

  dato_tipos = resp_tipos.json()
  print("\nEstas son los tipos de pokemons que puedes elegir\n")

  tipos = dato_tipos["results"]
  lista_tipos = []
  for i in range(len(tipos)):
      nombres_tipos = tipos[i]["name"]
      lista_tipos.append(str(i+1)+"-"+nombres_tipos)
      i = i + 1
      
  print_en_columnas(lista_tipos,4,ancho=20)

  tipo_final = input("\nCual es el tipo de pokemon que desea buscar: ")
  resp_tipo_final= requests.get(pokemon +"type/"+tipo_final)
  dato_tipo_final = resp_tipo_final.json()

  tipos_final = dato_tipo_final["pokemon"]
  print("\nEstos son los pokemones de tipo:",tipo_final+"\n")
  lista_tipos_final = []
  for i in range(len(tipos_final)):
      nombres_tipos_final = tipos_final[i]["pokemon"]['name']
      lista_tipos_final.append(str(i+1)+"-"+nombres_tipos_final)
      i = i + 1

  print_en_columnas(lista_tipos_final,30,ancho=30)

def selector():
    menu()
    opcion = input("\nIngresa una opcion: ")
    while True:
      try:
        opcion = int(opcion)
        lista_menu = [generacion, forma, habilidades, habitats, tipos]
        if opcion == 6:
          return "\nGracias por usar la pokeapi" 
        else:
          lista_menu[opcion - 1]()
          opcion2 = input("\nDeseas volver al menu principal? S/N: " ).upper()
          while True:
            if opcion2 == "S" or opcion2 == "SI":
              clean()
              print("Menu principal:\n")
              menu()
              opcion = input("\nIngresa una opcion: ")
              break
            elif opcion2 == "N" or opcion2 == "NO":
              return "\nGracias por usar la libreria virtual"
            else:
              opcion2 = input("Debes ingresar S o N: " ).upper()
      except:
        opcion = input("Ingresa una opcion válida: ")

clean()
print("---- BIENVENIDO/A A LA POKEAPI ----\n")
selector()


