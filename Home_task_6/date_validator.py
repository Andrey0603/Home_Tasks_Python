def _is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def is_valid_date(date_str):


    if len(date_str) != 10:
        return False

    parts = date_str.split('.')

    if len(parts) != 3:
        return False

    try:
        day, month, year = map(int, parts)
    except ValueError:
        return False

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if _is_leap_year(year) and day > 29:
            return False
        elif not _is_leap_year(year) and day > 28:
            return False

    return True
