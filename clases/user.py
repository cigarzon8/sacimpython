class Usuario:

    idusuario = int
    nombres = str
    apellidos = str
    correo = str
    telefono = int
    documento = int
    estado = int

    def __init__(self, idusuario, nombres, apellidos, correo, telefono, documento, estado):
        self.idusuario = idusuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.telefono = telefono
        self.documento = documento
        self.estado = estado

    def info(self):
        return (
            f"ID Usuario: {self.idusuario}\n"
            f"Nombres: {self.nombres}\n"
            f"Apellidos: {self.apellidos}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}\n"
            f"Documento: {self.documento}\n"
            f"Estado: {self.estado}"
        )
    def updateNombre(self,nombres):
        self.nombres = nombres
    def updateApellidos(self,apellidos):
        self.apellidos = apellidos
    def updateCorreo(self,correo):
        self.correo = correo
    def updateTelefono(self,telefono):
        self.telefono = telefono   
    def updateDocumento(self,documento):
        self.documento = documento   
    def updateEstado(self,estado):
        self.estado = estado
    def gestEstado(self):
        return(self.estado)
    def gestId(self):
        return(self.idusuario)