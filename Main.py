import os
import shutil

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt


console = Console()
# Muestra el titulo del programa
def mostrar_cabecera(console):
    console.print("[blue]Programa de organizacion de carpetas[/blue]")

def obtener_extension(nombre_archivo):
    ruta_archivo, extension = os.path.splitext(nombre_archivo)

    if not extension:
        return ruta_archivo, "sin_extension"
    else:
        return ruta_archivo, extension
    

def tamano_legible(tamano_bytes):

# Muestra el tamaño del archivo con los bytes
    kb = tamano_bytes // 1024
    bytes = tamano_bytes % 1024

    mb = kb // 1024
    kb = kb % 1024

    gb = mb // 1024
    mb = mb % 1024

    return gb, mb, kb, bytes

def una_dentro_de_otra(ruta_a, ruta_b):
# Comprueba si una ruta esta dentro de la otra

    ruta_absoluta_a = os.path.abspath(ruta_a) + os.sep
    ruta_absoluta_b = os.path.abspath(ruta_b) + os.sep
    
    return ruta_absoluta_a.startswith(ruta_absoluta_b) or ruta_absoluta_b.startswith(ruta_absoluta_a)


def nombre_disponible(ruta_destino, nombre_archivo):

# Da la ruta del archivo y en caso de que exista crea una nueva

    nueva_ruta = os.path.join(ruta_destino,nombre_archivo)

    if not os.path.exists(nueva_ruta):
        return nueva_ruta
    else:
        nombre, extension = os.path.split(nombre_archivo)
        contador = 1
        while os.path.exists(nueva_ruta):
            nueva_ruta = nombre + "_" + contador + extension
            
    return nueva_ruta


def clasificar_archivo(ruta_origen, nombre_archivo, ruta_destino,historial):
# Mueve el archivo a la carpeta/subcarpeta asignada
    ruta_total = os.path.join(ruta_origen, nombre_archivo)
    tamano = os.path.getsize(ruta_total)

    extension = obtener_extension(nombre_archivo)

    ruta_subcarpeta = os.path.join(ruta_destino, extension)
    os.makedirs(ruta_subcarpeta, exist_ok=True)

    nombre = nombre_disponible(ruta_subcarpeta, nombre_archivo)
    destino = os.path.join(ruta_subcarpeta,nombre)

    shutil.move(ruta_total,destino)

    movimiento_realizado = ruta_total + " -> " + destino

    historial.append(movimiento_realizado)

    return tamano

def clasificar_carpeta_recursivo(ruta_origen, ruta_destino,historial):
# Recorre todas las carpetas desde la ruta asignando donde va cada archivo y obteniendo su peso en bytes
    bytes_totales = 0

    archivos = os.listdir(ruta_origen)
    
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_origen, archivo)
        
        if os.path.isdir(ruta_archivo):
            bytes_totales += clasificar_carpeta_recursivo(ruta_origen,ruta_destino,historial)
        else:
            bytes_totales += clasificar_archivo(ruta_origen,archivo, ruta_destino,historial)
            

    return bytes_totales

def contar_archivos_recursivo(ruta):
    
    contador = 0
    
    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta,archivo)
        
        if os.path.isdir(ruta_archivo):
            contador += contar_archivos_recursivo(ruta_archivo)
        else:
            contador +1
    return



mostrar_cabecera(console)

crear_destino = False

console.print("\n[green]Introduzca la ruta de la carpeta de origen [/green]")

ruta_origen = Prompt.ask()


console.print("\n[green]Introduzca la ruta de la carpeta de destino [/green]")

ruta_destino = Prompt.ask()

if(ruta_origen == os.path.isdir()):
    if(ruta_destino == os.path.isdir()):
        pass
    elif(os.path.exists(ruta_destino)):
        crear_destino = True # PARA DESPUES CREAR ARCHIVO

    if(ruta_destino == ruta_origen or una_dentro_de_otra(ruta_origen,ruta_destino)):
        numero = 1



else:
    console.print(Panel("[red]La carpeta de origen no existe[/red]"))
