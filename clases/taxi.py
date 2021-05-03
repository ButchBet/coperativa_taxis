from propietario import Propietario
from conductor import Conductor

class Taxi:
    def __init__(self, marca, modelo, placa, tamañoMotor, propietarioT, conductorT):
        self._marca = marca
        self._modelo = modelo
        self._placa = placa
        self._tamañoMotor = tamañoMotor
        self._propietarioT = propietarioT
        self._conductorT = conductorT

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def placa(self):
        return self._placa
    
    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def tamañoMotor(self):
        return self._tamañoMotor
    
    @tamañoMotor.setter
    def tamañoMotor(self, tamañoMotor):
        self._tamañoMotor = tamañoMotor


    def toString(self):
        cadena = "Taxi{marca : " + str(self._marca)
        cadena += ", modelo : " + str(self.modelo)
        cadena += ", placa : " + str(self.placa)
        cadena += ", tama\u00f1oMotor : " + str(self.tamañoMotor)
        cadena += ", nombre propietario: " + str(self._propietarioT.nombre)
        cadena += ", cédula propietario: " + str(self._propietarioT.cedula)
        cadena += ", teléfono propietario: " + str(self._propietarioT.telefono)
        cadena += ", nombre conductor: " + str(self._conductorT.nombre)
        cadena += ", cédula conductor: " + str(self._conductorT.cedula)
        cadena += ", salário conductor: " + str(self._conductorT.salario) + "}"
        return cadena

if __name__ == "__main__":
    propietario = Propietario(nombre="Oracio", cedula=10323020, telefono= 3135063124)
    conductor = Conductor(nombre="Alejandro", cedula=1007213957, salario=1250000)
    taxi = Taxi(marca="Cars", modelo=2014, placa="UTF-8", tamañoMotor=3000, propietarioT = propietario, conductorT = conductor)
    print(taxi.toString())