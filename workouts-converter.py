"""Converts a CSV to JSON format for workouts. Adds week number and date from race date"""
import csv
import argparse
import json
from datetime import timedelta, datetime


def convert(input_csv, output_json, race_date):
    print("Converting {} to {} for race on {}".format(input_csv, output_json, race_date))

    days = []

    race = datetime.strptime(race_date, "%Y-%m-%d")
    weeks_30 = timedelta(weeks=30, days=-1)
    start = race - weeks_30
    print(start)

    with open(input_csv) as input:
        reader = csv.DictReader(input)
        for i, line in enumerate(reader):
            day_date = start + timedelta(days=i)
            day = create_day(day_date, line)
            days.append(day)

    weeks = create_weeks(days)
    with open(output_json, "w") as output:
        json.dump(weeks, output, sort_keys=True, indent=4)

    return weeks


def create_weeks(days):
    weeks = []
    for i in range(0, int(len(days) / 7)):
        week_days = days[i * 7:i * 7 + 7]
        week = {
            "num": i + 1,
            "days": week_days
        }
        weeks.append(week)
    return weeks


SWIM_FIELDS = {"Swim": "num", "Swim Notes": "note"}
BIKE_FIELDS = {"Bike Duration": "min", "Bike Zone": "zone", "Bike Notes": "note"}
RUN_FIELDS = {"Run Duration": "min", "Run Zone": "zone", "Run Notes": "note"}


def create_day(date, values):
    try:

        day = {
            "date": date.strftime("%Y-%m-%d"),
        }

        add_sport(day, "swim", SWIM_FIELDS, values)
        add_sport(day, "bike", BIKE_FIELDS, values)
        add_sport(day, "run", RUN_FIELDS, values)

        return day
    except Exception as e:
        print(e.with_traceback())
        print(values)


def add_sport(day, name, fields, values):
    sport = {json_key: values[csv_key] for (csv_key, json_key) in fields.items() if values[csv_key]}
    if sport:
        day[name] = sport


def parse_mins(mins):
    if mins:
        values = mins.split(":")
        return int(values[0]) * 60 + int(values[1])
    else:
        return 0


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", help="The input CSV file")
    parser.add_argument("output_json", help="The output JSON file")
    parser.add_argument("race_date", help="The date of the race on Sunday in YYYY-MM-DD")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    workouts = convert(args.input_csv, args.output_json, args.race_date)
    print(workouts)
