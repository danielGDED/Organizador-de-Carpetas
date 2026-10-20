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
    return

def tamano_legible(tamano_bytes):
    return

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
