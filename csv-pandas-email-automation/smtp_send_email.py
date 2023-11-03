"""send email by smtp"""
import smtplib
import email.message


def send_email():
    body = """
    <p> Paragraph <b>1</> </p>
    <p> Paragraph 2 </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['FROM'] = "remetente"
    msg['TO'] = "destinatario"
    password = 'password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()

    # Credentials
    smtp.login(msg['FROM'], password)
    smtp.sendmail(msg['FROM'], [msg['To']], msg.as_string().encode('utf-8'))

    print('Email Sent')
