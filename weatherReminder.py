import schedule
import smtplib
import requests
import re
from bs4 import BeautifulSoup

def weatherReminder():
    city = input('Enter your City: ')
    url = "https://www.google.com/search?q=" + "weather" + city
    html = requests.get(url).content
    
    #getting Raw Data
    
    soup = BeautifulSoup(html, 'html.parser')
    
    with open("weather.html","w",encoding='utf-8') as file:
        file.write(str(soup.prettify()))

    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    #formatting Data
    report_temp = temperature.split()[0]
    report_data = sky.split()[3]

    smtp_object = smtplib.SMTP('smtp.gmail.com',587)
        
        #start TLS for security
    smtp_object.starttls()
        
        #Authentication
    smtp_object.login("YOUR Email", "Password")
    subject = "Today's Weather Reminder"
    body = f"Hi Your Today's Weather Reminder\n weather condition for today is {report_data} and temprature {report_temp} in {city}."
    msg = f"Subject: {subject}\n\n{body}\n\nRegards,\n\nWeatherReminderSystem".encode('utf-8')
        
        #Sending the email
    smtp_object.sendmail("From Email","To Email",msg)
        
        #terminate the session
    smtp_object.quit()
    print('Email Sent')
        
#Schedule Your email daily at 8:00 A.M.
schedule.every().day.at("08:00").do(weatherReminder)
while(True):
    schedule.run_pending()  
