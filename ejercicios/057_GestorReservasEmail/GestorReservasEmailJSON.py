import imaplib
import email
import json
from getpass import getpass

def almacenar_reserva(nombre, mesa, dia, hora):
    with open("reservas.txt","a",encoding="UTF-8") as fichero:
        fichero.write(f"{nombre} ha reservado la mesa {mesa} el día {dia} a las {hora}\n")

def procesar_reserva(asunto, texto_mensaje):
    if (asunto=="RESERVA"):
        #{"Nombre":"Fernando Paniagua","Reserva":"5","Fecha":"02/03/2022","Hora":"21:15"}
        reserva_json = json.loads(texto_mensaje)
        nombre = reserva_json["Nombre"]
        mesa = reserva_json["Reserva"]
        dia = reserva_json["Fecha"]
        hora = reserva_json["Hora"]
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