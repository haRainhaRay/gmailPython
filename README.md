# gmailPython
send email using python in gmail

1. Account username and password are not accepted by gmail since June 02,2022 in third party apps due to less secure way they use to login to gmail. In our case, we use SMTP to send email.
2. Therefore, we need to create an app password in go account.
3. Login to gmail. CLick dot matrix in top right ie google apps icon. Click account. This will open Google account page.

![step 1](1.jpg?raw=true)

![step 2](2.jpg?raw=true)

4. In the navigation bar in the left, click on security. Scroll to "signing in to Google". Click app password. If you cannot see app password link in options, first set your two step authentication.

![step 3](3.jpg?raw=true)

5. In drop down menu of select app, select mail. In drop down of select device, select custom. Click on generate to generate the app password. Now, instead of using the account password in your python code to send email, use this gernerated app password. Username shall be your email id. 

![step 4](4.jpg?raw=true)

6. To know more about app passwords, click https://support.google.com/accounts/answer/185833?hl=en#zippy=%2Cwhy-you-may-need-an-app-password
