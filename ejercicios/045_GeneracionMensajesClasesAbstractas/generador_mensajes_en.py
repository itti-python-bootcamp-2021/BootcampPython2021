from generador_mensajes import GeneradorMensajes
"""
100 - Operación correcta
102 - Operación errónea
103 - Operación cancelada
Otro - Mensaje desconocido
"""
class GeneradorMensajesEN(GeneradorMensajes):
    def __init__(self) -> None:
        super().__init__()
        self.mensajes = {100:"Correct operation",102:"Error operation",103:"Operation cancelled"}
    def obtener_mensaje(self, codigo_mensaje):
        if (codigo_mensaje in self.mensajes):
            return self.mensajes[codigo_mensaje]
        else:
            return("Unknown code")
