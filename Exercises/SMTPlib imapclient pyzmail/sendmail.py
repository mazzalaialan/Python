import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn
conn.ehlo()
conn.starttls()
conn.login('mazzalaialan@gmail.com','password')
conn.sendmail('mazzalaialan@gmail.com','cinthiapardos@gmail.com','Subject: blabla...\n\nbody...')
conn.quit()