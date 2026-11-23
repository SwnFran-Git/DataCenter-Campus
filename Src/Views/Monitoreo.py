import os
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6 import uic
from Controllers.ServerController import ServerController
from Exeptions.Exeptions import ValidacionDatosError, ServerException
from Views.Registro import RegistroServerDialog
class ServerView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Cargar interfaz gráfica
        ruta_interfaz = os.path.join(
            os.path.dirname(__file__), "UI", "frm_Monitoreo.ui"
        )
        uic.loadUi(ruta_interfaz, self)

        # 2. Instanciar controlador
        self._controlador = ServerController()

        # 3. Vincular eventos
        self.ln_Busqueda.textChanged.connect(self._buscar_servidores)
        self.btn_Registro.clicked.connect(self._abrir_registro)

        # 4. Cargar servidores al iniciar
        self._listar_servidores()

    def _listar_servidores(self):
        try:
            servidores = self._controlador.Listar_Servidores()
            self._cargar_tabla(servidores)

        except ServerException as error:
            QMessageBox.critical(self, "Error de sistema", str(error))

    def _buscar_servidores(self):
        criterio = self.ln_Busqueda.text()

        try:
            servidores = self._controlador.Busqueda(criterio)
            self._cargar_tabla(servidores)

        except ValidacionDatosError as error:
            QMessageBox.warning(self, "Advertencia", str(error))

        except ServerException as error:
            QMessageBox.critical(self, "Error de sistema", str(error))

    def _cargar_tabla(self, servidores):
        self.tbl_Servers.setRowCount(len(servidores))

        for fila, servidor in enumerate(servidores):

            self.tbl_Servers.setItem(
                fila, 0, QTableWidgetItem(str(servidor.rack))
            )

            self.tbl_Servers.setItem(
                fila, 1, QTableWidgetItem(str(servidor.temperatura))
            )

            self.tbl_Servers.setItem(
                fila, 2, QTableWidgetItem(str(servidor.consumo))
            )

            self.tbl_Servers.setItem(
                fila, 3, QTableWidgetItem(servidor.mensaje_alerta)
            )

    def _abrir_registro(self):
        ventana = RegistroServerDialog(self)

        if ventana.exec():
            self._listar_servidores()