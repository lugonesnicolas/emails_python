from smtplib import SMTP #Importamos smtp
from os import getenv #Esta libreria permite traer las variables de entorno
from typing import List, Optional
from email.mime.multipart import MIMEMultipart #Determina que tipo de contenido vamos a enviar
from email.mime.text import MIMEText #Formateador de texto 

class Email:

    def __init__(self) -> None:
        self.server=SMTP(
            host=getenv('SMTP_HOSTNAME'),#Servidor
            port=getenv('SMTP_TLS_PORT')#Puerto
        )

    """
    El metodo connect_server nos permite conectar con el host de gmail.
    """
    def connect_server(self):
        self.server.starttls() #Inicia la conexion tls
        self.server.login(                  
            user=getenv('SMTP_USER'), #Credencial de entorno
            password=getenv('SMTP_PASSWORD') #Credenciales de entorno
        )

    def send_email(self, emails: List[str],subject: Optional[str], **kwargs):
        self.connect_server()
        print("Sending email")
        for email in emails:
            mime=MIMEMultipart()
            mime['From']=getenv('SMTP_USER')
            mime['Tp']=email
            mime['Subject']=subject
            format=MIMEText(kwargs['message_format'], kwargs['format'])
            mime.attach(format)
            try:
                self.server.sendmail(getenv('SMTP_USER'), email, mime.as_string())
            except Exception as e:
                raise e
            finally:
                self.disconnect_server()

    def disconnect_server(self):
        self.server.quit()
        self.server.close()