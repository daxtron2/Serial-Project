import serial
import smtplib
import time

def send_email(safe):
    msg = ""
    if not safe:
        msg = "Warning! Unsafe humidity level detected!"
    else:
        msg = "Nominal humidity levels have returned!"

    server.sendmail(
    "tjwrazzpi@gmail.com",
    "4016994055@txt.att.net",
    msg)

def loop(startTime):
    stillMoist = False
    while True:
        currHumidity = 0.0
        read = pSerial.readline()

        if read[:4] == "SEND":
            currHumidity = float(read[5:])

            print("Unsafe Humidity of %f%%" % currHumidity)
            if stillMoist == False:
                print("Send Txt w/ %f%% humidity" % currHumidity)
                send_email(False)
                stillMoist = True
            pSerial.reset_input_buffer()
            time.sleep(1)
        elif read[:4] == "SAFE":
            if stillMoist:
                print("Back to safe humidity")
                send_email(True)
            stillMoist = False
            currTime = time.time()
            if currTime - startTime > 5:
                startTime = currTime
                currHumidity = float(read[5:])
                print("Current Humidity: %f%%" % currHumidity)
            #print("Safe Humidity")


pwFile = open("raspw.txt","r")
contents = pwFile.read()
seperated = contents.split("|")
#print(seperated[0])
#print(seperated[1])

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(seperated[0], seperated[1])

pSerial = serial.Serial("/dev/ttyUSB0", 9600)

startTime = time.time()
loop(startTime)

print("Finished")
server.quit()
