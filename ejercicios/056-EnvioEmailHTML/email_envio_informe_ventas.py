import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
message = MIMEMultipart("alternative")#Se proporcionan dos alternativas: texto y html
compras_trimestrales = (("Trimestre 1",15000),("Trimestre 2",18000),("Trimestre 3",8000),("Trimestre 4",21500))
text = msg_txt
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <table style="width:500px">
        <tr style="background-color: rgb(12, 57, 139); color: white;" >
            <th style="padding:10px;">Trimestre</th>
            <th style="padding:10px;">Facturación(€)</th>
        </tr>
"""
contador=0
for compras in compras_trimestrales:
    color1 = "170, 170, 170"
    color2 = "255, 255, 255"
    if contador%2==0:
        color=color1
    else:
        color=color2
    contador+=1
    html=html+f"""
        <tr style="background-color: rgb({color});">
            <td style="padding:10px;">{compras[0]}</td>
            <td style="text-align:right;padding:10px;">{compras[1]}</td>
        </tr>
        """
html=html+"</table></body></html>"

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

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
    server.send_message(msg=message, from_addr=from_email, to_addrs=to_email)
    print("Mensaje enviado.")