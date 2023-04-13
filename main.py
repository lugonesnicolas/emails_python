from decouple import config
import smtplib
# from dotenv import load_dotenv
# from os import getenv #Esta libreria permite traer las variables de entorno


HOST=config('SMTP_HOSTNAME')
PORT=config('SMTP_TLS_PORT')
USER=config('SMTP_USER')
PASSWORD=config('SMTP_PASSWORD')
mensaje="Subject: Prueba\nEste es mi mensaje"

def main():
    conexion = smtplib.SMTP(host=HOST, port=PORT)
    conexion.ehlo()
    conexion.starttls()
    conexion.login(user=USER, password=PASSWORD)
    conexion.sendmail(from_addr=USER, to_addrs='lugonesnicolas@gmail.com', msg=mensaje)
    conexion.quit()


if __name__=='__main__':
    main()
