import os
import pandas as pd

file_name_check = r"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\BEFORE"
file_name_list = os.listdir(file_name_check)

for file_name in file_name_list:
    date = file_name[0:8]
    read_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\BEFORE\{file_name}", sep="\t", encoding="utf-16")
    read_data[["ROUTE_NAME"]] = read_data[["ROUTE_NAME"]] + "번"
    read_data.insert(0, "DATE", date)
    file_name = file_name.replace(".TXT", "")

    if "KJ" in file_name:
        read_data.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\ATFER\KJ\{file_name}.csv", encoding="euc-kr")
        print(f"{file_name} → \\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\ATFER\KJ_{file_name}")

    elif "YN" in file_name:
        read_data.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\ATFER\YN\{file_name}.csv", encoding="euc-kr")
        print(f"{file_name} → \\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\ATFER\YN_{file_name}")

    elif "JB" in file_name:
        read_data.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\ATFER\JB\{file_name}.csv", encoding="euc-kr")
        print(f"{file_name} → \\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\ATFER\JB_{file_name}")

    os.remove(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\EB_ROUTE_USER_SCORE\BEFORE\{file_name}.TXT")
    
print(f"ALL_COMPLETE")