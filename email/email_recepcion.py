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

#GLOBAL SETTINGS
IMAP_SERVER = "imap.gmail.com"
EMAIL_FOLDER = 'INBOX'

#GET MESSAGE INFO
username = input("Dirección de e-mail:")
password = getpass("Contraseña del emisor:")

#CONNECTION
mail = imaplib.IMAP4_SSL(IMAP_SERVER)

#VALIDATE CREDENTIALS
mail.login(username, password)

#READ FOLDERS
email_folders = mail.list() #Devuelve una lista con las carpetas o buzones

#SELECT INBOX
mail.select(EMAIL_FOLDER)
#READ EMAILS
"""
mail.search devuelve una tupla.
x, y, ... = tupla --> Unpack de un tupla
_, selected_mails = ... > En el  
"""
#_, selected_mails = mail.search(None, '(ALL)') #Todos los mensajes
_, selected_mails = mail.search(None, '(UNSEEN)') #Mensajes no leidos
mails = selected_mails[0].split()#En mails están todos los mensajes devueltos por search
print(f"Hay {len(mails)} mensajes la carpeta {EMAIL_FOLDER}")
for bytes_mail in mails:
    #Obtención de los datos del correo"
    _, data = mail.fetch(bytes_mail , '(RFC822)')#Sólo el texto del mensaje.
    #_, data = mail.fetch(bytes_mail , '(UID BODY[TEXT])')#El código HTML sin tratar
    _, bytes_data = data[0]
    #Obtención del mensaje a partir de sus bytes
    email_message = email.message_from_bytes(bytes_data)
    #Presentación del mensaje
    print("\n********************************************")
    print("Emisor: ",email_message["from"])
    print("Receptor:", email_message["to"])
    print("Asunto: ",email_message["subject"])
    print("Fecha: ",email_message["date"])
    for part in email_message.walk():
        if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
            message = part.get_payload(decode=True)
            print("Mensaje: \n", message.decode())
            print("********************************************\n")
            break

#CLOSE AND LOGOUT
mail.close()
mail.logout()