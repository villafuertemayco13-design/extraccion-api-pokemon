# Extracción de datos desde PokeAPI

## Descripción
Este proyecto fue realizado para practicar la extracción
y el almacenamiento de datos utilizando una API pública.

El programa consulta información de los primeros 10 Pokémon
disponibles en PokeAPI y guarda los resultados en un archivo JSON.

## Tecnologías utilizadas
- Python
- requests
- python-dotenv
- JSON

## Archivos del proyecto
- main.py: código principal de extracción.
- data_extracted.json: datos obtenidos de la API.
- .env.example: ejemplo de configuración.
- .gitignore: archivos que no deben subirse.
- requirements.txt: dependencias necesarias.

## Instalación
1. Descargar o clonar el repositorio.
2. Instalar las dependencias:

   pip install -r requirements.txt

3. Copiar .env.example y renombrar la copia a .env.
4. Ejecutar el programa:

   python main.py

## Funcionamiento
El programa realiza peticiones GET a PokeAPI,
selecciona los datos necesarios y los guarda en JSON.

También utiliza bloques try/except para manejar errores
de conexión y problemas con las respuestas.

## Fuente
https://pokeapi.co/
