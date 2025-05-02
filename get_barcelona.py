import urllib.request, json

url_tiempo = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

with urllib.request.urlopen(url_tiempo) as datos:
    parseado = json.load(datos)

    print("La temperatura en Barcelona es:", parseado["current"]["temperature_2m"])
