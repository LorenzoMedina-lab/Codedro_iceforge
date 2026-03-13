# main.py
# IMPORTACIÓN: Solo traemos el Motor.
from motor import Juego

def ejecutar_programa():
    # Razonamiento: Creamos la instancia del "Cerebro" del juego.
    # Al hacer esto, se ejecuta el __init__ de Juego y se crea el equipo.
    partida = Juego()
    
    # Razonamiento: Llamamos al método que contiene el bucle 'while'.
    # Aquí es donde el control pasa totalmente al Motor.
    partida.iniciar()

# El "Guardian" del script
if __name__ == "__main__":
    print("--- 🧊 INICIANDO SISTEMA ICEFORGE 🧊 ---")
    ejecutar_programa()