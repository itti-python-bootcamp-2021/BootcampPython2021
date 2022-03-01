import json
import smtplib, ssl
from email.mime.text import MIMEText

from getpass import getpass

#GLOBAL SETTINGS
SMTP_SERVER = "smtp.gmail.com"
PORT = 465
context = ssl.create_default_context()
CONFIG_FILE="email_config.json"

#LOAD STORED DATA
try:
    with open(CONFIG_FILE, "r", encoding="UTF-8") as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("Aviso:No existe fichero de configuracion")
    config={"FROM":"","TO":"","SUBJECT":""}

#GET MESSAGE INFO
from_email = input(f"Dirección del emisor[{config['FROM']}]:")
if from_email=="": from_email=config["FROM"]
password = getpass("Contraseña del emisor:")
to_email = input(f"Dirección del destinatario[{config['TO']}]:")
if to_email=="": to_email=config["TO"]
cc_email = input("CC:")
subject = input(f"Asunto[{config['SUBJECT']}]:")
if subject=="": subject=config['SUBJECT']
msg_txt = input("Texto del mensaje:")

#STORE DATA
with open(CONFIG_FILE, "w", encoding="UTF-8") as config_file:
    config_dict = {"FROM":from_email,"TO":to_email,"SUBJECT":subject}
    config_file.write(json.dumps(config_dict))

#CREATE MESSAGE
message = MIMEText(msg_txt)
message['Subject'] = subject
message['From'] = from_email
message['To'] = to_email
message['CC'] = cc_email
to_email = [to_email]+[cc_email]

#SEND MESSAGE
with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
    print("Validando credenciales...")
    server.login(from_email, password)
    print("Credenciales aceptadas.")
    print("Enviando mensaje...")
    #server.send_message(msg=message, from_addr=from_email, to_addrs=to_email) 
    server.send_message(msg=message, to_addrs=to_email) #from_addr no es obligatorio ni sirve para nada
    print("Mensaje enviado.")