#referencia de la clase 
from clases.herencia2.persona import Persona

class AutoParticular(Persona):
    def __init__(self, clave, nombre, edad, marca, color, placa):
        super().__init__(clave, nombre, edad)
        self.marca = marca 
        self.color = color
        self.placa = placa
    def __str__(self):
        return super().__str__()+" "+self.marca+" "+self.color+" "+self.placa
        
    def subirAuto(self):
        print("subiendo al auto")
        
    def arrancarAuto(self):
        print("encendemos el estereo")
        print("arrancando auto")
    
    def llegarDestino(self):
        print("llegando al destino")
        
    def bajarAuto(self):
        print("bajando del auto")
        
        