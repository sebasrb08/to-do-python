import streamlit as st
from TaskService import TaskService


# Obtiene todo las tareas s
def get_task():
    task_service = TaskService()
    tasks =  task_service.task_list()
    st.session_state.tasks=tasks

# Agrega Todas las tareas 
def add_task():
    title=st.session_state.add["title"]
    description=st.session_state.add["description"]
    task_service = TaskService()
    task_service.task_add(title,description)


# Borra la tarea por su id
def delete_task(id):
    task_service = TaskService()
    task_service.task_delete(id)
    indice =next(i for i, task in enumerate(st.session_state.tasks) if task["id"] == id)
    st.session_state.tasks.pop(indice)



# Cambia el estado
def change_status(id):
    task_service = TaskService()
    task_service.change_state(id)
    

#Cambia el color del estado
def change_color(status):
    if status =="Pendiente":
        return "red"
    return "green"

# Modal para agreagar las tareas
@st.dialog("Tareas")
def add():
    st.write("Agregas Tareas")
    title = st.text_input("Titulo")
    description = st.text_input("Descripcion")
    if st.button("Guardar"):
        st.session_state.add = {"title": title, "description": description}
        add_task()
        st.rerun()

# Actualiza la tarea
def update_task():
    task_service = TaskService()
    task_service.task_update(st.session_state.updates,st.session_state.updateId)
    
# Muestra los titulos de cada columna de la tabla de tareas
def table_title():
    col1, col2, col3, col4,col5,col6 = st.columns([1,1, 2, 1, 1,1])
    col1.write("MARCAR")
    col2.write("TITULO")
    col3.write("DESCRIPCION")
    col4.write("ESTADO")
    col5.write("ELIMINAR")
    col6.write("EDITAR")


#Modal para actualizar las tareas
@st.dialog("Tareas")
def update(task):
    st.write("Actualizar Tareas")
    title = st.text_input("Titulo",task["title"])
    description = st.text_input("Descripcion",task["description"])
    if st.button("Actualizar"):
        st.session_state.updates = {"title": title, "description": description}
        st.session_state.updateId = task["id"]
        update_task()
        st.rerun()

#Crea el checkbox
def checkbox(index,col1,row):
    if col1.checkbox("",key=f"checkbox{index}" ):
            change_status(row["id"])
            st.rerun()

#Muestra los datos de la tabla
def view_task():
    for index, row in enumerate(st.session_state.tasks):
        col1, col2, col3, col4,col5,col6 = st.columns([1,1, 2, 1, 1,1])
        
        if row["status"] == "Pendiente":
            checkbox(index,col1,row)
            
        col2.write(row["title"])
        col3.write(row["description"])
        color=change_color(row["status"])
        col4.write(f':{color}[{row["status"]}]')
        
        if row["status"] == "Completado":   
            col5.button("Eliminar",on_click=lambda: delete_task(row["id"]), key=f"delete_{index}")


        if col6.button("Editar", key=f"update{index}"):
            update(row)

        

        
def main():
    
    st.title("Tareas")
    
    if st.button("Agregar", icon="➕"):
        add()
    get_task()
    with st.container():
        table_title()
        view_task()
        



if __name__ == "__main__":
    main()
