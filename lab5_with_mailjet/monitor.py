import time
import os
from mailjet_rest import Client
import psutil

#mail credentials
api_key = os.getenv("MAILJET_API_KEY")
api_secret = os.getenv("MAILJET_SECRET_KEY")
my_email = "fafa.aboagye@amalitech.com"
print(api_key)
print(api_secret)

current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",current_time)

#Defining System thresholds 
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

def send_alert(subject, message):
    """
    jghutgu
    """
    #instantiating mailjet client
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [{
            "From": {
                "Email": my_email,
                "Name": "De-General"
            },
            "To": [
                {
                    "Email": "aboagyefafa12@gmail.com",
                    "Name": "Fafs"
                }
            ], 
            "Subject": subject,
            "HTMLPart": f"<h3>{message}</h3>"

        }
            
        ]
    }

    try:
        result = mailjet.send.create(data=data)
        print(f"Email sent: {result.status_code}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")    

# Check system metrics

cpu_usage = psutil.cpu_percent(interval=1) # print(cpu_usage)

ram_usage = psutil.virtual_memory().percent # print(ram_usage)

disk_usage = psutil.disk_usage('/').percent # print(disk_usage)    

# Create alert message based on threshold breaches
alert_message = ""

if cpu_usage > CPU_THRESHOLD:
    alert_message += f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"

if ram_usage > RAM_THRESHOLD:
    alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"

if disk_usage > DISK_THRESHOLD:
    alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"

# If any threshold is breached, send an email alert

if alert_message:
    send_alert(f"Python Monitoring Alert Alert-{formatted_time}", alert_message)
else:
    print("All system metrics are within normal limits.")    
