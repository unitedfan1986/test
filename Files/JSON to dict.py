import json
import csv

user_records = json.load(open("sample.json"))

with open('users_data_for_marketing.csv', "w+", newline='') as file:

    writer = csv.writer(file, delimiter=":")

    writer.writerow(['name', "age", "gender", "email", "balance"])

    for record in user_records:
        writer.writerow([(record["name"],record["age"], record["gender"], record["email"], record["balance"])])

