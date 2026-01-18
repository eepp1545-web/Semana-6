# main.py
# Punto de entrada: crea instancias y demuestra herencia, encapsulación y polimorfismo.

from modelos.auto import Auto
from modelos.moto import Moto
from servicios.registro_vehiculos import RegistroVehiculos

def main():
    registro = RegistroVehiculos()

    # Instancias (objetos) de clases derivadas (herencia)
    auto1 = Auto("pqr-789", "Chevrolet", puertas=2)
    moto1 = Moto("moto2", "Honda", cilindrada=250)

    # Encapsulación: la placa se valida y se normaliza (mayúscula)
    print("Placa auto (encapsulada):", auto1.placa)
    print("Placa moto (encapsulada):", moto1.placa)

    # Agregar a servicio (lógica)
    registro.agregar(auto1)
    registro.agregar(moto1)

    print("\n--- Vehículos registrados ---")
    for v in registro.listar():
        print(v.descripcion())

    horas = 6
    print(f"\n--- Tarifa por {horas} horas ---")
    for v in registro.listar():
        # Polimorfismo: cada objeto responde distinto al mismo método
        print(f"{v.descripcion()} -> Paga: ${v.calcular_tarifa(horas):.2f}")

    total = registro.total_a_pagar(horas)
    print(f"\nTOTAL a pagar por todos: ${total:.2f}")

if __name__ == "__main__":
    main()
