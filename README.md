# Prueba tecnica LQN - Diego Cabrera 📋

> En este repositorio podrá encontrar dos carpetas primordiales, que son **parte_1** y **parte_2**; en la carpeta **parte_1** podrá encontrar los dos primeros ejercicios resueltos, según lo planteado en la primera parte de la prueba y en la carpeta **parte_2** podrá encontrar dos capetas llamadas my_swapi y swapi_docker, donde esta resuelta la segunda parte de prueba. Más adelante entraré a explicar el desarrollo de la prueba.

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

Ya descargado el repositorio, procederemos a abrir el archivo con Visual Studio Code o nuestro editor de codigo preferido; allí encontraremos una carpeta llamada **parte_1**, en esta carpeta habrá dos archivos **ejercicio_1.py** y **ejercicio_2.py**, ahora procederemos a ejecutar cada uno de estos archivos (para poder ejecutarlos debemos dirigirnos a la carpeta **parte_1** mediante consola).

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

## Solucion parte 2, prueba tecnica 📖

### Arquitectura my_swapi ⚙️

- my_swapi:
    - app:
        - fixtures: **_(Archivos a cargar registros en la base de datos)_**
            - characters.json
            - diretors.json
            - films.json
            - people.json
            - planets.json
            - producers.json
            - unittest.json
        - management:
            - commands:  **_(función para cargar registros en la base de datos)_**
                - load_fixtures.py
        - admin.py
        - apps.py
        - models.py
        - schema.py
        - tests.py
        - utils.py
        - views.py
    - extra: **_(Coleccion para cargar en postman)_**
        - SWAPI.postman_collection.json
    - my_swapi: **_(Archivos principales y configuraciones de la aplicación)_**
        - schema.py
        - settings.py
        - urls.py
        - wsgi.py
    - tests: **_(Archivos .py para test unitarios)_**
        - test_character.py
        - test_director.py
        - test_film.py
        - test_people.py
        - test_planet.py
        - test_producer.py
    - db.sqlite3 
    - manage.py
    - pytest.ini **_(Configuración para pruebas unitarias)_**
    - requirements.txt
    - tox.ini **_(Configuración para flake8)_**

Nos dirigimos a la carpeta llamada **parte_2**, en esta carpeta habrá dos carpetas **my_swapi** y **swapi_docker**, ahora procederemos a abrir la carpeta **my_swapi**.

#### Solución apartado 1 de la segunda parte de la prueba 📝

En la carpeta **app** dentro de **my_swapi**, encontraremos un archivo llamado **models.py** allí podremos ver los cambios hechos sobre la clase People y por consiguiente la solución a este apartado.

#### Solución apartado 2 de la segunda parte de la prueba 📝

En la carpeta **app** dentro de **my_swapi**, encontraremos un archivo llamado **utils.py**, allí podremos ver documentado con un docstring, dicha función, según la solución de este apartado.

#### Solución apartado 3 de la segunda parte de la prueba 📝

En la carpeta **app** dentro de **my_swapi**, encontraremos un archivo llamado **schema.py**, allí podremos visualizar la solución al apartado.

#### Solución apartado 4 y 5 de la segunda parte de la prueba 📝

En la carpeta **app** dentro de **my_swapi**, encontraremos dos archivos llamados **models.py** y **schema**, allí podremos visualizar la solución al los apartados.

#### Solución apartado 6 de la segunda parte de la prueba 📝
En la carpeta **tests** dentro de **my_swapi**, en esta carpeta prodremos encotrar 6 archivos **.py**, son las pruebas unitarias, y para configurar las pruebas unitarias con la herramienta **pytest** se encuentra el archivo **pytest.ini** dentro de **my_swapi**.

#### Solución apartado 7 de la segunda parte de la prueba 📝
En la carpeta **app** dentro de **my_swapi**, encontraremos un archivo llamado **models.py** allí podremos ver los cambios hechos sobre la clase People y por consiguiente la solución a este apartado.
***
### Ejecutando y probando aplicación 🚀

* ### Ejecutando migraciones y cargando registros a la base de datos

