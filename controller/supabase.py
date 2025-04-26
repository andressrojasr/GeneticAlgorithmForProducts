import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_base_datos():
    try:
        conexion = psycopg2.connect(
            host= os.getenv('HOST'),
            port= os.getenv('PORT'),
            dbname= os.getenv('DBNAME'),
            user= os.getenv('USER'),
            password= os.getenv('PASSWORD'),
            sslmode='require'
        )
        return conexion
    except psycopg2.Error as err:
        print(f"Error: {err}")
        return None