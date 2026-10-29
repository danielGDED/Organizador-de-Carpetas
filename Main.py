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

    kb = tamano_bytes // 1024
    bytes = tamano_bytes % 1024

    mb = kb // 1024
    kb = kb % 1024

    gb = mb // 1024
    mb = mb % 1024

    return gb, mb, kb, bytes

def una_dentro_de_otra(ruta_a, ruta_b):
    
    return

def nombre_disponible(ruta_destino, nombre_archivo):
    return

def nombre_disponible(ruta_destino, nombre_archivo):
    return

def clasificar_archivo(ruta_origen, nombre_archivo, ruta_destino,historial):
    return

def clasificar_carpeta_recursivo(ruta_origen, ruta_destino,historial):
    return

def contar_archivos_recursivo(ruta):
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
