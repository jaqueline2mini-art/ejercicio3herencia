class Vehiculo(object):
    def __init__(self,matricula,modelo,potenciaCV):
        self.matricula= matricula
        self.modelo= modelo
        self.potenciaCV= potenciaCV
        
    def __str__(self):
        return self.matricula +""+ self.modelo +""+ str(self.potenciaCV)
    
    def encender(self):
        print('encendiendo vehiculo')
        
    def acelerar(self):
        print('acelerando vehiculo')
        
    def frenar(self):
        print('frenando vehiculo')
        
        
    