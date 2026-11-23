from Models.Entities.NodoServidor import NodoServidor
from Exeptions.Exeptions import ValidacionDatosError
from Models.ServerModel import ServerModel


class ServerController:

    def Listar_Servidores(self):
        return ServerModel.listar_Servidores()

    def Busqueda(self, criterio: str):
        return ServerModel.Busqueda(criterio)

    def Registrar_Servidor(self, rack: str, temperatura: str, consumo: str) -> NodoServidor:

        if not rack.strip() or not temperatura.strip() or not consumo.strip():
            raise ValidacionDatosError("Todos los campos son obligatorios.")

        try:
            rack = int(rack)
            temperatura = float(temperatura)
            consumo = float(consumo)
        except ValueError:
            raise ValidacionDatosError("Debe ingresar valores numéricos.")

        if rack <= 0:
            raise ValidacionDatosError("El rack debe ser mayor a cero.")

        if consumo < 0:
            raise ValidacionDatosError("El consumo no puede ser negativo.")

        if temperatura < 18:
            mensaje_alerta = "SOBREENFRIAMIENTO / ALTO GASTO"
        elif temperatura <= 24:
            mensaje_alerta = "TEMPERATURA OPTIMA"
        else:
            mensaje_alerta = "ALERTA CRITICA: SOBRECALENTAMIENTO"

        servidor = NodoServidor(rack, temperatura, consumo, mensaje_alerta)

        ServerModel.RegistrarServidor(rack, temperatura, consumo, mensaje_alerta)

        return servidor