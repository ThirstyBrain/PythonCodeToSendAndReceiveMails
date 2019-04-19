import smtplib
import time
import imaplib
import email


ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "demoEmailID@gmail.com" 
FROM_PWD = "<password of from emailID>"
SMTP_SERVER = "imap.gmail.com"

def read_email_from_gmail():

    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        print(id_list[0])
        print(id_list[-1])
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        
        for i in reversed(id_list):
            type, data = mail.fetch(id_list[-1], '(RFC822)' )
            
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                print('From : ' + email_from + '\n')
                print('Subject : ' + email_subject + '\n')

                # email_subject = msg['subject']
			    # #email_from = msg['from']
			    #print('From : ' + email_from + '\n')
			    

    except Exception as e:
        print ("ex"+e)

read_email_from_gmail()
