def timeConversion(s):
    am_pm = s[-2:]

    if s[:2] == "12":
        if am_pm == "PM":
            new_time = s[:-2]
        elif am_pm == "AM":
            new_time = "00" + s[2:-2]
    else:
        if am_pm == "PM":
            s_hour = int(s[:2]) + 12
            new_time = str(s_hour) + s[2:-2]
        elif am_pm == "AM":
            new_time = s[:-2]

    return new_time
