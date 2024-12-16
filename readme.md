
# To-Do App 

Esta aplicación permite gestionar tareas mediante una interfaz web interactiva construida con **Streamlit**. Utiliza **SQLAlchemy** como ORM para interactuar con una base de datos MySQL. La app permite agregar, editar, eliminar tareas y cambiar su estado (Pendiente/Completado). Además, las tareas se guardan y se recuperan de una base de datos MySQL.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado Python y un entorno virtual configurado. Esta guía te ayudará a instalar y configurar todo lo necesario.


## Instalación

1. **Clona este repositorio** o descarga los archivos.

   ```bash
      git clone https://github.com/sebasrb08/to-do-python.git



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

![Captura de pantalla 2024-12-16 163923](https://github.com/user-attachments/assets/b010dee3-3610-413f-a069-4490727a8c79)


2. **Modal Agregar Tareas**

![Captura de pantalla 2024-12-16 170422](https://github.com/user-attachments/assets/8ed2b3a0-83ae-479e-800c-1b055827e158)


3. **Editar Tareas**

![image](https://github.com/user-attachments/assets/3167e177-a1c1-4325-a6e9-1733482a75a2)


4. **Cambiar estado**

![image](https://github.com/user-attachments/assets/0c05825d-4f4a-4440-8e65-65b560bc7970)


5. **Eliminar Tarea**
para poder eliminar la tarea , el estado debe estar "Completado":

![image](https://github.com/user-attachments/assets/9be07848-3347-40c6-bb5c-1a51a7165b38)

