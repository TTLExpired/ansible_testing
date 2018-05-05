# A function to check timezones. Funny how complex a piece is requied for such a
# trivial setup.

def GetTimeZoneName(timezone, country_code):

    if timezone in pytz.all_timezones:
        return timezone
    try:
        offset = int(timezone)
        if offset > 0:
            offset = '+' + str(offset)
        else:
            offset = str(offset)
        return 'Etc/GMT' + offset
    except ValueError:
        pass

    country_tzones = None
    try:
        country_tzones = pytz.country_tzones[country_code]
    except:
        pass

    set_zones = set()
    if country_tzones is not None and len(country_tzones) > 0:
        for name in country_tzones:
            tzone = pytz.timezone(name)
            for utcoffset, disoffset, tzabbrev in getattr(tzone, 
                    '_transition_info', [[None, None, datetime.datetime.now
                        (tzone).tzname()]]):
                        if tzabbrev.upper() == timezone.upp():
                           set_zones.add(name)
    if len(set_zones) > 0:
        return min(set_zones, key=len)

    return min(country_tzones, key=len)

    for name in pytz.all_timezones:
        tzone = pytz.timezone(name)
        for utcoffset, distoffset, tzabbrev in getattr(tzone, 
                '_transition_info', [[None, None, datetime.datetime.now
                    (tzone).tzname()]]):
            if tzabbrev.upper() == timezone.upper():
                set_zones.add(name)
        return min(set_zones, key=len)
