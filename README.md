# HabiAPI

Para llevar a cabo el desarrollo de esta prueba se utilizó Docker, Python, Flask y SQL.

## Ejecucion.
- Instalar Docker.
- Descargue o clone el repositorio https://github.com/carlosacg/HabiAPI
- Ingrese al directorio y ejecute el comando "sh run.sh"
- Despues de que el comando se ejecute abra un navegador e ingrese a la url http://localhost:8084/get_properties

## Como usar el servicio
- Solo existe un endpoint llamado get_properties, este recibe 3 filtros year, city y status. Si desea obtener el listado de propiedades con filtros especificos agregue esos parametros a la URL

- Ejemplo 1: http://localhost:8084/get_properties?year=2020
- Ejemplo 2: http://localhost:8084/get_properties?year=2020&city=bogota

## Primer requerimiento
El codigo fuente de este requerimiento se encuentra en el archivo "controlador.py"

Este endpoint retorna un JSON con la siguiente estructura

.. code-block:: bash

    [
        {
            "address": "calle 95 # 78 - 49",
            "city": "bogota",
            "description": "hermoso acabado, listo para estrenar",
            "price": 120000000,
            "status": "pre_venta"
        },
        {
            "address": "calle 95 # 78 - 123",
            "city": "bogota",
            "description": "hermoso acabado, listo para estrenar",
            "price": 120000000,
            "status": "pre_venta"
        }
    ]

Se crearon pruebas unitarias, para ejecutarlas escriba el comando "python tests.py"

## Segundo requerimiento
Para llevar a cabo el segundo requerimiento se penso en agregar una tabla intermedia entre los inmuebles y los usuarios llamada "like"

Diagrama entidad relacion disponible en: https://ibb.co/YpJfvLx

Esta solucion resolveria la necesidad de almacenar en base de datos los "me gusta" que cada usuario le da a un inmueble.

.. code-block:: bash

    CREATE TABLE like(
        id INT NOT NULL,
        property_id INT NOT NULL,
        user_id INT NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (property_id) REFERENCES property(id),
        FOREIGN KEY (user_id) REFERENCES auth_user(id)
    );


## Puntos Extras
El modelo actual obliga a tener que realizar JOIN entre tablas para obtener el estado actual de un inmueble.

El JOIN es un operacion costosa por lo cual hace que las consultas de datos masivos sea un poco lenta.

En estos casos lo mejor es desnormalizar la base de datos, agregando un campo "current_status" en la tabla property que almacena los inmuebles.

Este campo se actualizaria con un disparador (trigger) cuando se ingrese un nuevo registro en la tabla status_history asociado a un inmueble.

De esta forma el campo current status almacenaria el valor del ultimo estado del inmueble y no tendriamos que hacer JOINs en la consulta.
