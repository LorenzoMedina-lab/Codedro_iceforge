from motor import Juego

def ejecutar_programa():
    # Se Crea la instancia del "Cerebro" del juego.
    # Al hacer esto, se ejecuta el __init__ de Juego y se crea el equipo.
    partida = Juego()
    
    # Se Llamama al método que contiene el bucle 'while'.
    # Aquí es donde el control pasa totalmente al Motor.
    partida.iniciar()

if __name__ == "__main__":
    print("--- 🧊 INICIANDO SISTEMA ICEFORGE 🧊 ---")
    ejecutar_programa()