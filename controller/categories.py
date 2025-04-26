import psycopg2
from controller.supabase import conectar_base_datos
def obtenerCategorias():
    conexion = conectar_base_datos()
    if conexion:
        cursor = conexion.cursor()
        query = """SELECT id, nombre FROM categorias"""
        cursor.execute(query)
        categorias_raw = cursor.fetchall()
        cursor.close()
        conexion.close()
        categorias = [
            {"id": row[0], "nombre": row[1]}
            for row in categorias_raw
        ]
        return categorias

def insertarCategoria(nombre):
    conexion = conectar_base_datos()
    if conexion is None:
        return "No se pudo conectar a la base de datos"

    cursor = conexion.cursor()

    query = """INSERT INTO categorias VALUES (DEFAULT, %s) RETURNING id"""
    try:
        cursor.execute(query, (nombre,))
        conexion.commit()
        return True
    except psycopg2.Error as err:
        return err
    finally:
        cursor.close()
        conexion.close()
        
def actualizarCategoria(id, nombre):
    conexion = conectar_base_datos()
    if conexion is None:
        return "No se pudo conectar a la base de datos"

    cursor = conexion.cursor()

    query = """UPDATE categorias SET nombre = %s WHERE id = %s"""
    try:
        cursor.execute(query, (nombre, id))
        conexion.commit()
        return True
    except psycopg2.Error as err:
        return err
    finally:
        cursor.close()
        conexion.close()
        
def eliminarCategoria(id):
    conexion = conectar_base_datos()
    if conexion is None:
        return "No se pudo conectar a la base de datos"

    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM categorias WHERE id = %s", (id))
            conexion.commit()
        return True
    except psycopg2.Error as err:
        return err
    finally:
        conexion.close()