from Database.ConexionDb import ConexionBD
from Exeptions.Exeptions import ServerException
from Models.Entities.NodoServidor import NodoServidor

class ServerModel:
    """Capa de Persistencia. Se comunica con MySQL mediante Stored Procedures."""
    
    @staticmethod
    def listar_Servidores():
        """Lee los programas desde MySQL y los devuelve como una lista de objetos."""
        conexion = None
        try:
            conexion = ConexionBD.obtener_conexion()
            # Usamos dictionary=True para poder leer las columnas por su nombre
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_listarServidores')
            
            listar_Servidores = []
            for result in cursor.stored_results():
                for row in result.fetchall():
                    # Mapeo exacto: Columna MySQL -> Atributo Python
                    obj = NodoServidor(
                        rack=row['rack'],
                        temperatura=row['Temperatura'],
                        consumo=row['Consumo'],
                        Mensaje_Alerta=row['Mensaje_alerta'],
                    )
                    listar_Servidores.append(obj)
            return listar_Servidores
            
        except Exception as ex:
            raise ServerException(f"Error al listar programas en BD: {ex}")
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()

    @staticmethod
    def RegistrarServidor(rack: int, temperatura: float,
                      consumo: float, mensaje_alerta: str):
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor()
            parametros = (rack, temperatura, consumo, mensaje_alerta)
            cursor.callproc('sp_RegistrarServidor', parametros)
            conexion.commit()
            return True

        except Exception as error:
            if conexion:
                conexion.rollback()

            raise ServerException(f"Error al registrar servidor: {error}")

        finally:
            if cursor:
                cursor.close()

            if conexion and conexion.is_connected():
                conexion.close()

    @staticmethod
    def Busqueda(Criterio: str):
        conexion = None
        cursor = None
        try:
            conexion = ConexionBD.obtener_conexion()
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_Busqueda_Servers', (Criterio,))
            servidores = []
            for resultado in cursor.stored_results():
                for row in resultado.fetchall():
                    obj = NodoServidor(
                        rack=row['rack'],
                        temperatura=row['Temperatura'],
                        consumo=row['Consumo'],
                        Mensaje_Alerta=row['Mensaje_alerta']
                    )
                    servidores.append(obj)
            return servidores
        except Exception as error:
            raise ServerException(f"Error en búsqueda: {error}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()