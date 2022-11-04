import requests
import json
from os import system
system("cls")

pokemon = "https://pokeapi.co/api/v2/"
#pokemon = "https://pokeapi.co/api/v2/pokemon/bulbasaur"
# # pokemon = 'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

def menu():
  print("\nOpción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.\nOpción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.\nOpción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.\nOpción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.\nOpción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.")

def generacion():

  generacion = input("ingrese que generacion busca (pista son solo 8 generaciones): ")
  resp_generacion = requests.get(pokemon+"generation/"+generacion)
  #cabezera = resp.headers
  #print(cabezera)
  print("************************************")
  dato_generacion = resp_generacion.json()
  #print("************************************")
  #print(dato)

  especies = dato_generacion["pokemon_species"]
  print("Estos son los pokemones de la generacion:",generacion)
  for i in range(len(especies)):
      nombres = especies[i]["name"]
      i = i + 1
      #print(len(especies))
      print(nombres, end="--")

def forma():

  #formas = input("que tipo de forma buscas: ")
  resp_formas = requests.get(pokemon+"pokemon-shape/")

  print("************************************")
  dato_formas = resp_formas.json()
  print("Estas son los tipos de formas que puedes elegir")
  #print(dato)

  formas = dato_formas["results"]
  for i in range(len(formas)):
      nombres_formas = formas[i]["name"]
      i = i + 1
      #print(len(especies))
      print(nombres_formas, end="--")

  forma_final = input("\nCual es la forma que desea buscar para los pokemons: ")
  resp_formas_final= requests.get(pokemon +"pokemon-shape/"+forma_final)
  dato_formas_final = resp_formas_final.json()

  formas_final = dato_formas_final["pokemon_species"]
  print("Estos son los pokemones de la forma:",forma_final)

  for i in range(len(formas_final)):
      nombres_formas_final = formas_final[i]["name"]
      i = i + 1
      #print(len(especies))
      print(nombres_formas_final, end="--")

def habilidades():

  #formas = input("que tipo de forma buscas: ")
  resp_habilidades = requests.get(pokemon+"ability/")

  print("************************************")
  dato_habilidades = resp_habilidades.json()
  print("Estas son los tipos de habilidades que puedes elegir")
  #print(dato)

  habilidad = dato_habilidades["results"]
  for i in range(len(habilidad)):
      nombres_habilidad = habilidad[i]["name"]
      i = i + 1
      #print(len(especies))
      print(nombres_habilidad, end="--")

  habilidad_final = input("\nCual es la habilidad que desea buscar para los pokemons: ")
  resp_habilidad_final= requests.get(pokemon +"ability/"+habilidad_final)
  dato_habilidades_final = resp_habilidad_final.json()

  habilidades_final = dato_habilidades_final["pokemon"]
  print("Estos son los pokemones de la habilidad:",habilidad_final)

  for i in range(len(habilidades_final)):
      nombres_habilidades_final = habilidades_final[i]["pokemon"]['name']
      i = i + 1
      #print(len(especies))
      print(nombres_habilidades_final, end="--")


menu()
opcion = int(input("Ingresa una opcion: "))
while True:
  if opcion == 1:
    generacion()
    opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
    if opcion2 == "S" or opcion2 == "SI":
      menu()
      opcion = int(input("Ingresa una opcion: "))
    else:
      print("Gracias por usar la libreria virtual")
    break
  if opcion == 2:
    forma()
    opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
    if opcion2 == "S" or opcion2 == "SI":
      menu()
      opcion = int(input("Ingresa una opcion: "))
    else:
      print("Gracias por usar la libreria virtual")
      break
  if opcion == 3:
    habilidades()
    opcion2 = input("\nDeseas volver al menu? S/N: " ).upper()
    if opcion2 == "S" or opcion2 == "SI":
      menu()
      opcion = int(input("Ingresa una opcion: "))
    else:
      print("Gracias por usar la libreria virtual")
      break

