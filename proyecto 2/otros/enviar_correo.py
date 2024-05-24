import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

tabla = """
Nombre JG  JF
─────────────
lol     1   2
lol2    3   4
"""

html = f"""
<html>
    <body>
        <pre>{tabla}</pre>
    </body>
</html>
"""


puerto = 587
servidor_smtp = "smtp.gmail.com"

archivo = open("correo_emisor.txt", "r", newline="\n")
correo_emisor = archivo.readline().rstrip()
contraseña = archivo.readline().rstrip()
print(correo_emisor, contraseña)
archivo.close()

correo_destino = "verdaderamenteesperoqueestecorreonoexista@gmail.com"

email = MIMEMultipart("alternative")
email["Subject"] = "Torneos de bola: tabla de jugadores"
email["From"] = correo_emisor
email["To"] = correo_destino
# email.add_header("Content-Type", "text/html")

email.attach(MIMEText(html, "html", "utf-8"))

smtp = smtplib.SMTP(servidor_smtp, puerto)

smtp.starttls()
smtp.login(correo_emisor, contraseña)
smtp.sendmail(correo_emisor, correo_destino, email.as_string())
smtp.quit()