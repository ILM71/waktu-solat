import requests
from datetime import datetime

kota = input("Masukkan Nama kota : ")

url = f"https://nominatim.openstreetmap.org/search?city={kota}&format=json"
response = requests.get(url).json()
lat = response[0]["lat"]
lon = response[0]["lon"]

url = f"http://api.aladhan.com/v1/timings?latitude={lat}&longitude={lon}&method=2"
response = requests.get(url).json()
timings = response["data"]["timings"]

for key in timings:
    timings[key] = datetime.strptime(timings[key], "%H:%M").strftime("%I:%M %p")

today = datetime.today().strftime("%A, %B %d, %Y")
print(f"\nJadwal waktu solat untuk {kota} ({lat}, {lon}) pada {today}:\n")
print(f"Imsak: {timings['Imsak']}")
print(f"Subuh: {timings['Fajr']}")
print(f"Dhuhr: {timings['Dhuhr']}")
print(f"Ashar: {timings['Asr']}")
print(f"Maghrib: {timings['Maghrib']}")
print(f"Isya: {timings['Isha']}")
