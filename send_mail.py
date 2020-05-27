import smtplib
from email.mime.text import MIMEText

def send_mail(customer,dealer,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '238f35944c8102'
    password = 'c91c0736d44246'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Rating: {rating}</li><li>Dealer: {dealer}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'jacob.anderson10@gmail.com'
    reciever_email = 'jacob.anderson10@gmail.com'
    msg = MIMEText(message,'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email,reciever_email,msg.as_string())


