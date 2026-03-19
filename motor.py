from entidades import Ingeniero, Recolector, Explorador   #Motor

class Juego:
    def __init__(self):
        # Atributos Globales (Encapsulados)
        self._integridad_base = 100 # Si la integridad de la base llega a 0, perdemos.
        self._suministros = 50      # Si llega a 0, los personajes moriran de hambre sad....
        self._dia = 1 
        self._jugando = True

        #El equipo, los especialistas estan guardados en una lista para recorrerlos facilmente.
        self._equipo = [
            Ingeniero("Pengu", 100),
            Recolector("Bob", 100),
            Explorador("Charlie", 100)
        ]

    def mostrar_estado(self):
        #Muestra el estado actual del juego, como la integridad de la base, suministros y energia de cada especialista.
        print(f"\n--- 🧊 Día {self._dia} en Igloo Base ---")
        print(f"Base: {self._integridad_base}% | Suministros: {self._suministros}")
        print("-" * 30)

    def iniciar(self):
        #El inicio principal del juego, donde se ejecutan los turnos hasta que el juego termine.
        print("SISTEMA DE SIMULACIÓN ACTIVO. Sobrevive a esta tormenta.")

        while self._jugando:   # Aqui se utiliza el while para que el juego siga ejecutandose hasta que se cumpla una condicion de fin de juego.
            self.mostrar_estado() 
            
            # PASO 1 y 2: Cada especialista actúa
            for especialista in self._equipo: #Aqui es donde recorre la lista de especialistas para ejecutar cada turno.
                recurso,valor = especialista.ejecutar_turno() # El especialista ejecuta su turno y devuelve el tipo de accion y el valor asociado (reparacion o recoleccion)  
                
                #En el segundo paso se procesa segun el resultado de la clase.
                if recurso == "Base":
                    self._integridad_base += valor # Si el recurso es Base, se repara la base aumentando su integridad.
                        
                elif recurso == "Suministros":
                    self._suministros += valor # Si el recurso es Suministros, se suman los suministros recolectados a la reserva total.
                    
                elif recurso == "Exploracion":
                    print(f"-> {especialista.get_nombre()} ha despejado el camino.")
                if self._integridad_base > 100: self._integridad_base = 100 # Filtro para que la integridad de la base no supere el 100%

            #El paso 3 es desgaste diario de la colonia.
            self._suministros -= 20 #La colonia consume recursos cada dia.
            self._integridad_base -= 15 #El hielo daña la estructura.

            # Filtro para que los indicadores no muestren números negativos
            if self._suministros < 0: self._suministros = 0
            if self._integridad_base < 0: self._integridad_base = 0

            #El paso 4 es la verificacion de fin de la partida
            if self._integridad_base <= 0 or self._suministros <= 0:
                self.mostrar_estado() # Mostramos el desastre final antes de salir
                print("\n LA COLONIA HA PERECIDO. Fin de la simulación.")
                self._jugando = False
                break # Se rompe el ciclo inmediatamente

            #El control de avance
            input("\nPresiona Enter para pasar al siguiente dia....")
            self._dia += 1 # Aqui se incrementa para que el juego avance al siguiente dia.