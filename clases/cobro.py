class Cobro:

    idVehiculo = int
    fecha = int
    placa = str
    tiposervicio = int
    tiempo = int 
    estado = int
    valor = float

    def __init__(self, fecha, idVehiculo, placa, tiposervicio, estado,tiempo,valor):
        self.fecha = fecha
        self.idVehiculo = idVehiculo
        self.placa = placa
        self.tiposervicio = tiposervicio
        self.estado = estado
        self.tiempo = tiempo
        self.valor = valor

    def info(self):
        return (
            f"ID Usuario: {self.fecha}\n"
            f"ID vehiculo: {self.idVehiculo}\n"
            f"Placa: {self.placa}\n"
            f"TipoVehiculo: {self.tiposervicio}\n"
            f"Estado: {self.estado}"
            f"Tiempo: {self.tiempo}"
            f"Valor: {self.valor}"
        )
    def updatePlaca(self,placa):
        self.placa = placa
    def updateIdVehiculo(self,idVehiculo):
        self.idVehiculo = idVehiculo
    def updateEstado(self,estado):
        self.estado = estado
    def updateFecha(self,fecha):
        self.fecha = fecha
    def updateTiposervicio(self,tiposervicio):
        self.tiposervicio = tiposervicio
    def updateTiposervicio(self,tiempo):
        self.tiempo = tiempo
    def updateTiposervicio(self,valor):
        self.valor = valor
    def gestEstado(self):
        return(self.estado)
    def gestIdCobro(self):
        return(self.idVehiculo)