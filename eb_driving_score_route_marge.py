import pandas as pd
from date_range import date_range_f

company = "KJ"
dates = date_range_f("20220218", "20220218")

result = list()
date_result = list()

for date in dates:
    read_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\ATFER\{company}\{date}_{company}.csv", encoding="euc-kr")
    read_data[["GENL_RIDE_CNT", "STU_RIDE_CNT", "CHILD_RIDE_CNT", "GENL_ALIGHT_CNT", "STU_ALIGHT_CNT", "CHILD_ALIGHT_CNT"]] = read_data[["GENL_RIDE_CNT", "STU_RIDE_CNT", "CHILD_RIDE_CNT", "GENL_ALIGHT_CNT", "STU_ALIGHT_CNT", "CHILD_ALIGHT_CNT"]].apply(pd.to_numeric)

    route_station_data_edit = read_data.groupby(["DATE", "ROUTE_ID", "ROUTE_NAME", "STA_ID", "STATION_NAME"])[["GENL_RIDE_CNT", "STU_RIDE_CNT", "CHILD_RIDE_CNT", "GENL_ALIGHT_CNT", "STU_ALIGHT_CNT", "CHILD_ALIGHT_CNT"]].sum()
    route_station_data_edit.insert(3, "RIDE_USER_SCORE", route_station_data_edit["GENL_RIDE_CNT"] + route_station_data_edit["STU_RIDE_CNT"] + route_station_data_edit["CHILD_RIDE_CNT"])
    route_station_data_edit.insert(7, "ALIGHT_USER_SCORE", route_station_data_edit["GENL_ALIGHT_CNT"] + route_station_data_edit["STU_ALIGHT_CNT"] + route_station_data_edit["CHILD_ALIGHT_CNT"])

    date_result.append(route_station_data_edit)
    result = pd.concat(date_result)

start_date = dates[0]
end_date = dates[-1]
result.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE_EDIT\ROUTE_STATION\{company}\{company}_{start_date}_{end_date}_ROUTE_STATION_SCORE.csv", encoding="euc-kr")