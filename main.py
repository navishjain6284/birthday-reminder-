import sys
import os
import app.reminder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.reminder import check_birthdays

if __name__ == "__main__":
    check_birthdays()