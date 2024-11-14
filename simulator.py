import pandas as pd
import random
from datetime import datetime, timedelta

# Get the number of rows to generate from the user
num_records = int(input("Enter the number of records to generate: "))

# Define the possible values for each column
ids = ["amy", "andy", "ben", "chris", "david"]
media_types = ["AU", "VD", "IM"]
languages = ["English", "Spanish", "French"]
interpreter = ["sp28", "sp29", "sp30", "sp31"]
line = ["1101", "1102", "1103"]
minutes_range = (5, 60)  # Range for "minute" column

# Generate random data
data = []
start_time = datetime(2024, 9, 1, 1, 0)  # Base start date for timestamp

for _ in range(num_records):
    record = {
        "id": random.choice(ids),
        "timestamp": (start_time + timedelta(minutes=random.randint(0, 500))).strftime("%m/%d/%Y %H:%M"),
        "media": random.choice(media_types),
        "language": random.choice(languages),
        "interpreter": random.choice(interpreter),
        "line": random.choice(line),
        "minutes": random.randint(*minutes_range),
    }
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("output.csv", index=False)

print("Dataset generated and saved as output.csv")
