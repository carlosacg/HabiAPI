# HabiAPI

Para llevar a cabo el desarrollo de esta prueba se utilizara Docker, Python, Flask y consultas SQL.

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

## Segundo requerimiento