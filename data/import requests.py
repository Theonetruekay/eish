import requests

def get_municipalities():
    response = requests.get("https://loadshedding.eskom.co.za/LoadShedding/GetMunicipalities/?Id=4")
    return response.json()

def get_suburbs(municipality_id):
    response = requests.get(f"http://loadshedding.eskom.co.za/LoadShedding/GetSurburbData/?pageSize=100&pageNum=1&id={municipality_id}")
    return response.json()

def get_load_shedding_schedule(suburb_id, suburb_total, municipality_total):
    response = requests.get(f"https://loadshedding.eskom.co.za/LoadShedding/GetScheduleM/{suburb_id}/2/9/{suburb_total}")
    schedule_lines = response.text.splitlines()
    schedule = []
    for line in schedule_lines:
        parts = line.split()
        if len(parts) == 4:
            day = parts[0]
            time = f"{parts[1]} - {parts[3]}"
            schedule.append({"day": day, "time": time})
    return schedule

def main():
    municipalities = get_municipalities()
    if municipalities:
        municipality = municipalities[0]
        suburb_id = municipality["Value"]
        suburb_name = municipality["Text"]
        suburb_total = municipality["Tot"]

        suburbs = get_suburbs(suburb_id)
        if suburbs:
            suburb = suburbs[0]
            schedule = get_load_shedding_schedule(suburb["Value"], suburb_total, municipality["Tot"])
            print(f"Load Shedding Schedule for {suburb['Text']}, {suburb_total}:")
            for entry in schedule:
                print(f"{entry['day']} {entry['time']}")
        else:
            print("No suburb data available.")
    else:
        print("No municipality data available.")

if __name__ == "__main__":
    main()
