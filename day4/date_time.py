from datetime import datetime, timedelta

# Get current datetime
now = datetime.now()
print(now)

# Create a datetime for a specific date and time
date = datetime(2023, 2, 1, 12, 0)
print(date)

# Calculate the differnce between the two datetimes
delta = now - date
print(delta)