import pywhatkit
from datetime import datetime

def send_whatsapp(phone, message):

    now = datetime.now()

    pywhatkit.sendwhatmsg(
        phone,
        message,
        now.hour,
        now.minute + 1
    )