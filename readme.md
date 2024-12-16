
# To-Do App 

Esta aplicación permite gestionar tareas mediante una interfaz web interactiva construida con **Streamlit**. Utiliza **SQLAlchemy** como ORM para interactuar con una base de datos MySQL. La app permite agregar, editar, eliminar tareas y cambiar su estado (Pendiente/Completado). Además, las tareas se guardan y se recuperan de una base de datos MySQL.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado Python y un entorno virtual configurado. Esta guía te ayudará a instalar y configurar todo lo necesario.


## Instalación

1. **Clona este repositorio** o descarga los archivos.

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <CARPETA_DEL_REPOSITORIO>
Crea un entorno virtual (opcional pero recomendado):

2. **Crea un entorno virtual**

    ```bash
    python -m venv venv
    venv\Scripts\activate


3. **Instalacion de dependencias**
    ```bash
    pip install streamlit sqlalchemy mysql-connector-python python-dotenv

4. **Configuración de la base de datos**
4.1. Crea una base de datos en MySQL

    CREATE DATABASE sqlalchemy;

4.2. Crea un archivo .env

Crea un archivo llamado .env en la raíz de tu proyecto. Este archivo contendrá las credenciales de tu base de datos MySQL. Configura el archivo .env con tus valores personalizados como se muestra a continuación:

    DB_USERNAME=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_HOST= tu_host
    DB_PORT=tu_puerto
    DB_NAME=nombre_de_tu_base_de_datos


5. **Inicia la aplicación de Streamlit:**

    ```bash
    streamlit run src/app.py
    ```


## Pantallas

1. **Pantalla de Inicio (Listado de Tareas)**

2. **Modal Agregar Tareas**

3. **Editar Tareas**

4. **Cambiar estado**

5. **Eliminar Tarea**
para poder eliminar la tarea , el estado debe estar "Completado":
