# write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is 
# expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"

def format_duration(seconds):
    if seconds == 0:
        return "now"
    year = seconds // (365*24*60*60)
    seconds = seconds % (365*24*60*60)
    day = seconds // (24*60*60)
    seconds = seconds % (24*60*60)
    hour = seconds // (60*60)
    seconds = seconds % (60*60)
    minute = seconds // 60
    seconds = seconds % 60
    
    result =[]
    if year >0:
        result.append(str(year)+(" year" if year==1 else " years"))
    if day >0:
        result.append(str(day)+(" day" if day==1 else " days"))
    if hour >0:
        result.append(str(hour)+(" hour" if hour==1 else " hours"))
    if minute >0:
        result.append(str(minute)+(" minute" if minute==1 else " minutes"))
    if seconds >0:
        result.append(str(seconds)+(" second" if seconds==1 else " seconds"))
        
    if len(result)==1:
        return result[0]
    elif len(result)==2:
        return " and ".join(result)
    else:
        return ", ".join(result[:-1])+" and "+ result[-1]