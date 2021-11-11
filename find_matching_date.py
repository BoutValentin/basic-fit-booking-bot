import datetime
from constant import DATE_FORMAT, O_DATE_FORMAT

def create_tomorrow(wanted_hour):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    wanted_hour_split = wanted_hour.split('h')
    wanted_hour_f = wanted_hour_split[0] + ":" + wanted_hour_split[1] + ":00.000"
    tomorrow_date_hour = datetime.datetime.strptime(tomorrow.strftime(O_DATE_FORMAT) + "T" + wanted_hour_f, DATE_FORMAT)
    tomorrow_str = tomorrow.strftime(O_DATE_FORMAT)
    
    return (tomorrow, tomorrow_date_hour, tomorrow_str)

def find_matching_date(dts, tomorrow_date_hour):
    matching_date = None
    idx = 0
    len_dts = len(dts)
    while idx < len_dts and datetime.datetime.strptime(dts[idx]['startDateTime'], DATE_FORMAT) < tomorrow_date_hour:
        idx = idx + 1
    
    if idx < len_dts and datetime.datetime.strptime(dts[idx]['startDateTime'], DATE_FORMAT) == tomorrow_date_hour:
        matching_date = dts[idx]

    return matching_date

