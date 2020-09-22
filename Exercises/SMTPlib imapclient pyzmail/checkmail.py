import imapclient
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('mazzalaialan@gmail.com','password')
conn.list_folders()
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2020'])
UIDs = conn.search(['BEFORE 20-Aug-2020'])
UIDs = conn.search(['ON 20-Aug-2020'])
UIDs = conn.search(['ALL'])
UIDs = conn.search(['SUBJECT "hola mundo"'])
UIDs = conn.search(['BODY "hola mundo"'])
UIDs = conn.search(['TEXT "hola mundo"'])
rawMessage = conn.fetch([47474],['BODY[]'],['FLAGS'])
import pyzmail
Message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
Message.get_subject()
Message.get_addresses('from')
Message.get_addresses('to')
Message.get_addresses('bcc')
Message.text_part
Message.html_part
Message.text_part.get_payload().decode('UTF-8')
Message.text_part.charset
conn.delete_messages([47474])
conn.logout