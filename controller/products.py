import psycopg2
from controller.supabase import conectar_base_datos
def obtenerProductos():
    conexion = conectar_base_datos()
    if conexion:
        cursor = conexion.cursor()
        query = """SELECT p.id, p.nombre, p.volumen, p.frecuencia, p.ganancia, p.url, c.id AS idCategoria, c.nombre AS nombreCategoria FROM productos p JOIN categorias c ON p."idCategoria" = c.id"""
        cursor.execute(query)
        productos_raw = cursor.fetchall()
        cursor.close()
        conexion.close()
        print(productos_raw)
        productos = [
            {"id": row[0], "nombre": row[1], "volumen": row[2], "frecuencia": row[3], "ganancia": row[4], "url": row[5], "idCategoria": row[6], "nombreCategoria": row[7]}
            for row in productos_raw
        ]
        return productos

def insertarProducto(nombre, volumen, ganancia, idCategoria, url):
    conexion = conectar_base_datos()
    if conexion is None:
        return "No se pudo conectar a la base de datos"

    cursor = conexion.cursor()

    query = """INSERT INTO productos (nombre, volumen, ganancia, "idCategoria", url) VALUES (%s, %s, %s, %s, %s)"""
    try:
        cursor.execute(query, (nombre, volumen, ganancia, idCategoria, url))
        conexion.commit()
        return True
    except psycopg2.Error as err:
        return err
    finally:
        cursor.close()
        conexion.close()
        
def actualizarProducto(id, nombre, volumen, ganancia, idCategoria, url):
    conexion = conectar_base_datos()
    if conexion is None:
        return "No se pudo conectar a la base de datos"

    cursor = conexion.cursor()

    query = """UPDATE productos SET nombre = %s, volumen = %s, ganancia = %s, "idCategoria"= %s, url= %s WHERE id = %s"""
    try:
        cursor.execute(query, (nombre, volumen, ganancia, idCategoria, url, id))
        conexion.commit()
        return True
    except psycopg2.Error as err:
        return err
    finally:
        cursor.close()
        conexion.close()
        
def eliminarProducto(id):
    conexion = conectar_base_datos()
    if conexion is None:
        return "No se pudo conectar a la base de datos"

    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM productos WHERE id = %s", (id, ))
            conexion.commit()
        return True
    except psycopg2.Error as err:
        return err
    finally:
        conexion.close()
        
def getProducts(category):
    conexion = conectar_base_datos()
    if conexion:
        cursor = conexion.cursor()
        query = """SELECT p.id, p.nombre, p.volumen, p.frecuencia, p.ganancia, p.url, c.id AS idCategoria, c.nombre AS nombreCategoria FROM productos p JOIN categorias c ON p."idCategoria" = c.id WHERE c.id = %s ORDER BY p.id ASC"""
        cursor.execute(query, (category, ))
        productos_raw = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos_raw
    
if __name__ == "__main__":
    # Test the functions here if needed
    pass
from controller.supabase import conectar_base_datos