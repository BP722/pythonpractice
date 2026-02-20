from datetime import date 
def birthday_countdown():
    today = date.today()
    birthday = date(today.year, 7, 22)
    if birthday < today:
        birthday = date(today.year + 1, 7, 22)
    if birthday == today:
        print("Happy Birthday!")
    else:
        days_until_birthday = (birthday - today).days
        print(f"Your birthday is in {days_until_birthday} days.")
if __name__ == "__main__":
    birthday_countdown()