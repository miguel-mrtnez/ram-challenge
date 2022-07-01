# ram-challenge

## Instalación
El programa utiliza el un entorno virtual soportado por la [librería](https://pipenv-es.readthedocs.io/es/latest/) `pipenv`. Para instalarla en un sistema Windows, se puede mendiante la ejecución del siguiente comando:

```pip install pipenv```

Con una consola ubicada en el directorio base, se debe ejecutar el comando `pipenv shell` para ingresar al entorno virtual. Han de instalarse todas las dependencias listadas en el archivo `Pipfile`, que incluye una versión específica de Python.

## Módulos
En `utils/` se pueden encontrar los siguientes módulos:
- `timer.py`: Implementa la clase `Timer`, que se utiliza para medir el tiempo de ejecución de las tareas.
- `response.py`: Implementa la clase `ResponseManager`, que toma por argumentos los resultados de cada una de las tareas y las convierte al formato requerido.
- `proxy.py`: Implementa la clase `Proxy`, que obtiene la información de `locations`, `episodes` y `characters` desde la API.
- `excercises.py`: Contiene las funciones `char_counter` y `episode_locations`, que realizan las tareas homónimas requeridas.

Además, en el directorio principal se encuentra el archivo `main.py`, que se encarga de ejecutar el programa, y generar un archivo de nombre `output.json` con el resultado.

Finalmente, las *urls* fueron tratadas como parámetros en el archivo `params.yaml`.

### Testing
Se agregaron módulos de tests unitarios en el directorio `testing`. Pueden ser ejecutados de manera independiente, o bien en conjunto, con el comando:

`python -m unittest <path_test_1> <path_test_2> ...`

### Nota sobre la clase `Proxy`
Si bien existe una [librería](https://rickandmortyapi.com/documentation/#python) ya implementada que contiene cierta lógica de conexión con la API de Rick and Morty, se optó por una solución propia por las siguentes razones:
- El código útil de la librería consistía solo en un [módulo](https://github.com/curiousrohan/ramapi/blob/master/ramapi/ramapi.py).
- La librería solo incluye una método para obtener las páginas de los `characters`, por lo que de todas maneras se habría tenido que programar el acceso a las de los dos recursos restantes.
