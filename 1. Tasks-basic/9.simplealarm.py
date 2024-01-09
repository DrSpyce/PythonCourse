import time

try:
    user_input = input("Set a time (HH:MM:SS format): ")
    user_time = time.strptime(user_input, "%H:%M:%S")
except ValueError:
    print("Invalid time format. Please use the HH:MM:SS format.")
    exit()

user_seconds = user_time.tm_hour * 3600 + user_time.tm_min * 60 + user_time.tm_sec

time.sleep(user_seconds)

print("It's time! Your specified time has been reached.")