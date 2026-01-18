# modelos/vehiculo.py
# Clase base (POO): herencia + encapsulación + polimorfismo (se sobrescribe en hijas)

class Vehiculo:
    def __init__(self, placa: str, marca: str):
        # Encapsulación: atributo "privado" por convención (underscore)
        self._placa = None
        self.placa = placa  # usamos el setter para validar
        self.marca = marca

    # Encapsulación: getter
    @property
    def placa(self) -> str:
        return self._placa

    # Encapsulación: setter con validación
    @placa.setter
    def placa(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 5:
            raise ValueError("La placa debe ser un texto de al menos 5 caracteres.")
        self._placa = value.strip().upper()

    # Método común (puede ser polimórfico si se sobrescribe)
    def calcular_tarifa(self, horas: int) -> float:
        """
        Método pensado para polimorfismo:
        las clases hijas lo sobrescriben con su propia implementación.
        """
        raise NotImplementedError("Este método debe ser sobrescrito en las clases derivadas.")

    def descripcion(self) -> str:
        return f"{self.__class__.__name__} - Placa: {self.placa}, Marca: {self.marca}"
