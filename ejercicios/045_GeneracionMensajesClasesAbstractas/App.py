from FactoryGeneradoresMensaje import GeneradorMensajesFactory
from generador_mensajes import GeneradorMensajes

gm = GeneradorMensajesFactory().get_generador_mensajes()
if isinstance(gm, GeneradorMensajes):
    print(gm.obtener_mensaje(100))
else:
    print("Error.")