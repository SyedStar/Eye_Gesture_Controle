import pyttsx3
import RPi.GPIO as GPIO
import requests

engine = pyttsx3.init()
relay1 = 3
relay2 = 2
relay3 = 4

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.output(relay1, GPIO.LOW)
GPIO.output(relay2, GPIO.LOW)
GPIO.output(relay3, GPIO.LOW)

class Myclass:
    def __int__(self):
        pass

    def Blink(self):
        if self == 1:
            engine.say("Light on")
            engine.runAndWait()
            print("Light on")
            payload = {'cmd': '1'}
            r = requests.post('https://airobosoft.com/2023/eye-ges3/api/update_data.php', params=payload)
            print(r.url)
            GPIO.output(relay1, GPIO.HIGH)  # Turn motor on

        if self == 2:
            engine.say("Light off")
            engine.runAndWait()
            print("Light off")
            payload = {'cmd': '2'}
            r = requests.post('https://airobosoft.com/2023/eye-ges3/api/update_data.php', params=payload)
            print(r.url)
            GPIO.output(relay1, GPIO.LOW)  # Turn motor off

        if self == 3:
            engine.say("Fan on")
            engine.runAndWait()
            print("Fan on")
            payload = {'cmd': '3'}
            r = requests.post('https://airobosoft.com/2023/eye-ges3/api/update_data.php', params=payload)
            print(r.url)
            GPIO.output(relay2, GPIO.HIGH)  # Turn motor on

        if self == 4:
            engine.say("Fan off")
            engine.runAndWait()
            print("Fan off")
            payload = {'cmd': '4'}
            r = requests.post('https://airobosoft.com/2023/eye-ges3/api/update_data.php', params=payload)
            print(r.url)
            GPIO.output(relay2, GPIO.LOW)  # Turn motor off

        if self == 5:
            engine.say("bed lamp on")
            engine.runAndWait()
            print("Bed lamp on")
            payload = {'cmd': '5'}
            r = requests.post('https://airobosoft.com/2023/eye-ges3/api/update_data.php', params=payload)
            print(r.url)
            GPIO.output(relay3, GPIO.HIGH)  # Turn motor on


        if self == 6:
            engine.say("Bed lamp off")
            engine.runAndWait()
            print("Bed lamp off")
            payload = {'cmd': '6'}
            r = requests.post('https://airobosoft.com/2023/eye-ges3/api/update_data.php', params=payload)
            print(r.url)
            GPIO.output(relay3, GPIO.LOW)  # Turn motor off