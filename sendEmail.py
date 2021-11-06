import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart # para crear cabeza de mensaje
from email.mime.text import MIMEText # para que el mensaje sea tipo HTML

from email.mime.base import MIMEBase # para adjuntar archivos
from email import encoders # para codificar archivos

print (" enviar Email con Gmail")
user = input("Introduce tu email: ")
password = getpass.getpass("Introduce tu contraseña: ")

remitente = input("Introduce el email del remitente: ")
destinatario = input("Introduce el email del destinatario: ")
asunto = input("Introduce el asunto del email: ")
mensaje = input("Introduce el mensaje del email: ")
archivo = input("Introduce el nombre del archivo a enviar: ")

gmail = smtplib.SMTP('smtp.gmail.com', 587)

gmail.starttls()    
gmail.login(user, password)
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

mensaje = MIMEText(mensaje, 'html') # para que el mensaje sea tipo HTML
header.attach(mensaje)

if(os.path.isfile(archivo)):
    adjunto = MIMEBase('application', 'octet-stream')
    adjunto.set_payload(open((archivo, 'rb')).read())
    encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(archivo))
    header.attach(adjunto)

gmail.sendmail(remitente, destinatario, header.as_string())
gmail.quit()