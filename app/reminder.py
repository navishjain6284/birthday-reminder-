from datetime import datetime
from app.database import get_connection
from app.messenger import send_whatsapp

def check_birthdays():

    # Get today's month and day
    today = datetime.today().strftime('%m-%d')

    conn = get_connection()
    cursor = conn.cursor()

    # Query to find birthdays today
    cursor.execute("""
        SELECT name, phone
        FROM contact
        WHERE TO_CHAR(birthday, 'MM-DD') = %s
    """, (today,))

    contacts = cursor.fetchall()

    if contacts:
        for name, phone in contacts:

            message = f"Happy Birthday {name}! 🎉 Hope you have a wonderful day."

            send_whatsapp(phone, message)

            print(f"Birthday message sent to {name}")

    else:
        print("No birthdays today.")

    cursor.close()
    conn.close()