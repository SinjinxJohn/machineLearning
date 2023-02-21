import pywhatkit

phone_number = input("Enter the phone number: ")
msg = input("Enter the message: ")
time_in_hours = int(input("Enter the time in hours: "))
time_in_minutes = int(input("Enter the time in minutes: "))
def whatmsg(ph,msg,tih,tim):
    pywhatkit.sendwhatmsg(ph,msg,tih,tim)


whatmsg(phone_number,msg,time_in_hours,time_in_minutes)