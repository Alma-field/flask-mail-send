import smtplib
from email import message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class gmail():
    def __init__(self, mail_address, password):
        self.EMAIL_ADDRESS = mail_address
        self.EMAIL_PASSWORD = password
        self.loggedin = False

    def __del__(self):
        try:
            self.smtpobj.quit()
        except AttributeError as e:
            pass
        except smtplib.SMTPServerDisconnected as e:
            pass

    def login(self):
        try:
            self.smtpobj.quit()
        except AttributeError as e:
            pass
        except smtplib.SMTPServerDisconnected as e:
            pass
        except BaseException as e:
            return False
        self.smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtpobj.ehlo()
        self.smtpobj.starttls()
        self.smtpobj.ehlo()
        self.smtpobj.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
        self.loggedin = True
        return True

    def create_message(self, to_addr, subject, body):
        msg = message.EmailMessage()
        msg.set_content(body);
        msg['Subject'] = subject
        msg['From'] = self.EMAIL_ADDRESS
        msg['To'] = to_addr
        return msg

    def create_minemulti(self, from_name, to_addr, subject, text, html):
        msg = MIMEMultipart('MailObject')
        msg['Subject'] = subject
        msg['From'] = f'{from_name}<{self.EMAIL_ADDRESS}>'
        msg['To'] = to_addr
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        return msg

    def send(self, to_addr, body_msg):
        try:
            #self.smtpobj.send_message(body_msg)
            self.smtpobj.sendmail(self.EMAIL_ADDRESS, to_addr, body_msg.as_string())
        except (smtplib.SMTPServerDisconnected, AttributeError) as e:
            self.login()
            return self.send(to_addr, body_msg)
        return True

    def send_mail_one(self, from_name, destination, destination_name, subject, text, html):
        mail_obj = self.create_minemulti(from_name=from_name, to_addr=destination_name, subject=subject, text=text, html=html)
        if not self.loggedin and not self.login():
            return False
        self.send(to_addr=destination, body_msg=mail_obj)
        self.smtpobj.quit()
        return True
