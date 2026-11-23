class ServerException(Exception):
    """Excepción base de la aplicación."""
    pass


class CampoObligatorioError(ServerException):
    """Se dispara cuando un campo está vacío."""

    def __init__(self, mensaje="Campo obligatorio"):
        super().__init__(mensaje)


class ValidacionDatosError(ServerException):
    """Se dispara cuando los datos ingresados son inválidos."""
    pass


class ServidorNoEncontradoError(ServerException):
    """Se dispara cuando el servidor no existe."""

    def __init__(self, mensaje="Servidor no encontrado"):
        super().__init__(mensaje)


class ConsumoInvalidoError(ServerException):
    """Se dispara cuando el consumo eléctrico es negativo."""

    def __init__(self, mensaje="El consumo no puede ser negativo"):
        super().__init__(mensaje)