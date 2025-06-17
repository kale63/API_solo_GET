# Actividad_1: API solo GET

Antes de construir los endpoints, se realizó una limpieza y agrupación de los datos provenientes del archivo CSV para asegurar consistencia y facilitar futuras consultas. Los principales cambios fueron:

- Agrupación de hobbies: Se agruparon actividades similares en categorías generales. Por ejemplo, "escuchar música" y "tocar instrumentos" se unificaron en "música", mientras que ir al  gym y varios deportes se agruparon como "ejercicio".

- Normalización de nombres de carrera: Las carreras fueron simplificadas a sus claves, como "ITI", para mantener un formato uniforme, corto y simple.

- Revisión de campos clave: Se estandarizaron los valores de campos como “Preferencia” o “Estado” para prevenir errores al consultar.

Este preprocesamiento permite trabajar con datos más limpios y estructurados, lo cual mejora tanto la calidad del API como la experiencia del usuario al interactuar con los endpoints. 

Después de esto, importamos los datos que provienen de un archivo CSV que luego se convierte en modelos de Pydantic y creamos los endpoints de FastAPI en una estructura jerárquica de tres niveles para consultar estudiantes a partir de los datos proporcionados por un archivo CSV. A continuación se detalla las peticiones disponibles:

## Primer nivel

1. GET /alumnos/
Devuelve todos los alumnos registrados.

- /alumnos/

2. GET /alumnos/{matricula}
Busca un alumno por su matrícula.
Devuelve sus datos si se encuentra o muestra un mensaje de error.

Ejemplo:
/alumnos/202230800
/alumnos/202214537

## Segundo nivel

3. GET /alumnos/edad/{edad}
Filtra a los alumnos por su edad exacta.

Ejemplo: /alumnos/edad/21

4. GET /alumnos/estado/{estado}
Filtra a los alumnos por su estado de origen.

Ejemplo: /alumnos/estado/Puebla

5. GET /alumnos/carrera/{carrera}
Lista a los alumnos de una carrera específica.

Ejemplo: /alumnos/carrera/ITI

6. GET /alumnos/{matricula}/hobby
Muestra el hobby de un alumno específico según su matrícula.

Ejemplo: /alumnos/202230800/hobby

7. GET /alumnos/{carrera}/preferencia
Devuelve la preferencia de cada alumno en una carrera específica.

Ejemplo: /alumnos/ITI/preferencia

## Tercer nivel

8. GET /alumnos/edad/{edad}/carrera/{carrera}
Filtra alumnos por su edad y carrera.

Ejemplo: /alumnos/edad/20/carrera/ITI

9. GET /alumnos/edad/{edad}/estado/{estado}
Filtra por edad y estado de origen.

Ejemplo: /alumnos/edad/20/estado/Tlaxcala

10. GET /alumnos/carrera/{carrera}/semestre/{semestre}
Filtra los alumnos por carrera y semestre.

Ejemplo: /alumnos/carrera/ICC/semestre/8

11. GET /alumnos/estado/{estado}/carrera/{carrera}
Filtra a los alumnos por su estado de origen y carrera.

Ejemplo: /alumnos/estado/Oaxaca/carrera/ITI

