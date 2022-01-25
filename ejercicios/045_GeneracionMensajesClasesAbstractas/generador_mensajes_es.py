from generador_mensajes import GeneradorMensajes
"""
100 - Operación correcta
102 - Operación errónea
103 - Operación cancelada
Otro - Mensaje desconocido
"""
class GeneradorMensajesES(GeneradorMensajes):
    def __init__(self) -> None:
        super().__init__()
        self.mensajes = {100:"Operación Correcta",102:"Operación errónea",103:"Operación cancelada"}
    def obtener_mensaje(self, codigo_mensaje):
        if (codigo_mensaje in self.mensajes):
            return self.mensajes[codigo_mensaje]
        else:
            return("Mensaje desconocido")