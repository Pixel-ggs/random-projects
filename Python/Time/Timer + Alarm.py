import time
import os
import platform
import winsound
import threading

running = True

def input_thread():
    global running
    input("Press \'Enter\' to turn off alarm. ")
    running = False

def loop_thread():
    while running:
        winsound.Beep(3000, 500)
        winsound.Beep(6000, 300)

hours, minutes, seconds = 0, 0, 0

hours_input = int(input("Enter the number of hours: "))
minutes_input = int(input("Enter the number of minutes: "))
seconds_input = int(input("Enter the number of seconds: "))
total_seconds = (hours_input * 3600) + (minutes_input * 60) + seconds_input + 1

for j in range(total_seconds):
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
 
for i in range(total_seconds):
    system = platform.system()
    if system == "Windows":
        os.system("cls")

    if seconds == 0:
        if minutes != 0:
            minutes -= 1
            seconds = 60
    if minutes == 0:
        if hours != 0:
            hours -= 1
            minutes = 60
    seconds -= 1
# was a breakpoint here. who knows if it made a difference but if something breaks add it back and try again. -- insp quote by Asher Payn
    print(f"{hours:02} : {minutes:02} : {seconds:02}")


    time.sleep(1)

print("\nDone! Timer has ended.\n")

t1 = threading.Thread(target=input_thread)
t2 = threading.Thread(target=loop_thread)

t1.start()
t2.start()

t1.join()
t2.join()

system = platform.system()
if system == "Windows":
        os.system("cls")

print("\nAlarm stopped.\n")

