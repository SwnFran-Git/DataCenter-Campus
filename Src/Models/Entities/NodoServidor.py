class NodoServidor:

    def __init__(self, rack, temperatura, consumo, Mensaje_Alerta):
        self._rack = rack
        self._temperatura = temperatura
        self._consumo = consumo
        self._mensaje_alerta = Mensaje_Alerta

    @property
    def rack(self):
        return self._rack

    @property
    def temperatura(self):
        return self._temperatura

    @property
    def consumo(self):
        return self._consumo

    @property
    def mensaje_alerta(self):
        return self._mensaje_alerta