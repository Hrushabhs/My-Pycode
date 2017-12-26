import smtplib
content="Hello I am Hrushbah sending you message using python script "
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login('hrushabhs@gmail.com','password')
mail.sendmail('hrushabhs@gmail.com','shrushabh97@gmail.com',content)
mail.close()
