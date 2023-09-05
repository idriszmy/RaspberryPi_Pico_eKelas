import os
import wifi
import ipaddress
import socketpool
import adafruit_requests
import ssl

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

response = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Asia/Kuala_Lumpur")

print(response.json())
print()
print(response.json()['dayOfWeek'])
print(response.json()['date'])
print(response.json()['time'])