class Automovil:
    
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        
    def encender(self):
        print('encender ' + self.marca)

    def avanzar(self):
        print('avanzar ' + self.marca)
        
    def acelerar(self):
        print('acelerar ' + self.marca)
        
    def frenar(self):
        print('frenar ' + self.marca)
        
# CREAMOS OBJETOS DE LA CLASE AUTOMOVIL
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
tico = Automovil(1990,'CH-5678','Rojo','Daewoo')
lamborghini = Automovil(2020,'CH-9101','Dorado','Lamborghini')

vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()
tico.encender()