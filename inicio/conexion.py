from logging import exception
import mysql.connector
from mysql.connector import Error

def conexion():
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',database='python')
        if conn.is_connected() :
            return conn

        else:
            print("No se pudo conectar ala base de datos")
    
    except Error as error:
        print(error)

def ingresarDatos():
    try:
        conn = conexion()
        cursor =conn.cursor()

        consulta = "insert into usuario(nombre , apellido) values (%s,%s)"
        valores =('maria','mendosa')

        cursor.execute(consulta,valores)
        conn.commit()
        print("guardados los datos")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("conexion terminada")
        else:
            print("no se pudo conectar")

def mostrarTodo():
    try:
        conn = conexion()
        cursor = conn.cursor()

        consulta = "SELECT * FROM usuario"
        cursor.execute(consulta)
        registros = cursor.fetchall()

        for registro in registros:
            print (registro)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("conexion terminada")
        else:
            print("no se pudo conectar")

mostrarTodo()