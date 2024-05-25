class Tipoestado:

    idestado = int
    nombreestado = str
    seccion = int

    def __init__(self, idestado, nombreestado, seccion):
        self.idestado = idestado
        self.nombreestado = nombreestado
        self.seccion = seccion

    def info(self):
        return (
            f"ID Estado: {self.idestado}\n"
            f"Nombre Estado: {self.nombreestado}\n"
            f"Seccion: {self.seccion}\n"
        )
    def updateIdEstado(self,idestado):
        self.idestado = idestado
    def updateNombreEstado(self,nombreestado):
        self.nombreestado = nombreestado
    def updateseccion(self,seccion):
        self.seccion = seccion
    def gestNombreEstado(self):
        return(self.nombreestado)
    def gestIdParqueadero(self):
        return(self.intparqueadero)