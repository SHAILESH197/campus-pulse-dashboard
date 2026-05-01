import pandas as pd
import random
from datetime import datetime, timedelta

# options
years = ["1st", "2nd", "3rd", "4th"]
majors = ["CSE", "IT", "ECE", "ME", "CE"]
facilities = ["Library", "Cafeteria", "Sports"]

data = []

for i in range(1, 501):  # 500 rows
    student_id = i
    academic_year = random.choice(years)
    major = random.choice(majors)
    facility = random.choice(facilities)
    score = random.randint(1, 5)

    # random date
    start_date = datetime(2023, 1, 1)
    random_days = random.randint(0, 365)
    timestamp = start_date + timedelta(days=random_days)

    data.append([student_id, academic_year, major, facility, score, timestamp])

df = pd.DataFrame(data, columns=[
    "student_id",
    "academic_year",
    "major",
    "facility_rated",
    "satisfaction_score",
    "timestamp"
])

# save file
df.to_csv("data/student_satisfaction.csv", index=False)

print("Dataset Created Successfully ")