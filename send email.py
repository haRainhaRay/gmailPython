import smtplib

#change the following 3 lines for your case.
fromEmail='YOUR_EMAIL@gmail.com'
emailPass='YOUR GENERATED APP PASSWORD' 
toEmail='TO_EMAIL@gmail.com'

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #instead of only SMTP used in firstemail code, here SMTP_SSL is used, port name is also changed
    smtp.login(fromEmail,emailPass)

    subject='This email has been sent using Python'
    body="Don't you find it fascinating that this email has been sent using Python after gmail revised its less secure app policy? Now logging is done using the app password and not the account password."

    msg=f'Subject:{subject}\n\n{body}' #this is for both subject and body. This is using f strings
    #msg='Hey, lets go out some day' #this sendS only the body and no subject
    #msg='Subject:hey bro this is subject2 \n\n This is the body of a dinosaur'#you may use this for both subject and body if you dont understand f strings
    smtp.sendmail(fromEmail,toEmail,msg) 