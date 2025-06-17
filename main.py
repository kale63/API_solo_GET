from fastapi import FastAPI
from pydantic import BaseModel
import csv

app = FastAPI()

# Actividad 1: GET de la API

class Alumnos(BaseModel):
    Matricula: str
    Nombre: str
    Edad: int
    Genero: str
    Carrera: str
    Semestre: int
    Trabajo: str
    Estado: str
    Hobby: str
    Preferencia: str
    
# Importar la lista de alumnos

classmates_list = []

with open('COPIA_bdmodelos.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=',')
    print("CSV headers:", reader.fieldnames)
    
    for row in reader:
        classmate = Alumnos(
            Matricula=row["Matricula"],
            Nombre=row["Nombre"],
            Edad=int(row["Edad"]),
            Genero=row["Genero"],
            Carrera=row["Carrera"],
            Semestre=int(row["Semestre"]),
            Trabajo=row["Trabajo"],
            Estado=row["Estado"],
            Hobby=row["Hobby"],
            Preferencia=row["Preferencia"]
        )
        classmates_list.append(classmate)

# Endpoints de primer nivel    
    
# Endpoint para obtener la lista completa de alumnos
@app.get("/alumnos/")
async def get_classmates():
    return classmates_list

@app.get("/alumnos/{matricula}")
async def get_classmate(matricula: str):
    for classmate in classmates_list:
        if classmate.Matricula == matricula:
            return classmate
    return {"error": "Alumno no encontrado"}

# Endpoints de segundo nivel

@app.get("/alumnos/edad/{edad}")
async def get_classmates_by_age(edad: int):
    filtered_classmates = [classmate for classmate in classmates_list if classmate.Edad == edad]
    if filtered_classmates:
        return filtered_classmates
    return {"error": "No se encontraron alumnos con esa edad"}

@app.get("/alumnos/estado/{estado}")
async def get_classmates_by_state(estado: str):
    filtered_classmates = [classmate for classmate in classmates_list if classmate.Estado.lower() == estado.lower()]
    if filtered_classmates:
        return filtered_classmates
    return {"error": "No se encontraron alumnos que vengan de ese estado"}

@app.get("/alumnos/carrera/{carrera}")
async def get_classmates_by_career(carrera: str):
    filtered_classmates = [classmate for classmate in classmates_list if classmate.Carrera.lower() == carrera.lower()]
    if filtered_classmates:
        return filtered_classmates
    return {"error": "No se encontraron alumnos en esa carrera"}

@app.get("/alumnos/{matricula}/hobby")
async def get_classmate_hobby(matricula: str):
    for classmate in classmates_list:
        if classmate.Matricula == matricula:
            return {"Hobby": classmate.Hobby}
    return {"error": "Alumno no encontrado"}

@app.get("/alumnos/{carrera}/preferencia")
async def get_classmates_by_career_preference(carrera: str):
    filtered_classmates = [classmate for classmate in classmates_list if classmate.Carrera.lower() == carrera.lower()]
    if filtered_classmates:
        return [{"Matricula": classmate.Matricula, "Preferencia": classmate.Preferencia} for classmate in filtered_classmates]
    return {"error": "No se encontraron alumnos en esa carrera"}

# Endpoints de tercer nivel

@app.get("/alumnos/edad/{edad}/carrera/{carrera}")
async def get_classmates_by_age_and_career(edad: int, carrera: str):
    filtered_classmates = [
        classmate for classmate in classmates_list 
        if classmate.Edad == edad and classmate.Carrera.lower() == carrera.lower()
    ]
    if filtered_classmates:
        return filtered_classmates
    return {"error": "No se encontraron alumnos con esa edad y carrera"}

@app.get("/alumnos/edad/{edad}/estado/{estado}")
async def get_classmates_by_age_and_state(edad: int, estado: str):
    filtered_classmates = [
        classmate for classmate in classmates_list 
        if classmate.Edad == edad and classmate.Estado.lower() == estado.lower()
    ]
    if filtered_classmates:
        return filtered_classmates
    return {"error": "No se encontraron alumnos con esa edad y estado"}

@app.get("/alumnos/carrera/{carrera}/semestre/{semestre}")
async def get_classmates_by_career_and_semester(carrera: str, semestre: int):
    filtered_classmates = [
        classmate for classmate in classmates_list 
        if classmate.Carrera.lower() == carrera.lower() and classmate.Semestre == semestre
    ]
    if filtered_classmates:
        return filtered_classmates
    return {"error": "No se encontraron alumnos en esa carrera y semestre"}

@app.get("/alumnos/estado/{estado}/carrera/{carrera}")
async def get_classmates_by_state_and_career(estado: str, carrera: str):
    filtered_classmates = [
        classmate for classmate in classmates_list 
        if classmate.Estado.lower() == estado.lower() and classmate.Carrera.lower() == carrera.lower()
    ]
    if filtered_classmates:
        return filtered_classmates
    return {"error": "No se encontraron alumnos de ese estado y carrera"}

# uvicorn main:app --reload