# Aplicacion SIATA

Juan Felipe Ramirez Castañeda  
Telematica 2023-10

## Indice
1. [Descripcion](#descripcion)
2. [Tecnologias](#tecnologias)
3. [Instalacion](#instalacion)
4. [Funcionamiento](#funcionamiento)
5. [Agradecimientos](#agradecimientos)

## Tabla de contenidos

### Descripcion

Este repositorio contiene un proyecto el cual consiste en una pagina web para monitorizar el nivel del agua en la ciudad de Medellin, Colombia.
La pagina web esta alojada en dos contenedores dentro de un mismo servidor, los contenedores hechos son estos:

* El frontend cuenta con dos paginas, una que permite ingresar al usuario mediante un usuario y una contraseña, y es donde se muestra el mapa con
los datos del nivel de cauce.
* El backend por su parte alberga la logica donde se obtienen los datos externos y los transforma a un formato usable para ser mostrado
en el frontend.  

Adicionalmente se trabaja con un volumen ubicado en la carpeta **volumenSIATA** el cual esta conectado con dos carpetas de nombre **datos**
con cada una perteneciendo a un contenedor. (la creacion del volumen se hace con propositos ilustrativos)

### Tecnologias

Las tecnologias usadas para la aplicacion son las siguientes:

* **Ubuntu server:** version 22.04 LTS
* **Python:** version 3.10
* **Docker:** version 20.10.21
* **Pip:** version 22.0.2
* **Flask:** version 2.3.2
* **Pandas:** version 2.0.1
* **Plotly:** version 2.20.0
* **Dash:** version 2.9.3

### Instalacion

**Importante:** a la hora de instalar el servidor el archivo **front.py** esta configurado para que su url este en el localhost, esto da problemas
a la hora de correr el contenedor del front, por lo cual se debe donde dice localhost reemplazarlo por la Ip privada del servidor.  

Una vez en el servidor ubuntu en el ambiente que se disponga se pueden instalar los contenedores por los siguientes metodos:

#### Por el Script

En la carpeta del proyecto se encuentra el script **scriptSiata.sh** este contiene todas las configuraciones necesarias para poder poner a funcionar la
pagina web, este script hara las siguientes funciones:

1. Instalar el paquete docker-compose en el servidor ubuntu.
2. Ejecutar los diferentes dockerfile para crear los dos contenedores.
3. Crear la carpeta donde estaran los volumenes.
4. Encender las maquinas y ponerlas a funcionar con sus respectivos volumenes.

Para ejecutar el script se pone:
```
$ bash scriptSIATA.sh
```

#### Instalacion manual

para instalar dockers:
```
$ sudo apt update
$ sudo apt install docker-compose
```
para crear los contenedores (se presupone que se realiza desde la carpeta del proyecto):
```
$ sudo docker build . -f DockerfileFront -t front:v01
$ sudo docker build . -f DockerfileApi -t api:v01
```
para correr los contenedores con volumenes (se presupone que se realiza desde la carpeta del proyecto):
```
$ sudo mkdir ~/volumenSIATA
$ sudo docker run -d -v ~/volumenSIATA:/datos -p 5000:5000 api:v01
$ sudo docker run -d -v ~/volumenSIATA:/datos -p 80:80 front:v01
```

### Funcionamiento

#### Parte del usuario

La pagina web esta puesta para funcionar por el puerto 80 por cualquier dispositivo con conexion a internet, para acceder se pone la direccion del servidor
en un navegador web.  

La pagina llevara al login del servidor, las contraseñas estan dadas en un diccionario en el archivo **front.py**, las contraseñas por defecto del sitio son:
* Usuario: **admin** - Contraseña: **root**
* Usuario: **user** - Contraseña: **pass01**

Una vez se ingrese la contraseña el servidor dara acceso a un mapa, en este se podran ver los datos de
las diferentes estaciones de monitoreo del cauce del SIATA en el valle de aburra, el resultado sera indicado cuando ponga click sobre la mancha azul que indica su
ubicacion, en cuanto mas nivel de cauce tenga la zona mas opaca se vera esta mancha.

#### Parte del codigo

La aplicacion consiste en una pagina dash, esta pagina contiene dos layout: uno es el que se usa para el login, con sus respectivos componentes. El segundo
contiene un mapa en el cual se muestran las estaciones del SIATA, el cual se hizo mediante unas listas en donde estan las coordenadas y el nivel del cauce, este
material se obtuvo mediante la funcion de readJSON de la libreria de pandas, cuya url es precisamente la IP privada del servidor por el puerto en
que se abrio la pagina del contenedor de la api. (puerto 5000)  

Por parte de la Api el codigo es hecho en una pagina de flask, el codigo consiste en una funcion en la que se lee
mediante la misma funcion de readJSON el contenido de la url donde se almacena la informacion del SIATA, esto ademas se le agrega una contraseña para
aumentar la seguridad del servidor, y ya tras eso se transforma y retorna el JSON a un diccionario para poder usarlo en el frontend.

### Agradecimientos

* Quiero agradecer al profesor Leonardo Betancur quien contribuyo en gran parte para el codigo de esta aplicacion.  
* Tambien agradecer a Ionos por dar la plantilla en que se baso este archivo README.  
* Agradecer a Plotply por proporcionar la documentacion para los callbacks de la aplicacion.  
* Agradecer a ChatGPT por ayudar a resolver algunas de las dudas e inconvenientes que se tuvieron haciendo este proyecto.