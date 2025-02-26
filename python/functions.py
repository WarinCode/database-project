def format_date(date, month, year):
    date = "0" + date if len(date) == 1 else date
    month = "0" + month if len(month) == 1 else month
    new_date = year + "-" + month + "-" + date
    return new_date

def format_time(hours, minutes, seconds):
    hours = "0" + hours if len(hours) == 1 else hours
    minutes = "0" + minutes if len(minutes) == 1 else minutes
    new_time = hours + ":" + minutes + ":" + seconds
    return new_time

def format_date_time(year, month, date, hours, minutes, seconds):
    return format_date(date, month, year) + " " + format_time(hours, minutes, seconds)

def get_null(val):
    return "NULL" if str(val).lower().strip() in ('nan', '0.0', '') else val