Para poder ejecutar el proyecto debemos dirigirnos mediante consola a la carpeta **my_swapi**, por consiguiente debemos escribir:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py load_fixtures
```

* #### PyTest

Ahora escribimos lo siguiente:
```
pytest
```
Esto lo hacemos para generar las pruebas unitarias con herramienta **_PyTest_** y poder estar seguros que nuestro proyecto esta corriendo correctamente antes de salir a producción.
#### Ejemplo:
![ScreenShot](/images/pytest1.jpg)

* #### Flake8
Escribimos lo siguiente:
```
flake8 .
```
Esto lo hacemos para cerciorarnos que nuestro proyecto tiene una sintaxis correcta y es un código de calidad, con la herramienta **_Flake8_**.
#### Ejemplo:
![ScreenShot](/images/flake.jpg)

* #### Ejecutando proyecto
Para correr nuestro proyecto:
```
python manage.py runserver
```
Una vez estemos corriendo el servidor, abrimos Postman e importamos nuestra colección, que tiene como nombre **_SWAPI.postman_collection.json_** que esta en **extra** en la carpeta **my_swapi**, allí podremos probar cada uno de los query, tanto como los que se añadieron **Character(Personaje)**, como los anteriores.

#### Colección Postman
![ScreenShot](/images/postman1.jpg)

## Creando contenedor de Docker para Django 🐍🐳

Este proyecto esta ubicado en la carpeta **parte_2** de nuestro proyecto clonado y tiene como nombre **swapi_docker**.
### Nota: 📢
> Dado que para crear un contenedor docker para Django, debemos cambiar varias líneas de código en settings.py y generar carpetas adicionales y configuraciones para nuestro contenedor; tome la decisión de crear un proyecto aparte para este apartado de la práctica.

>Tenga encuenta que para ejecutar correctamente el proyecto debe tener instalado Docker y debe dirigirse mediante consola de git bash a la carpeta **swapi_docker**).


### Arquitectura swapi_docker ⚙️

- my_swapi:
    - app:
        - fixtures: **_(Archivos a cargar registros en la base de datos)_**
            - characters.json
            - diretors.json
            - films.json
            - people.json
            - planets.json
            - producers.json
            - unittest.json
        - management:
            - commands:  **_(función para cargar registros en la base de datos)_**
                - load_fixtures.py
        - admin.py
        - apps.py
        - models.py
        - schema.py
        - tests.py
        - utils.py
        - views.py
    - config:
        - gunicorn:
            - conf.py **_(Configurando el servidor wsgi (guinicorn))_**
        - nginx:
            - conf.d:
                - local.conf **_(Configurando servidor inverso (nginx))_**
    - static
    - staticfiles: **_(Archivos estaticos generados)_**
        - admin
            - css
            - fonts
            - js
        - graphene_django
        - staticfiles.json
    - extra: **_(Coleccion para cargar en postman)_**
        - SWAPI.postman_collection.json
    - my_swapi: **_(Archivos principales y configuraciones de la aplicación)_**
        - schema.py
        - settings.py
        - urls.py
        - wsgi.py
    - tests: **_(Archivos .py para test unitarios)_**
        - test_character.py
        - test_director.py
        - test_film.py
        - test_people.py
        - test_planet.py
        - test_producer.py
    - docker-compose.yml **_(Archivo necesario para crear el contenedor)_**
    - Dockerfile.py **_(Archivo necesario para crear el contenedor)_**
    - manage.py
    - pytest.ini **_(Configuración para pruebas unitarias)_**
    - requirements.txt
    - tox.ini **_(Configuración para flake8)_**

***
### Ejecutando y creando contenedor 🚀🐳

Nos dirigimos a nuestro proyecto **swapi_docker** mediante consola y desde allí escribimos lo siguiente:
```
docker-compose up --build
```

Una vez crea el contenedor, debemos hacer las migraciones de nuestra aplicacion en el contenedor
```
docker-compose run django_app python manage.py makemigrations
```
```
docker-compose run django_app python manage.py migrate
```

Procedemos a cargar los registros en la base de datos
```
docker-compose run django_app python manage.py load_fixtures
```
Para que nos pueda mostrar los archivos estaticos
```
docker-compose run django_app python manage.py collectstatic
```
Hacer el **__Pytets__** antes de sacarlo a produccion
```
docker-compose run django_app pytest
```

Luego debemos correr el contenedor y volver hacer los query con los request en Postman.

## **__Eso es todo, muchas gracias__**. 🧑‍💻
