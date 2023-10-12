import time
import os
import board
import digitalio
import simpleio
import wifi
import socketpool
import adafruit_requests
import ssl

# Telegram API url.
API_URL = "https://api.telegram.org/bot" + os.getenv("TELEGRAMBOT_TOKEN")

NOTE_G4 = 392
NOTE_C5 = 523
buzzer = board.GP18

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT

button2 = digitalio.DigitalInOut(board.GP21)
button2.direction = digitalio.Direction.INPUT

def init_bot():
    get_url = API_URL
    get_url += "/getMe"
    r = requests.get(get_url)
    return r.json()['ok']

first_read = True
update_id = 0
def read_message():
    global first_read
    global update_id
    
    get_url = API_URL
    get_url += "/getUpdates?limit=1&allowed_updates=[\"message\",\"callback_query\"]"
    if first_read == False:
        get_url += "&offset={}".format(update_id)

    r = requests.get(get_url)
    #print(r.json())
    
    try:
        update_id = r.json()['result'][0]['update_id']
        message = r.json()['result'][0]['message']['text']
        chat_id = r.json()['result'][0]['message']['chat']['id']

        #print("Update ID: {}".format(update_id))
        print("Chat ID: {}\tMessage: {}".format(chat_id, message))

        first_read = False
        update_id += 1
        simpleio.tone(buzzer, NOTE_G4, duration=0.1)
        simpleio.tone(buzzer, NOTE_C5, duration=0.1)
        
        return chat_id, message

    except (IndexError) as e:
        #print("No new message")
        return False, False

def send_message(chat_id, message):
    get_url = API_URL
    get_url += "/sendMessage?chat_id={}&text={}".format(chat_id, message)
    r = requests.get(get_url)
    #print(r.json())

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

if init_bot() == False:
    print("Telegram bot failed.")
else:
    print("Telegram bot ready!\n")
    simpleio.tone(buzzer, NOTE_C5, duration=0.1)

    while True:
        chat_id, message_in = read_message()
        
        if message_in == "/start":
            send_message(chat_id, "Selamat Datang ke Telegram Bot!")
        elif message_in == "LED ON":
            led.value = True
            send_message(chat_id, "LED menyala.")
        elif message_in == "LED OFF":
            led.value = False
            send_message(chat_id, "LED padam.")
        else:
            send_message(chat_id, "Tiada arahan.")
        
        if button1.value == False:
            print("Butang 1 ditekan")
            send_message("222209693", "Butang 1 ditekan")
            
            while button1.value == False:
                continue
        
        if button2.value == False:
            print("Butang 2 ditekan")
            send_message("222209693", "Butang 2 ditekan")
            
            while button2.value == False:
                continue
