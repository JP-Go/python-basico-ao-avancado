from string import Template
from sender_data import my_mail, my_pass
from datetime import datetime

# Base de um email
from email.mime.multipart import MIMEMultipart
# Conteudo em texto de um email
from email.mime.text import MIMEText
# Conteúdo em imagem
from email.mime.image import MIMEImage

# Lib para enviar conteúdo por servidores smtp
import smtplib

HOJE = datetime.now().strftime('%d/%m/%Y')

with open('./template.html', 'r') as file:
    email_template = Template(file.read())
    html_body = email_template.substitute(nome='João', data=HOJE)

msg = MIMEMultipart()  # Cria uma mensagem de email de tipo multipart
msg['from'] = 'Luiz Otávio Miranda'  # Nome do remetente
msg['to'] = my_mail  # Email do destinatário
msg['subject'] = 'Email de teste'  # Assunto do email

body = MIMEText(html_body, 'html')
msg.attach(body)

with open('./cabin.png', 'rb') as img:
    img = MIMEImage(img.read())  # Send bytes from the image to img var
    msg.attach(img)  # Attaches it to email

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # Manda uma mensagem de hello para o sevidor
    smtp.starttls()  # Inicia uma conexão tls
    smtp.login(user=my_mail, password=my_pass)  # Loga no servidor smtp
    smtp.send_message(msg)  # Envia o email
    print('Email enviado com sucesso')
