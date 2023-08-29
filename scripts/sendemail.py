import smtplib
import os
#Email Variables
SMTP_SERVER = "smtp.gmail.com" #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = "lab.XPPLUS@gmail.com" #change this to match your gmail account
GMAIL_PASSWORD = "jgvu yjlw vruc jxgb"  #change this to match your gmail app-password
sendTo = "sebainfante186@gmail.com"

path_file="/home/sebastian/Documents/LAB_HEP/red_pitaya/"
file_name="prueba.txt"

f=open(path_file+file_name, 'r')
data = f.readlines()
emailSubject = "reporte semanal"
content_general="Este es un correo automatico desde el sistema de adquicision de datos del detector de lago en la facultad de fisica de la serena con coordenadas longitud sur 29 grados, 54.6 minutos y latitud oeste de 71 grados, 14.4 minutos y  elevacion de 87.2 metros."
content_mond = data[0+0*3] +data[1+0*3] + data[2+0*3]
content_tues = data[0+1*3] +data[1+1*3] + data[2+1*3]
content_wedn = data[0+2*3] +data[1+2*3] + data[2+2*3]
content_thur = data[0+3*3] +data[1+3*3] + data[2+3*3]
content_frid = data[0+4*3] +data[1+4*3] + data[2+4*3]
content_satu = data[0+5*3] +data[1+5*3] + data[2+5*3]
content_sund = data[0+6*3] +data[1+6*3] + data[2+6*3]
emailContent = content_general + "<br> <br>" + content_mond + "<br>" + content_tues + "<br>"+ content_wedn + "<br>" + content_thur + "<br>" + content_frid + "<br>" + content_satu + "<br>" + content_sund + "<br>" 
f.close()
class Emailer:
    def sendmail(self, recipient, subject, content):

        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()


#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
sender.sendmail(sendTo, emailSubject, emailContent)

os.remove(path_file+file_name)
