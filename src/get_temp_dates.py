from datetime import datetime
def get_tmax_tmin_dates(reader, header_row):
    
    highs = []
    dates = []
    lows = []
    tmax = 0
    tmin = 0
    date_index = 0
    header_index = 0
    for header in header_row:
        if header == 'TMAX':
            tmax = header_index
        if header == 'TMIN':
            tmin = header_index
        if header == 'DATE':
            date_index = header_index
        header_index = header_index +1

    for row in reader:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        dates.append(date)

        try:
            high = int(row[tmax])
            highs.append(high)
        except:
            print(f"invalid high value for {date}")
            high = 0
            highs.append(high)
        try:
            low = int(row[tmin])
            lows.append(low)
        except:
            print(f"invalid low value for {date}")
            low = 0
            lows.append(low)

    return [highs, lows, dates]