# PYTHON EMAIL SENDING
import email.message
msg = email.message.EmailMessage()
msg["From"] = "tuj0419@gapp.nthu.edu.tw"
msg["To"] = "tuj0419@gmail.com"
msg["Subject"] = "Hello, Jason Tu"
password = ""

# pure text sending
msg.set_content("Dear Jason,\n \
\n \
\n \
Best Regards,\n \
Alice \
\n")

# SMTP lib sending mails
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(msg["From"], password)
server.send_message(msg)
server.close()
