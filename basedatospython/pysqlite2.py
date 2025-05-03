import sqlite3

# Conexión y creación de tabla
conn = sqlite3.connect("alumnos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    correo TEXT
)
""")
conn.commit()

# Funciones principales
def agregar_estudiante(nombre, edad, correo):
    cursor.execute("INSERT INTO estudiantes (nombre, edad, correo) VALUES (?, ?, ?)", (nombre, edad, correo))
    conn.commit()
    print("Estudiante agregado correctamente.")

def mostrar_estudiantes():
    cursor.execute("SELECT * FROM estudiantes")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

def buscar_por_nombre(nombre):
    cursor.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?", ('%' + nombre + '%',))
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

# Menú principal
while True:
    print("\n1. Agregar estudiante\n2. Mostrar todos\n3. Buscar por nombre\n4. Salir")
    op = input("Elige una opción: ")

    if op == '1':
        nombre = input("Nombre: ")
        try:
            edad = int(input("Edad: "))
        except ValueError:
            print("Edad inválida.")
            continue
        correo = input("Correo: ")
        agregar_estudiante(nombre, edad, correo)

    elif op == '2':
        mostrar_estudiantes()

    elif op == '3':
        nombre = input("Nombre a buscar: ")
        buscar_por_nombre(nombre)

    elif op == '4':
        break

    else:
        print("Opción no válida.")

# Cierre de conexión
conn.close()
