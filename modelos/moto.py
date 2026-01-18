# modelos/moto.py
# Clase derivada: hereda de Vehiculo y sobrescribe calcular_tarifa (polimorfismo)

from modelos.vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, placa: str, marca: str, cilindrada: int):
        super().__init__(placa, marca)
        self.cilindrada = cilindrada  # atributo propio de la Moto

    # Polimorfismo: misma firma, comportamiento distinto
    def calcular_tarifa(self, horas: int) -> float:
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0.")
        # Ejemplo: motos pagan menos: $1.25 por hora
        return horas * 2.25
