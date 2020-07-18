import smtplib

email = ''
password = ''
def send_email() :
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.starttls()
    session.login(email, password)
    message = 'Python mail sending'
    session.sendmail(email, email, message)