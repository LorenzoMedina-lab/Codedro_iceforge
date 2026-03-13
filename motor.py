from entidades import Ingeniero, Recolector, Explorador

class Juego:
    def __init__(self):
        # Atributos Globales (Encapsulados)
        self._integridad_base = 100 
        self._suministros = 50      
        self._dia = 1 
        self._jugando = True

        # El equipo está guardado en una lista para recorrerlos fácilmente (Polimorfismo)
        self._equipo = [
            Ingeniero("Pengu", 100),
            Recolector("Bob", 100),
            Explorador("Charlie", 100)
        ]

    def mostrar_estado(self):
        print(f"\n--- 🧊 Día {self._dia} en Igloo Base ---")
        print(f"Base: {self._integridad_base}% | Suministros: {self._suministros}")
        print("-" * 30)

    def iniciar(self):
        print("SISTEMA DE SIMULACIÓN ACTIVO. Sobrevive a esta tormenta.")

        while self._jugando:
            self.mostrar_estado() 
            
            # PASO 1 y 2: Cada especialista actúa
            for especialista in self._equipo: 
                valor = especialista.ejecutar_turno()
                
                # Procesamos según la clase (Discernimiento técnico)
                if isinstance(especialista, Ingeniero):
                    self._integridad_base += valor
                elif isinstance(especialista, Recolector):
                    self._suministros += valor
                elif isinstance(especialista, Explorador):
                    print(f"-> {especialista._nombre} ha despejado el camino.")

            # Paso 3: Desgaste diario de la colonia
            self._suministros -= 20 
            self._integridad_base -= 15 

            # Paso 4: Verificación de fin de partida (Derrota)
            if self._integridad_base <= 0 or self._suministros <= 0:
                print("\n LA COLONIA HA PERECIDO. Fin de la simulación.")
                self._jugando = False
                break # Rompemos el ciclo inmediatamente

            # Control de avance
            input("\nPresiona Enter para pasar al siguiente dia....")
            self._dia += 1