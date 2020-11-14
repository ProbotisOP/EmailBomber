import smtplib
import random , os
import string

os.system("figlet MailSender")
print('                                '"By SATNAM")
small_letters = string.ascii_lowercase
capital_letters = string.ascii_uppercase
# FOR GMAIL
GMAIL_USERNAME = input("Enter your Email")
GMAIL_PASSWORD = input("Enter your PassWord")
GMAIL_RECIPIENT = input("ENTER RECEIVER'S GMAIL ADDRESS: ")
BODY = input('ENTER MESSAGE: ')
ENTER_TIME = int(input("ENTER NUMBER OF SEND: "))
# creates SMTP session
SMTP_MAIL = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
SMTP_MAIL.starttls()
# login with our gmail account
SMTP_MAIL.login(GMAIL_USERNAME, GMAIL_PASSWORD)
for i in range(0, ENTER_TIME):
    email_subject = "".join((random.choice(capital_letters + small_letters)) for i in range(0, 10))
    # message masala
    type_sent = f"from: {GMAIL_USERNAME}\nsubject: {email_subject}\nto: {GMAIL_RECIPIENT}\n"
    result = type_sent + "\n" + BODY
    try:
        SMTP_MAIL.sendmail(GMAIL_USERNAME, GMAIL_RECIPIENT, result)
        print(f"{i}|MAIL HAS BEEN SENT")
    except:
        print(f"TURN ON LESS SECURE APP ACCESS")

SMTP_MAIL.quit()