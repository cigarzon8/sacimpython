class Vehiculo:

    idusuario = int
    idVehiculo = int
    placa = str
    tipovehiculo = int
    estado = int

    def __init__(self, idusuario, idVehiculo, placa, tipovehiculo, estado):
        self.idusuario = idusuario
        self.idVehiculo = idVehiculo
        self.placa = placa
        self.tipovehiculo = tipovehiculo
        self.estado = estado

    def info(self):
        return (
            f"ID Usuario: {self.idusuario}\n"
            f"ID vehiculo: {self.idVehiculo}\n"
            f"Placa: {self.placa}\n"
            f"TipoVehiculo: {self.tipovehiculo}\n"
            f"Estado: {self.estado}"
        )
    def updatePlaca(self,placa):
        self.placa = placa
    def updateTipoVehiculo(self,tipovehiculo):
        self.tipovehiculo = tipovehiculo
    def updateEstado(self,estado):
        self.estado = estado
    def gestEstado(self):
        return(self.estado)
    def gestUsuarioId(self):
        return(self.idusuario)
    def gestId(self):
        return(self.idVehiculo)