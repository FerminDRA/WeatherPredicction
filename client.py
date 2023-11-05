import requests

body = {
    'Humidity':0.89,
    'Wind_Speed_km_h':14.1197,
    'Wind_Bearing_degrees':251.0,
    'Visibility':15.826300000000002,
    'Pressure_millibars':1015.13
}
response = requests.post(url = 'http://127.0.0.1:8000/score',
json = body)
print (response.json())

# output: {'score': 0.866490130600765}