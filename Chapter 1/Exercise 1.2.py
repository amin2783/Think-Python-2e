minutes = 42
seconds = 42
total_seconds = seconds + (42*60)

print(f'There are {total_seconds} seconds in 42 minutes and 42 seconds')

kilometers = 10
miles = kilometers/1.61

print(f"There are {miles} miles in 10 kilometers")

hours = total_seconds/3600

average_pace_in_minutes = (minutes+(minutes/60))/miles
average_speed = miles/hours

print(f'Average pace in minutes is {average_pace_in_minutes} minutes per mile and average speed is {average_speed} miles per hour.')