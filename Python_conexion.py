import mysql.connector

def hacer_conexion():
    conexion = mysql.connector.connect(
        host="localhost", 
        database="tienda", 
        user="root", 
        password=""
    )
    return conexion

def agregar_cliente(nombre):
    conex = hacer_conexion()
    cursor = conex.cursor()
    sql = "INSERT INTO cliente (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conex.commit()
    print(f"Cliente {nombre} agregado.")
    conex.close()

def agregar_producto(nombre, precio, cantidad):
    conex = hacer_conexion()
    cursor = conex.cursor()
    sql = "INSERT INTO productos (nombre_producto, precio, cantidad) VALUES (%s, %s, %s)"
    valores = (nombre, precio, cantidad)
    cursor.execute(sql, valores)
    conex.commit()
    print(f"Producto {nombre} guardado.")
    conex.close()

def crear_recibo(id_client, id_product):
    conex = hacer_conexion()
    cursor = conex.cursor()
    sql = "INSERT INTO gestionar (id_client, id_product) VALUES (%s, %s)"
    cursor.execute(sql, (id_client, id_product))
    conex.commit()
    print("Recibo creado exitosamente.")
    conex.close()

def ver_ventas():
    conex = hacer_conexion()
    cursor = conex.cursor()
    sql = """
    SELECT gestionar.id_recibo, cliente.nombre, productos.nombre_producto
    FROM gestionar
    INNER JOIN cliente ON gestionar.id_client = cliente.id
    INNER JOIN productos ON gestionar.id_product = productos.id
    """
    cursor.execute(sql)
    for fila in cursor.fetchall():
        print(f"Recibo {fila[0]}: {fila[1]} compró {fila[2]}")
    conex.close()