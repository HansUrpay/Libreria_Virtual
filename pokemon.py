import requests
import json
from os import system
from itertools import zip_longest
system("cls")
from itertools import zip_longest

pokemon = "https://pokeapi.co/api/v2/"

def grouper(lista, n, fillvalue=""):
    args = [iter(lista)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def print_en_columnas(lista, numfilas, ancho=15):
  for fila in zip(grouper(lista, numfilas)):
    print("".join(f"{nombre:{ancho}s}" for nombre in fila))

def menu():
  print("\nOpción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.\nOpción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.\nOpción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.\nOpción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.\nOpción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.")

def generacion():

  generacion = input("\ningrese que generacion busca (pista son solo 8 generaciones): ")
  resp_generacion = requests.get(pokemon+"generation/"+generacion)
  dato_generacion = resp_generacion.json()

  especies = dato_generacion["pokemon_species"]
  print("\nEstos son los pokemones de la generacion:",generacion,"\n")
  lista_generacion = []
  for i in range(len(especies)):
      nombres = especies[i]["name"]
      lista_generacion.append(str(i+1)+"-"+nombres)
      i = i + 1
      #print(len(especies))
  print_en_columnas(lista_generacion,25,ancho=20)

def forma():

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
      lista_formas_final.append(str(i+1)+"-"+nombres_formas_final)
      i = i + 1
  print_en_columnas(lista_formas_final,25,ancho=20)

def habilidades():

  resp_habilidades = requests.get(pokemon+"ability/")

  dato_habilidades = resp_habilidades.json()
  print("\nEstas son los tipos de habilidades que puedes elegir\n")

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
      lista_habilidad_final.append(str(i+1)+"-"+nombres_habilidades_final)
      i = i + 1

  print_en_columnas(lista_habilidad_final,10,ancho=30)


# opcion 4 habitats de pokemons
def habitats():
  resp_habitats = requests.get(pokemon + "pokemon-habitat/")
  dato_habitats = resp_habitats.json()
  print("Estas son los tipos de habitats que puedes elegir")
  habitat = dato_habitats["results"]
  lista_habitats = []
  for i in range(len(habitat)):
      nombres_habitat = habitat[i]["name"]
      lista_habitats.append(str(i + 1) + "-" + nombres_habitat)
      i = i + 1
  print_en_columnas(lista_habitats, 3, ancho=20)

  habitat_final = input("\nCual es el habitat que desea buscar para los pokemons: ")
  resp_habitats_final= requests.get(pokemon +"pokemon-habitat/"+habitat_final)
  dato_habitats_final = resp_habitats_final.json()

  habitats_final = dato_habitats_final["pokemon_species"]
  print("Estos son los pokemones de la habitat:", habitat_final)
  lista_habitats_final = []
  for i in range(len(habitats_final)):
      nombres_habitats_final = habitats_final[i]['name']
      lista_habitats_final.append(str(i + 1) + "-" + nombres_habitats_final)
      i = i + 1
  print_en_columnas(lista_habitats_final, 15, ancho=20)


menu()
opcion = int(input("\nIngresa una opcion: "))
while True:
  if opcion == 1:
    generacion()
    opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
    if opcion2 == "S" or opcion2 == "SI":
      menu()
      opcion = int(input("\nIngresa una opcion: "))
    else:
      print("\nGracias por usar la libreria virtual")
      break
  if opcion == 2:
    forma()
    opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
    if opcion2 == "S" or opcion2 == "SI":
      menu()
      opcion = int(input("\nIngresa una opcion: "))
    else:
      print("\nGracias por usar la libreria virtual")
      break
  if opcion == 3:
    habilidades()
    opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
    if opcion2 == "S" or opcion2 == "SI":
      menu()
      opcion = int(input("\nIngresa una opcion: "))
    else:
      print("\nGracias por usar la libreria virtual")
      break


