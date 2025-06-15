En este repositorio agrego los scripts y/o mini proyectos que subo a las redes sociales.

## Mejores Prácticas
Para una mejor gestión de las dependencias y para evitar conflictos entre las versiones de los paquetes, se recomienda utilizar entornos virtuales. Puedes crear un entorno virtual con `venv` (incluido en Python) o con `conda` si tienes Anaconda/Miniconda instalado.

**Usando `venv`:**
```bash
# Crear un entorno virtual
python -m venv .venv

# Activar el entorno virtual (en Linux/macOS)
source .venv/bin/activate

# Activar el entorno virtual (en Windows)
.venv\Scripts\activate

# Para desactivar el entorno
deactivate
```

**Usando `conda`:**
```bash
# Crear un entorno conda con una versión específica de Python
conda create -n mi_entorno python=3.9

# Activar el entorno conda
conda activate mi_entorno

# Para desactivar el entorno
conda deactivate
```

## Instalación de Miniconda
Miniconda es una instalación mínima de Anaconda que incluye Conda, un gestor de paquetes y entornos. Es una excelente opción si prefieres `conda` para gestionar tus entornos de Python.

Puedes descargar Miniconda desde la documentación oficial:
[https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

Sigue las instrucciones de instalación para tu sistema operativo específico que se encuentran en esa página.

## Descripción de los Scripts
- `any-all.py`: Demuestra el uso de las funciones `any()` y `all()` en Python.
- `decorator-simple.py`: Muestra un ejemplo de un decorador simple en Python.
- `for_loop_primos.py`: Script que busca números primos utilizando un bucle `for`.
- `googlesheets.py`: Script para interactuar con Google Sheets.
- `hadouken.py`: Ejemplo de cómo indentar el código.
- `inference.py`: Script relacionado con inferencia, en el contexto de machine learning o estadísticas.
- `items.py`: Script que maneja 'items' o elementos, una demo de estructuras de datos.
- `keylogger-demo.py`: Demostración de un keylogger, script para capturar pulsaciones de teclas.
- `lambda-test.py`: Script para probar o demostrar el uso de funciones lambda en Python.
- `ligatures.py`: Script relacionado con ligaduras tipográficas o de texto.
- `long_num.py`: Truco para trabajar con números largos o de alta precisión.
- `loop-numeros.py`: Demostración de bucle básico.
- `mail-reader.py`: Script para leer correos electrónicos.
- `map-test.py`: Script para probar o demostrar el uso de la función `map()` en Python.
- `no_existe.py`: Creación de "sitio web que no existe" usando un LLM.
- `reconocer.py`: Demostración de cómo generar un reconocimiento de imágenes con un modelo de clasificación.
- `scan.py`: Demostración de API mockup.
- `socket-client.py`: Implementación de un cliente de socket para comunicaciones de red.
- `socket-server.py`: Implementación de un servidor de socket para comunicaciones de red.
- `threadingdemo.py`: Demostración del uso de hilos (`threading`) en Python.
- `troyano-client.py`: Implementación de un cliente para un troyano (con fines educativos/demostrativos).
- `troyano-server.py`: Implementación de un servidor para un troyano (con fines educativos/demostrativos).
