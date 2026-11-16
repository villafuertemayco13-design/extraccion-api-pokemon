import os
import json
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

API_URL = os.getenv("API_URL")

def extraer_pokemon():
    if not API_URL:
        print("Error: falta configurar API_URL.")
        return

    lista_pokemon = []

    for pokemon_id in range(1, 11):
        url = f"{API_URL.rstrip('/')}/{pokemon_id}"

        try:
            respuesta = requests.get(url, timeout=10)
            respuesta.raise_for_status()

            datos = respuesta.json()

            pokemon = {
                "id": datos["id"],
                "nombre": datos["name"],
                "altura": datos["height"],
                "peso": datos["weight"],
                "tipo": [
                    tipo["type"]["name"]
                    for tipo in datos["types"]
                ],
                "experiencia_base": datos["base_experience"]
            }

            lista_pokemon.append(pokemon)
            print(f"Extraído: {pokemon['nombre']}")

        except requests.exceptions.RequestException as error:
            print(f"Error de conexión: {error}")

        except (KeyError, TypeError, ValueError) as error:
            print(f"Error procesando datos: {error}")

    if len(lista_pokemon) == 10:
        with open("data_extracted.json", "w", encoding="utf-8") as archivo:
            json.dump(
                lista_pokemon,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("Extracción finalizada correctamente.")
    else:
        print("Extracción incompleta. No se actualizó el JSON.")

if __name__ == "__main__":
    extraer_pokemon()
