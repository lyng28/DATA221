# Time conversion function

def convert_seconds_since_midnight(seconds_since_midnight):
    if type(seconds_since_midnight) != int:
        return "Invalid input, seconds must be an integer"
    if seconds_since_midnight < 0 or seconds_since_midnight >= 24 * 60 * 60:
        return "Invalid input, seconds must be between 0 and 86,399"

    hours = seconds_since_midnight // 3600
    minutes = (seconds_since_midnight % 3600) // 60
    seconds = seconds_since_midnight % 60

    if hours < 12:
        AMorPM = "AM"
    else:
        AMorPM = "PM"

    hours_in_12hours_clock = hours % 12
    if hours_in_12hours_clock == 0:
        hours_in_12hours_clock = 12

    return(f"{hours_in_12hours_clock} {minutes} {seconds} {AMorPM}")

print(convert_seconds_since_midnight(23489))
print(convert_seconds_since_midnight(86399))
print(convert_seconds_since_midnight(82928))
print(convert_seconds_since_midnight(82400))


