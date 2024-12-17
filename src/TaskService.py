from Task import Task
from Database import SessionLocal,Base,engine
import json

class TaskService :

    #Guarda las tareas en un archivo Json
    def guardar(self,tasks):
        try:
            archivo = "src/data.json"
            with open(archivo, "w") as json_file:
                json.dump(tasks, json_file, indent=4)
        except NameError as e:
            print("No se pudo guardar los datos de la tarea", e)

    #Obtiene los datos del archivo JSON
    def importar(self):
        try:
            with open("src/data.json", "r") as json_file:
                tasks = json.load(json_file)
            return tasks
        except :
            with open("src/data.json", "w") as archivo:
                json.dump([], archivo, indent=4)
            return []
        
    #Hace la conexion a la base de datos
    def connect_bd(self):
        try: 
            #Crea las tablas
            Base.metadata.create_all(bind=engine)
            session = SessionLocal()
            return session
        except Exception as e:
           return f"Error al traer los datos: {e}"
    
    #Obtiene todas las tareas de la base de datos y guarda y carga los archivos json
    def task_list(self):
        try:
            session=self.connect_bd()
            tasks = session.query(Task).all()
            data = self.convert(tasks)
            self.guardar(data)
            data = self.importar()
            return data
        except Exception as e:
           return f"Error cargando las tareas: {e}"
       
    #Agrega la tarea a la base de datos
    def task_add(self,title,description):
        try:
            task = Task(title,description,"Pendiente")
            session=self.connect_bd()
            session.add(task)
            session.commit()
            
        except Exception as e:
           return f"Error enviando las tareas: {e}"
    
    # Borra la tarea por el id en la base de datos
    def task_delete(self,id):
        try:
            session=self.connect_bd()
            task_id = session.query(Task).filter(Task.id== id).first()
            session.delete(task_id)
            session.commit()
            return   
        except Exception as e:
           return f"Error eliminado la tarea: {e}"
       
    # Cambia el estado de Pendiente a completado en la base de datos
    def change_state(self,id):
        try:
            session=self.connect_bd()
            task_id = session.query(Task).filter(Task.id== id).first()
            task_id.set_status("Completado")
            session.add(task_id)
            session.commit()  
        except Exception as e:
           return f"Error Cambiando el estado: {e}" 
       
    #Actualiza la tarea por el id en la base de datos
    def task_update(self,task,id):
        try:
            session=self.connect_bd()
            task_id = session.query(Task).filter(Task.id== id).first()
            task_id.title =task["title"]
            task_id.description =task["description"] 
            session.add(task_id)
            session.commit()
        except Exception as e:
            return f"Error Actualizando las tarea: {e}" 

    #Convierte una lista de clases a una lista de diccionarios
    def convert(self,tasks):
        data = []
        for task in tasks:
            data.append({
                "id":task.id,
                "title":task.title,
                "description":task.description,
                "status":task.status
            })
        return data
        