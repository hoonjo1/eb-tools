import pandas
from datetime import datetime

def date_range_f(start, end):
    start = datetime.strptime(start, "%Y%m%d")
    end = datetime.strptime(end, "%Y%m%d")
    dates = [date.strftime("%Y%m%d") for date in pandas.date_range(start, periods=(end-start).days+1)]
    return dates
