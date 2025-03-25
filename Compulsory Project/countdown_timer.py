# project 7 countdown time
import time
def countdown_timer(seconds):
    while seconds > 0:
      mins,secs = divmod(seconds, 60)#mins secs calculate hu rhe
      time_format ='{:02d}:{:02d}'.format(mins,secs) # Changed 'min' to 'mins' and 'sec' to 'secs'
      print(time_format, end='\r')
      time.sleep(1)
      seconds -= 1
    print("00:00 \n Time's up!")

# Get user input for timer
total_seconds =int(input("Enter countdown time in seconds: "))
countdown_timer(total_seconds)