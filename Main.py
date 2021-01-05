import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from smtplib import SMTP
import os
from io import open
import urllib.request
from getpass import getuser
import platform
import sys
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def arranque():
    os.system("title AnonymousEmail Service")
    os.system("Color 0f")
    print("                                             AnonymousEmail")
    print("                                       Servicio de correos anonimos")
    CorreoDesti = input("Correo electronico del destinatario: ")
    print("Si no esta el servidor al que quieres mandar selecciona gmail")
    ServidorDesti = input("Coloque el tipo de correo, solo hay 3 servidores disponibles (Yahoo, Gmail, Live): ")
    CorreoAsunto = input("Asunto del correo (Titulo): ")
    CorreoContenido = input("Contenido del correo (Mensaje): ")

    mensaje = MIMEMultipart("plain")
    mensaje["From"] = "anonymousemailsservices@gmail.com"
    mensaje["To"] = CorreoDesti
    mensaje["Subject"] = "Correo enviado con AnonymousEmail: "+CorreoAsunto
    mensaje.attach(MIMEText(CorreoContenido, 'plain'))
    if ServidorDesti == 'Gmail':
        servidorsmtp = "smtp.gmail.com"
    elif ServidorDesti == 'gmail':
        servidorsmtp = "smtp.gmail.com"
    elif ServidorDesti == 'Live':
        servidorsmtp = "smtp.live.com"
    elif ServidorDesti == 'live':
        servidorsmtp = "smtp.live.com"
    elif ServidorDesti == 'Outlook':
        servidorsmtp = "smtp.live.com"
    elif ServidorDesti == 'outlook':
        servidorsmtp = "smtp.live.com"
    elif ServidorDesti == 'Yahoo':
        servidorsmtp = "smtp.yahoo.com"
    elif ServidorDesti == 'yahoo':
        servidorsmtp = "smtp.yahoo.com"
    smtp = SMTP(servidorsmtp, 587)
    # smtp.live.com for outlook accounts
    # smtp.gmail.com for google accounts
    # smtp.yahoo.com for yahoo accounts
    smtp.starttls()
    smtp.login("anonymousemailsservices@gmail.com", "Pinoto08")
    smtp.sendmail("anonymousemailsservices@gmail.com",mensaje["To"], mensaje.as_string())
    smtp.quit()
    clear()
    print("El correo se envio correctamente")
    print("La aplicacion se reiniciara en 5 segundos!")
    time.sleep(5)
    clear()
    arranque()
arranque()