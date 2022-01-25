import locale
from generador_mensajes_es import GeneradorMensajesES
from generador_mensajes_en import GeneradorMensajesEN

class GeneradorMensajesFactory:
    @classmethod
    def get_generador_mensajes(self):
        codigo_local = locale.getlocale()[0]
        if (codigo_local=="es_ES"):
            return GeneradorMensajesES()
        else:
            return GeneradorMensajesEN()


