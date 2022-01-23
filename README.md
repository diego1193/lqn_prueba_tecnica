# Prueba tecnica LQN - Diego Cabrera 📋

> En este repositorio podrá encontrar dos carpetas primordiales, que son **parte_1** y **parte_2**; en la carpeta **parte_1** podrá encontrar los dos primeros ejercicios resueltos, según lo planteado en la primera parte de la prueba y en la carpeta **parte_2** podrá encontrar dos capetas llamadas my_swapi y swapi_docker. Más adelante entraré a explicar el desarrollo de la prueba.

## Requerimientos 📔
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)
* [Docker](https://docs.docker.com/desktop/windows/install/)
* [PyTest](https://docs.pytest.org/en/6.2.x/getting-started.html)
* [Flake8](https://ichi.pro/es/que-es-flake8-y-por-que-deberiamos-usarlo-202979474961394)
## Intalación del entorno y paquetes 🛠️

Primero tendremos que dirigirnos a anaconda prompt (debes tener instalado anaconda), lo puedes buscar en tu buscado de Windows (si está instalado), una vez estemos en la consola de anaconda, procederemos instalar el entorno virtual, empezaremos con escribir:
```
conda create -n (nombre del entonrno) python==3.8.5 -y
```
Una vez instalado el entorno, procederemos a activarlo:
```
conda activate (nombre del entonrno)
```
Luego tendremos que clonar el proyecto:
```
git clone https://github.com/diego1193/lqn_prueba_tecnica.git
```
Una vez clonado el proyecto, nos dirigimos a la ruta mediante la consola de anaconda y una vez allí, podremos encontrar el archivo requirements.txt; procederemos a instalarlo:
```
pip install -r requirements.txt
```
(Mediante la instalación podremos obtener un error de tensorflow ya que estamos utilizamos conda para instalar el entorno virtual, pero no es relevante).

### Nota: 📢
> Debe utilizar **conda** para instalar el proyecto ya que para utilizar Flake8 tendremos que tener el entorno instalado con esta herramienta.

## Solucion parte 1, prueba tecnica 🚀

Ya descargado el repositorio, procederemos a abrir el archivo con Visual Studio Code o nuestro IDE preferido; allí encontraremos una carpeta llamada **parte_1**, en esta carpeta abran dos archivos **ejercicio_1.py** y **ejercicio_2.py**, ahora procederemos a ejecutar cada uno de estos archivos (para poder ejecutarlos debemos dirigirnos a la carpeta **parte_1** mediante consola).

#### Solución ejercicio 1 de la primara parte de la prueba 📝

En consola escribimos:
```
python ejercicio_1.py
```
Y aparecerá en consola la solución del ejercicio 1.

#### Solución ejercicio 2 de la primara parte de la prueba 📝

En consola escribimos:
```
python ejercicio_2.py
```
Y aparecerá en consola la solución del ejercicio 2.
