from clases.herencia1.taxi import Taxi
from clases.herencia1.auto_particular import AutoParticular

def main():
    coche= Taxi("123-GTO","Versa",1000,"123-a")
    
    
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()
    #crear el objeto de la clase
    ap= AutoParticular("456","Jaqueline","18","volvo","rojo","abc")#pasar los valores por parametro
    ap.subirAuto()
    ap.arrancarAuto()
    ap.llegarDestino()
    ap.bajarAuto()
    print("datos del usuario: ")
    print(ap)
    
    
    
if __name__=='__main__':
    main()
    