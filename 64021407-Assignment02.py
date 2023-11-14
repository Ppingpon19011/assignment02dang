import json
from urllib.request import urlopen

obj = json.load(urlopen('http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16'))

available_params = obj["stations"][0]["params"]

print("Available Parameters: " + ", ".join(available_params))
selected_params_input = input("Enter the parameters you want to display (comma-separated): ").split(',')

selected_params = [param.strip().upper() for param in selected_params_input if param.strip().upper() in map(str.upper, available_params)]

start_datetime = input("Enter the start date and time (YYYY-MM-DD HH:MM): ")
end_datetime = input("Enter the end date and time (YYYY-MM-DD HH:MM): ")

if selected_params:
    print("Selected Parameters: " + ", ".join(selected_params))
    print("Time Range: {} to {}".format(start_datetime, end_datetime))
    
    print("\nStation ID: " + obj["stations"][0]["stationID"])
    print("Data Table:")
    header = ["TIME"] + selected_params
    print(" ".join(header))

    for entry in obj["stations"][0]["data"]:
        entry_datetime = entry["DATETIMEDATA"]
        if start_datetime <= entry_datetime <= end_datetime:
            row = [entry_datetime]
            for param in selected_params:
                row.append(entry[param])
            print(" ".join(map(str, row)))
else:
    print("Invalid parameters selected or no parameters selected.")
