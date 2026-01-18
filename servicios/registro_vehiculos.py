# servicios/registro_vehiculos.py
# Capa de servicio: maneja la lógica (no define las entidades)

from typing import List
from modelos.vehiculo import Vehiculo

class RegistroVehiculos:
    def __init__(self):
        self._vehiculos: List[Vehiculo] = []

    def agregar(self, vehiculo: Vehiculo):
        # Validación simple: no repetir placa
        if any(v.placa == vehiculo.placa for v in self._vehiculos):
            raise ValueError(f"Ya existe un vehículo con placa {vehiculo.placa}")
        self._vehiculos.append(vehiculo)

    def listar(self) -> List[Vehiculo]:
        return self._vehiculos

    def total_a_pagar(self, horas: int) -> float:
        # Polimorfismo en acción:
        # aunque todos son Vehiculo, cada uno calcula su tarifa diferente
        return sum(v.calcular_tarifa(horas) for v in self._vehiculos)
