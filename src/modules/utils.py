from datetime import date

def get_current_date() -> str:
    return date.today().strftime("%d.%m.%Y")
