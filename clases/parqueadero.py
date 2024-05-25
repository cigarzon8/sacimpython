class Parqueadero:

    intparqueadero = int
    estado = int
    tipoparqueadero = int
    tipovehiculo = int

    def __init__(self, intparqueadero, estado, tipoparqueadero, tipovehiculo):
        self.intparqueadero = intparqueadero
        self.estado = estado
        self.tipoparqueadero = tipoparqueadero
        self.tipovehiculo = tipovehiculo

    def info(self):
        return (
            f"ID Parqueadero: {self.intparqueadero}\n"
            f"Estado: {self.estado}\n"
            f"Tipo parqueadero: {self.tipoparqueadero}\n"
            f"Placa: {self.tipovehiculo}\n"
        )
    def updateIntParqueadero(self,intparqueadero):
        self.intparqueadero = intparqueadero
    def updateEstado(self,estado):
        self.estado = estado
    def updateTipoParqueadero(self,tipoparqueadero):
        self.tipoparqueadero = tipoparqueadero
    def updateTipoVehiculo(self,tipovehiculo):
        self.tipovehiculo = tipovehiculo

    def gestEstado(self):
        return(self.estado)
    def gestIdParqueadero(self):
        return(self.intparqueadero)