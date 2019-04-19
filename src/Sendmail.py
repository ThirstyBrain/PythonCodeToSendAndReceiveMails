import smtplib

gmail_user = '<From email ID >'  
gmail_password = "<From password>"

sent_from = gmail_user  
# to = ['<emailID1>', '<emailID2>']
to = ['<EmailID>']  
subject = 'OMG Super Important Message'  
body = "Hey, what's up?\n\n- This mail is through python code !!! :)"


email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:  
    print('Something went wrong...')
