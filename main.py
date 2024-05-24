from clases.user import Usuario
from clases.vehiculo import Vehiculo
from clases.cobro import Cobro
from clases.parqueadero import Parqueadero
from clases.pago import Pago


if __name__ == "__main__":
    usuario1 = Usuario(1, "Juan", "Pérez", "juan.perez@example.com", 1234567890, 987654321, 1)
    print(usuario1.info())
    print(usuario1.gestEstado())
    usuario1.updateNombre('agua')