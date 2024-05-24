class Pago:

    intpago = int
    intcobro = int
    fecha = int
    tiposervicio = int
    tiempo = int
    estado = int
    valor = float

    def __init__(self, intpago, intcobro, fecha, tiposervicio,tiempo,estado,valor):
        self.intpago = intpago
        self.intcobro = intcobro
        self.fecha = fecha
        self.tiposervicio = tiposervicio
        self.tiempo = tiempo
        self.estado = estado
        self.valor = valor

    def info(self):
        return (
            f"ID pago: {self.intpago}\n"
            f"Estado: {self.estado}"
            f"ID cobrar: {self.intcobro}\n"
            f"Fecha: {self.fecha}\n"
            f"Tiposervicio: {self.tiposervicio}\n"
            f"Tiempo: {self.tiempo}\n"
            f"Valor: {self.valor}\n"
        )
    def updateEstado(self,estado):
        self.estado = estado
    def updateIntPago(self,intpago):
        self.intpago = intpago
    def updateIntCobro(self,intcobro):
        self.intcobro = intcobro
    def updateFecha(self,fecha):
        self.fecha = fecha
    def updateTipoServicio(self,tiposervicio):
        self.tiposervicio = tiposervicio
    def updateTiempo(self,tiempo):
        self.tiempo = tiempo
    def updateValor(self,valor):
        self.valor = valor

    def gestEstado(self):
        return(self.estado)
    def gestIdPago(self):
        return(self.intpago)