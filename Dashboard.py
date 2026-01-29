# ----------------------------------------
# Dashboard personalizado por GLADYS FIGUEROA COCHEA
# Asignatura: Programación Orientada a Objetos
# Función: Gestión, visualización y ejecución de scripts POO
# ----------------------------------------

import os
import subprocess


def mostrar_codigo(ruta_script):
    """
    Muestra el código fuente del script seleccionado
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(" El archivo no se encontró.")
        return None
    except Exception as e:
        print(f" Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """
    Ejecuta el script seleccionado en una nueva ventana
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux / Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f" Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """
    Muestra el menú principal del Dashboard
    """
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'UNIDAD 1',
        '2': 'UNIDAD 2'
    }

    while True:
        print("\n===================================")
        print("   DASHBOARD DE PROYECTOS POO")
        print("   Estudiante: Freddy Ríos")
        print("   Programación Orientada a Objetos")
        print("===================================")

        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Seleccione una opción: ")

        if eleccion_unidad == '0':
            print("Gracias por usar el Dashboard POO. ¡Hasta luego! ")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print(" Opción no válida. Intente nuevamente.")


def mostrar_sub_menu(ruta_unidad):
    """
    Muestra las subcarpetas dentro de una unidad
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n--- Submenú de Contenidos ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Seleccione una opción: ")

        if eleccion_carpeta == '0':
            break
        else:
            try:
                indice = int(eleccion_carpeta) - 1
                if 0 <= indice < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
                else:
                    print(" Opción fuera de rango.")
            except ValueError:
                print(" Entrada no válida.")


def mostrar_scripts(ruta_sub_carpeta):
    """
    Lista los scripts Python disponibles en la subcarpeta
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta)
               if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n--- Scripts Disponibles ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")
        print("9 - Menú principal")

        eleccion = input("Seleccione una opción: ")

        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)

                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1 = Sí | 0 = No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        else:
                            print("El script no fue ejecutado.")
                        input("\nPresione Enter para continuar...")
                else:
                    print(" Opción inválida.")
            except ValueError:
                print(" Entrada incorrecta.")


# -------------------------------
# Punto de entrada del programa
# -------------------------------
if __name__ == "__main__":
    mostrar_menu()
