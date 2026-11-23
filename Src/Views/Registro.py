import os
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6 import uic
from Controllers.ServerController import ServerController
from Exeptions.Exeptions import ValidacionDatosError, ServerException

class RegistroServerDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Cargar interfaz
        ruta_interfaz = os.path.join(
            os.path.dirname(__file__), "UI", "frm_registro.ui"
        )
        uic.loadUi(ruta_interfaz, self)

        # 2. Instanciar controlador
        self._controlador = ServerController()

        # 3. Vincular eventos
        self.btn_registrar.clicked.connect(self._registrar_servidor)
        self.btn_cancelar.clicked.connect(self.reject)

    def _registrar_servidor(self):

        rack = self.ln_rack.text()
        temperatura = self.ln_temperatura.text()
        consumo = self.ln_consumo.text()

        try:
            servidor = self._controlador.Registrar_Servidor(
                rack, temperatura, consumo
            )

            QMessageBox.information(self,
            "Registro exitoso",
            f"Servidor registrado correctamente.\n\n"
            f"Temperatura: {servidor.temperatura} °C\n"
            f"Estado: {servidor.mensaje_alerta}"
            )

            self.accept()

        except ValidacionDatosError as error:
            QMessageBox.warning(self, "Advertencia", str(error))

        except ServerException as error:
            QMessageBox.critical(self, "Error de sistema", str(error))