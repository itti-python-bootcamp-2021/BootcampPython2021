"""
Paso 1: Comprueba que IMAP esté activado
1.Abre Gmail en el ordenador.
2. Arriba a la derecha, haz clic en Configuración. Ver todos los ajustes.
3. Haz clic en la pestaña Reenvío y correo POP/IMAP.
4. En el apartado "Acceso IMAP", selecciona Habilitar IMAP.
5. Haz clic en Guardar cambios.
"""

import imaplib
import email
from getpass import getpass

def almacenar_reserva(nombre, mesa, dia, hora):
    with open("reservas.txt","a",encoding="UTF-8") as fichero:
        fichero.write(f"{nombre} ha reservado la mesa {mesa} el día {dia} a las {hora}\n")

def procesar_reserva(asunto, texto_mensaje):
    if (asunto=="RESERVA"):
        #['Nombre:Juan Luis\r', 'Reserva:12\r', 'Dia:28/02/2022\r', 'Hora:22:05\r', '']
        info_reserva = texto_mensaje.split("\n")[:-1]
        nombre = info_reserva[0].split(":")[1][:-1]
        mesa = info_reserva[1].split(":")[1][:-1]
        dia = info_reserva[2].split(":")[1][:-1]
        hora = info_reserva[3].split(":")[1]+":"+info_reserva[3].split(":")[2][:-1]
        almacenar_reserva(nombre,mesa,dia,hora)
    else:
        print("El mensaje no es una reserva")

IMAP_SERVER = "imap.gmail.com"
EMAIL_FOLDER = 'INBOX'
username = input("Dirección de e-mail:")
password = getpass("Contraseña del emisor:")
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(username, password)
mail.select(EMAIL_FOLDER)
_, selected_mails = mail.search(None, '(UNSEEN)') #Mensajes no leidos
mails = selected_mails[0].split()#En mails están todos los mensajes devueltos por search
print(f"Hay {len(mails)} mensajes la carpeta {EMAIL_FOLDER}")
for bytes_mail in mails:
    _, data = mail.fetch(bytes_mail , '(RFC822)')#Sólo el texto del mensaje.
    _, bytes_data = data[0]
    email_message = email.message_from_bytes(bytes_data)
    asunto = email_message["subject"]
    for part in email_message.walk():
        if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
            message = part.get_payload(decode=True)
            texto_mensaje = message.decode()
            break
    procesar_reserva(asunto, texto_mensaje)

mail.close()
mail.logout()