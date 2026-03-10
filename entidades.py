from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__ (self, nombre, energia):
        self._nombre = nombre          #Encapsulado
        self._energia = energia        #Encapsulado
        self._estado = "Activo"        #Encapsulado el "_"Representa la encapsulacion lo cual no permite que se modefique desde fuera
    
    # Metodo de instancia (La logica compartida)
    def recibir_daño(self, cantidad):
        self._energia -= cantidad   #Cada ves que recibe daño resta una cantidad de energia 
        if self._energia <= 0: #Si la cantidad de energia es igual a 0
            self._energia = 0 # Cantidad de energia queda en 0
            self._estado = "Caido" # Por lo cual cuando esta en 0 el personaje a caido basicamente murio.
        print(f"{self._nombre}recibio {cantidad}de daño. Energia restante:{self._energia}")  #Cada ves que el jugador recibe daño eso muestra el daño recibido y la cantidad de energia que le queda luego del golpe

    @abstractmethod
    def ejecutar_turno(self):
            pass
    

    #Especialistas 
class Ingeniero(Entidad):
     def __init__(self, nombre, energia):
          super().__init__(nombre, energia) #Se llama al constructor de la base en este caso entidad
          self._repuestos = 3 #Atributo unico de Ingeniero es la cantidad de reparaciones posibles
          #este es un atributo que solo le pertenece a esta clase por cual aunque herede entidad esto lo vuelve unico 
