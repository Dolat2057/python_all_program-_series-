import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_add = 'dolurathore18@gmail.com'
to_add = ['dolatrathore18@gmail.com','pawan95251@gmail.com','rk3225741@gmail.com']
msg = MIMEMultipart()
msg['from'] = from_add
msg['To'] = " ,".join(to_add)
msg['subject']='just to check'
body = 'hello world'
msg.attach(MIMEText(body,'plain'))

email= " dolurathore18@gmail.com"
password = " uzumymw12345"

mail= smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text= msg.as_string()
mail.sendmail(from_add,to_add,text)
mail.quit()
