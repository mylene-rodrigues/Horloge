from tkinter import *
import time
from datetime import datetime   
from playsound import playsound

root = Tk()

root.title("Heure")
root.geometry("1920x1040+0+0")
root.config(bg="black")

def recupereHeure():
    h = str(time.strftime(("%H")))
    m = str(time.strftime(("%M")))
    s = str(time.strftime(("%S")))

    print(h,m,s)


    lbl_heure.config(text=h)
    lbl_minute.config(text=m)
    lbl_seconde.config(text=s)
    lbl_heure.after(200, recupereHeure)


#heure
lbl_heure= Label(root, text="12", font=("times new roman", 50, "bold"), bg="green")
lbl_heure.place(x=600, y=300, width=200, height=130)

heure = Label(root, text="Heure", font=("times new roman", 20, "bold"), bg="green" )
heure.place(x=600, y=450, width=200, height=30)

#minute
lbl_minute= Label(root, text="30", font=("times new roman", 50, "bold"), bg="yellow")
lbl_minute.place(x=850, y=300, width=200, height=130)

minute = Label(root, text="Minute", font=("times new roman", 20, "bold"), bg="yellow")
minute.place(x=850, y=450, width=200, height=30)

#seconde
lbl_seconde= Label(root, text="50", font=("times new roman", 50,"bold"), bg="red")
lbl_seconde.place(x=1100, y=300, width=200, height=130)

seconde = Label(root, text="Seconde", font=("times new roman", 20, "bold"), bg="red" )
seconde.place(x=1100, y=450, width=200, height=30)

#alarme
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")

alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break

recupereHeure()
root.mainloop ()

