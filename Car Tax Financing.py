import csv
import os
from datetime import datetime
from twilio.rest import Client

with open('NAME.csv') as cars:

    reader = csv.DictReader(cars)

    expiring_cars = []

    for row in reader:
        expiry = datetime.strptime(row['tax end'], '%d/%m/%y').date()
        today = datetime.today().date()
        days_remaining = (expiry - today).days


        if days_remaining == 7:
            expiring_cars.append(row)

    num_expiring = len(expiring_cars)

    lines = []
    lines.append("\n The following cars will expire in 7 days: \n ")

    for car in expiring_cars:
        lines.append(f" {car['make']} {car['model']}")

print("\n".join(lines))

client = Client('TWILIO_ACCOUNT_SID', '"TWILIO_AUTH_TOKEN"')

message_body = "\n".join(lines)

message = client.messages.create(
    body=message_body,
    from_="+XXXXXXXXXXX",
    to="+XXXXXXXXXXX"
)





