import sqlite3

miConexion=sqlite3.connect("db_prueba")
miCursor=miConexion.cursor()
miCursor.execute("CREATE  TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio REAL, seccion TEXT)")
#miCursor.execute("INSERT INTO productos(nombre, precio, seccion) VALUES('Pelota', 20.0,'Deportes')")
#miCursor.execute("INSERT INTO productos(nombre, precio, seccion) VALUES('Bate', 40.0,'Deportes')")
#miCursor.execute("INSERT INTO productos(nombre, precio, seccion) VALUES('Careta', 160.0,'Deportes')")
#lstproductos=[
 #   ("Jarrón", 10.0, "Ferretería"),
  #  ("Vaso", 2.0, "Ferretería"),
   # ("Plato", 6.0, "Ferretería")
#]

#miCursor.executemany("INSERT INTO productos(nombre, precio, seccion) VALUES(?,?,?)",lstproductos)
#miConexion.commit()
miCursor.execute("SELECT * FROM productos")
lstprodcutos=miCursor.fetchall()
print(lstprodcutos)

miConexion.close()