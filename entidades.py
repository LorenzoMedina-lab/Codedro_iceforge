from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__ (self, nombre, energia):
        self._nombre = nombre          #Encapsulado
        self._energia = energia        #Encapsulado
        self._estado = "Activo"        #Encapsulado el "_"Representa la encapsulacion lo cual no permite que se modefique desde fuera

    # Getters y Setters para controlar el acceso a los atributos encapsulados (Getters para leer, Setters para modificar con validacion)
    @property
    def energia(self):  #Permite leer la energia sin acceder directamente a ella.
        return self._energia
    @property
    def nombre(self):  # Permite leer el nombre sin acceder directamente a el.
         return self._nombre

    @energia.setter
    def energia(self, valor):
        """Valida la vida y actualiza el estado automáticamente."""
        if valor <= 0:
            self._energia = 0
            self._estado = "Caido" # Por lo cual cuando esta en 0 el personaje a caido basicamente murio.
        elif valor > 100:
            self._energia = 100
        else:
            self._energia = valor

    # Metodo de instancia (La logica compartida)
    def recibir_daño(self, cantidad):
        # Al usar 'self.energia', Python llama automáticamente al @energia.setter
        self.energia -= cantidad   #Cada ves que recibe daño resta una cantidad de energia 
        print(f" {self._nombre} recibio {cantidad} de daño. Energia restante:{self.energia}")  #Cada ves que el jugador recibe daño eso muestra el daño recibido y la cantidad de energia que le queda luego del golpe

    @abstractmethod
    def ejecutar_turno(self):
            pass
    

    #Especialistas 
class Ingeniero(Entidad):
    def __init__(self, nombre, energia):
          super().__init__(nombre, energia) #Se llama al constructor de la base en este caso entidad
          self._potencia_reparacion = 15 # Esto es cuanto puede arreglar por turno esto es un atributo especifico 
    
    def ejecutar_turno(self):
        gasto_energia = 5
        # NOTA TÉCNICA: Usamos el método recibir_daño para que pase por el Setter
        self.recibir_daño(gasto_energia) #Aqui se utiliza de vuelta el metodo que ya fue creado Recibir daño
        print (f" {self._nombre} ha reparado el reactor termico.")
        print (f" Gasto de energia por trabajo: {gasto_energia}. Energia actual: {self.energia}")

        return self._potencia_reparacion # Esto devuelve la cantidad de reparaciones que realizo 
    
class Recolector(Entidad):
    def __init__(self, nombre, energia):
          super().__init__(nombre, energia)
          #Caracterista unica de clase Recolector
          self._capacidad_recoleccion = 20
    
    def ejecutar_turno(self):
        if self._estado == "Caido":   # Su es personaje esta caido no puede realizar acciones por lo cual aqui se valida eso
            print(f" {self._nombre} esta en el suelo y no puede buscar suministros.")
            return 0  #No aporta nada en este turno
          #Buscar en la tormenta claro que es agotador por lo cual ...
        desgaste = 10
        print (f" {self._nombre} se interna en la nieve buscando recursos....")
        self.recibir_daño(desgaste)
          # Si despues del desgaste quedo caido lo que pasara sera que recolectara la mitad por el esfuerzo empleado
        if self._estado == "Caido":
                print(f" {self._nombre} colapso durante la expediccion")
                return self._capacidad_recoleccion // 2 
          # Si todo salio bien devolvera el total de los recursos obtenidos 
        return self._capacidad_recoleccion
    
class Explorador(Entidad):
    def __init__(self, nombre, energia):
          super().__init__(nombre, energia)
          #caracterista unica de clase Explorador 
          self._rango_exploracion = 20
    
    def ejecutar_turno(self):
        if self._estado == "Caido": #Si el explorador eata caido no puede realizar acciones por lo cual aqui se valida eso
            print(f" {self._nombre} esta en el suelo y no puede seguir explorando.")
            return 0  #No aporta nada en este turno
        desgaste = 8 #Al explorar se cansa menos
        print(f" {self._nombre} esta mirando el horizonte...")
        self.recibir_daño(desgaste) 

        if self._estado == "Caido":
             print (f"{self._nombre} colapso durante la expediccion por lo cual no puede continuar")
             return self._rango_exploracion //2
        return self._rango_exploracion