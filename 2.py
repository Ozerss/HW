time = int(input("Enter seconds you want formate to hh:mm:ss: "))
hours_count = time // 3600
minutes_count = (time - hours_count * 3600) // 60
seconds_count = time - (hours_count * 3600 + minutes_count * 60)
print(f"Time is {hours_count}:{minutes_count}:{seconds_count}")
