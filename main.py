import pandas as pd

file_name = "British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx"
data = pd.read_excel(file_name)

# Long flights
long_flights = data[data["HAUL"] == "LONG"]

# Short flights
short_flights = data[data["HAUL"] == "SHORT"]

# Morning, Lunchtime, Afternoon, and Evening!

# Long flights
long_flights_Morning = long_flights[long_flights["TIME_OF_DAY"] == "Morning"]
long_flights_Lunchtime = long_flights[long_flights["TIME_OF_DAY"] == "Lunchtime"]
long_flights_Afternoon = long_flights[long_flights["TIME_OF_DAY"] == "Afternoon"]
long_flights_Evening = long_flights[long_flights["TIME_OF_DAY"] == "Evening"]

# Short flights
short_flights_Morning = short_flights[short_flights["TIME_OF_DAY"] == "Morning"]
short_flights_Lunchtime = short_flights[short_flights["TIME_OF_DAY"] == "Lunchtime"]
short_flights_Afternoon = short_flights[short_flights["TIME_OF_DAY"] == "Afternoon"]
short_flights_Evening = short_flights[short_flights["TIME_OF_DAY"] == "Evening"]

subgroups = [
    ("LONG", "Morning", long_flights_Morning),
    ("LONG", "Lunchtime", long_flights_Lunchtime),
    ("LONG", "Afternoon", long_flights_Afternoon),
    ("LONG", "Evening", long_flights_Evening),
    ("SHORT", "Morning", short_flights_Morning),
    ("SHORT", "Lunchtime", short_flights_Lunchtime),
    ("SHORT", "Afternoon", short_flights_Afternoon),
    ("SHORT", "Evening", short_flights_Evening),
]
row_list = []

for how_long, time_flight, subgroup in subgroups:
    t1_pax = subgroup["TIER1_ELIGIBLE_PAX"].sum()
    t2_pax = subgroup["TIER2_ELIGIBLE_PAX"].sum()
    t3_pax = subgroup["TIER3_ELIGIBLE_PAX"].sum()

    total_pax = (
            subgroup["FIRST_CLASS_SEATS"].sum() +
            subgroup["BUSINESS_CLASS_SEATS"].sum() +
            subgroup["ECONOMY_SEATS"].sum()
    )

    t1_pct = round((t1_pax / total_pax) * 100, 1) if total_pax > 0 else 0.0
    t2_pct = round((t2_pax / total_pax) * 100, 1) if total_pax > 0 else 0.0
    t3_pct = round((t3_pax / total_pax) * 100, 1) if total_pax > 0 else 0.0

    row = {
        "HAUL": how_long,
        "TIME_OF_DAY": time_flight,
        "Tier_1_%": f"{t1_pct}%",
        "Tier_2_%": f"{t2_pct}%",
        "Tier_3_%": f"{t3_pct}%"
    }
    row_list.append(row)

final_table = pd.DataFrame(row_list)
final_table.to_excel("final_lounge_eligibility.xlsx", index=False)
