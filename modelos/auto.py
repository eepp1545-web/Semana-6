# modelos/auto.py
# Clase derivada: hereda de Vehiculo y sobrescribe calcular_tarifa (polimorfismo)

from modelos.vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, placa: str, marca: str, puertas: int):
        super().__init__(placa, marca)
        self.puertas = puertas  # atributo propio del Auto

    # Polimorfismo: misma firma, comportamiento distinto
    def calcular_tarifa(self, horas: int) -> float:
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0.")
        # Ejemplo simple: $2 por hora
        return horas * 4.0
