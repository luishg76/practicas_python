class Coche:
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Camion:
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
micoche=Coche()
micoche.desplazamiento()
micamiom=Camion()
micamiom.desplazamiento()

def DesplazamientoVehiculos(vehiculos):
    vehiculos.desplazamiento()

DesplazamientoVehiculos(micoche)
DesplazamientoVehiculos(micamiom)
