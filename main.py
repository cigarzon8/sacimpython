from clases.user import Usuario
from clases.vehiculo import Vehiculo
from clases.cobro import Cobro
from clases.pago import Pago
from clases.parqueadero import Parqueadero
from clases.tipoestados import Tipoestado

if __name__ == "__main__":

    ##prueba usuario
    usuario1 = Usuario(1, "Juan", "Pérez", "juan.perez@example.com", 1234567890, 987654321, 1)
    print(usuario1.info())
    print("\n")
    print(usuario1.gestEstado())
    print("\n")
    usuario1.updateNombre('pedro')
    print(usuario1.info())
    print("\n")

    ##prueba Vehiculo
    vehiculo1 = Vehiculo(1,1,'abc123',1,1)
    print(vehiculo1.info())
    print("\n")
    print(vehiculo1.gestEstado())
    print("\n")
    vehiculo1.updatePlaca('xyz789')
    print(vehiculo1.info())
    print("\n")


    ##prueba cobro
    cobro1 = Cobro(1716595626,1,'xyz789',1,1,3600,123456789)
    print(cobro1.info())
    print("\n")
    print(cobro1.gestEstado())
    print("\n")
    cobro1.updateValor(987654321)
    print(cobro1.info())
    print("\n")


    ##prueba pago
    pago1 = Pago(1,1,1716595626,1,3600,1,123456789)
    print(pago1.info())
    print("\n")
    print(pago1.gestEstado())
    print("\n")
    pago1.updateValor(987654321)
    print(pago1.info())
    print("\n")

    ##prueba parqueadero
    parqueadero1 = Parqueadero(1,1,3600,1)
    print(parqueadero1.info())
    print("\n")
    print(parqueadero1.gestEstado())
    print("\n")
    parqueadero1.updateEstado(2)
    print(parqueadero1.info())
    print("\n")

    ##prueba Tipoestado
    tipoestado1 = Tipoestado(1,"Activo",1)
    print(tipoestado1.info())
    print("\n")
    print(tipoestado1.gestNombreEstado())
    print("\n")
    tipoestado1.updateNombreEstado("desactivado")
    print(tipoestado1.info())
    print("\n")