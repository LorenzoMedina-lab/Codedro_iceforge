from abc import ABC, abstractmethod       #Dominio

class Entidad(ABC):  # Clase padre
    def __init__ (self, nombre, energia):
        self._nombre = nombre          #Encapsulado
        self._energia = energia        #Encapsulado
        self._estado = "Activo"        #Encapsulado el "_"Representa la encapsulacion lo cual no permite que se modefique desde fuera

    # Getters y Setters
    def get_nombre(self):
         return self._nombre
    def get_energia(self):
         return self._energia
    def set_energia(self, valor):
         if valor < 0:
              self._energia = 0
              self._estado = "Caido" # Si la energia llega a 0, el estado cambia a caido
              print(f"DESESPERADO: {self._nombre} ha caido en la nieve...") # Mensaje de que el personaje ha caido
         elif valor > 100:
                self._energia = 100
         else:
              self._energia = valor

    # Metodo de instancia (La logica compartida)
    def recibir_daño(self, cantidad):
         print (f"Desgaste {self._nombre} antes de recibir daño: {self.get_energia()}") # Mensaje que muestra la energia antes de recibir daño
         nueva_energia = self.get_energia() - cantidad
         self.set_energia(nueva_energia) # Se usa el setter para actualizar la energia y manejar el estado
         print(f"Desgaste {self._nombre} después de recibir daño: {self.get_energia()}") # Mensaje que muestra la energia despues de recibir daño
         print(f" {self._nombre} recibio {cantidad} de daño. Energia actual: {self.get_energia()}") # Mensaje que muestra el daño recibido y la energia actual

    @abstractmethod
    def ejecutar_turno(self):
            pass
    

    #Especialistas 
class Ingeniero(Entidad):
    def __init__(self, nombre, energia):
          super().__init__(nombre, energia) #Se llama al constructor de la base en este caso entidad
          self._potencia_reparacion = 15 # Esto es cuanto puede arreglar por turno esto es un atributo especifico 
    
    def ejecutar_turno(self):
        # Se usa el método recibir_daño para que pase por el Setter
        self.recibir_daño(5) #Aqui se utiliza de vuelta el metodo que ya fue creado Recibir daño
        print (f" {self.get_nombre()} ha reparado el reactor termico.")
        return "Base", self._potencia_reparacion # Esto devuelve el tipo de accion y la cantidad de reparacion que realizo el ingeniero

    
class Recolector(Entidad):
    def __init__(self, nombre, energia):
          super().__init__(nombre, energia)
          #Caracterista unica de clase Recolector
          self._capacidad_recoleccion = 20
    
    def ejecutar_turno(self):
         if self._estado == "Caido":
              print(f" {self.get_nombre()} esta caido y no puede recolectar.")
              return "Suministros", 0 # Si el recolector esta caido no puede recolectar por lo cual se devuelve 0
         print(f" {self.get_nombre()} esta buscando suministros...")
         self.recibir_daño(10) # Al recolectar se cansa mas por lo cual recibe mas daño

         puntos = self._capacidad_recoleccion // 2 if self._estado == "Caido" else self._capacidad_recoleccion # Si despues del desgaste quedo caido lo que pasara sera que recolectara la mitad por el esfuerzo empleado
         return "Suministros", puntos # Esto devuelve el tipo de accion y la cantidad de suministros recolectados
    
class Explorador(Entidad):
    def __init__(self, nombre, energia):
          super().__init__(nombre, energia)
          #caracterista unica de clase Explorador 
          self._rango_exploracion = 20
    
    def ejecutar_turno(self):
        if self._estado == "Caido": return "Exploracion", 0 # Si el explorador esta caido no puede explorar por lo cual se devuelve 0
        self.recibir_daño(8) # Al explorar se cansa menos por lo cual recibe menos daño
        print(f" {self._nombre} esta mirando el horizonte...")
        puntos = self._rango_exploracion // 2 if self._estado == "Caido" else self._rango_exploracion # Si despues del desgaste quedo caido lo que pasara sera que explorara la mitad por el esfuerzo empleado
        return "Exploracion", puntos # Esto devuelve el tipo de accion y la cantidad de exploracion realizada