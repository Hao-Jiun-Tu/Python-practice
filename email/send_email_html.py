# PYTHON EMAIL SENDING
import email.message
msg = email.message.EmailMessage()
msg["From"] = "tuj0419@gapp.nthu.edu.tw"
msg["To"] = "tuj0419@gmail.com"
msg["Subject"] = "Hello, Jason Tu"
password = ""

# html format sending
msg.add_alternative("<h3>Dear Jason,</h3> \
It's been a long time since we last met!<br> \
...<br> \
...<br> \
<h3>Best Regards,<br> \
Alice</h3> \
\n", subtype = "html")

# SMTP lib sending mails
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(msg["From"], password)
server.send_message(msg)
server.close()
