import mysql.connector

def guardarnombre(nombre):
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Cazamobs1228.',
            database='nombres',
            port = '3306'
        )
        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()
        # Sentencia SQL para insertar el nombre en la tabla
        query = "INSERT INTO persona (nombre) VALUES (%s)"
        # Datos a insertar en la tabla (en este caso, solo el nombre)
        datos = (nombre,)
        # Ejecutar la sentencia SQL
        cursor.execute(query, datos)
        # Confirmar la inserción en la base de datos
        conexion.commit()
        print("Nombre guardado correctamente en MySQL")

    except mysql.connector.Error as error:
        print("Error al guardar el nombre en MySQL:", error)

    finally:
        # Cerrar el cursor y la conexión a la base de datos
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()

def main():
    while(True):
        nombre = input("Ingrese su nombre: ")

        # Guardar el nombre en MySQL
        guardarnombre(nombre)

if __name__ == "__main__":
    main()
