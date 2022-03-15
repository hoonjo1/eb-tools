import pandas as pd

route_id = "GGB233000031"
city_code = "31010"
service_key = "%2BdWKtitGklFO91lyLm1Z55YZ%2BmabwFFxveAzj89w016h7KJKucPHw381iYBYgvuw3P%2FgrJVuEJRW7id87mnjAA%3D%3D"
url = f"http://apis.data.go.kr/1613000/BusLcInfoInqireService/getRouteAcctoBusLcList?serviceKey={service_key}&pageNo=1&numOfRows=30&_type=xml&cityCode={city_code}&routeId={route_id}"
result = pd.read_xml(url, xpath=".//item")

gpslati = result["gpslati"].map(str)
gpslong = result["gpslong"].map(str)
location = "http://www.google.com/maps/search/" + gpslati + "+" + gpslong
result.insert(3, "location", location)
# result.to_csv("test.csv", encoding="euc-kr")



api_test = result[["gpslati", "gpslong", "nodeord", "vehicleno"]]
api_test.insert(2, "latlng", gpslati + "," + gpslong)

print(result)